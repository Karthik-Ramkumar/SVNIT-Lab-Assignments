import random
import math
import numpy as np
from collections import Counter

# Data loading config
file_path = "../assignment1/word_tokenized.txt"
MAX_SENTENCES = 1000000
MIN_COUNT = 2
random.seed(42)


# Read sentences from word-tokenized file (blank line delimited)
def read_sentences():
    sentence = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            word = line.strip()
            if word:
                sentence.append(word)
            elif sentence:
                yield sentence
                sentence = []
        if sentence:
            yield sentence


# Load up to MAX_SENTENCES, shuffle, split into train/dev/test
print("Loading sentences...")
sentences = []
for sentence in read_sentences():
    sentences.append(sentence)
    if len(sentences) >= MAX_SENTENCES:
        break

random.shuffle(sentences)
dev_set_raw = sentences[:1000]
test_set_raw = sentences[1000:2000]
train_set_raw = sentences[2000:]

print(f"Training set size:    {len(train_set_raw)} sentences")
print(f"Development set size: {len(dev_set_raw)} sentences")
print(f"Test set size:        {len(test_set_raw)} sentences")


# Build vocab from training set
word_counts = Counter(word for sentence in train_set_raw for word in sentence)
vocab = {word for word, count in word_counts.items() if count >= MIN_COUNT}
vocab.add("<UNK>")
del word_counts

# Assign integer IDs for memory-efficient storage
word2id = {word: idx for idx, word in enumerate(vocab)}
unk_id = word2id["<UNK>"]
V = len(vocab)
print(f"Vocabulary size: {V}")


# Encode a list of string sentences to numpy int32 arrays
def encode_sentences(data):
    return [np.array([word2id.get(w, unk_id) for w in sent], dtype=np.int32)
            for sent in data]


train_set = encode_sentences(train_set_raw)
dev_set = encode_sentences(dev_set_raw)
test_set = encode_sentences(test_set_raw)
del train_set_raw, dev_set_raw, test_set_raw

N = sum(len(s) for s in train_set)


# Single-pass build of all n-gram count tables (uni, bi, tri, quad)
# Contexts (prefix counts) needed for conditional probabilities
unigram_counts = Counter()
bigram_counts = Counter()
bigram_contexts = Counter()
trigram_counts = Counter()
trigram_contexts = Counter()
quadgram_counts = Counter()
quadgram_contexts = Counter()

for sent in train_set:
    length = len(sent)
    for i in range(length):
        w0 = int(sent[i])
        unigram_counts[w0] += 1

        if i >= 1:
            w1 = int(sent[i - 1])
            bigram_counts[(w1, w0)] += 1
            bigram_contexts[(w1,)] += 1

        if i >= 2:
            w2 = int(sent[i - 2])
            trigram_counts[(w2, w1, w0)] += 1
            trigram_contexts[(w2, w1)] += 1

        if i >= 3:
            w3 = int(sent[i - 3])
            quadgram_counts[(w3, w2, w1, w0)] += 1
            quadgram_contexts[(w3, w2, w1)] += 1

print(f"Unique unigrams:  {len(unigram_counts)}")
print(f"Unique bigrams:   {len(bigram_counts)}")
print(f"Unique trigrams:  {len(trigram_counts)}")
print(f"Unique quadgrams: {len(quadgram_counts)}")


# Perplexity from accumulated log-probability and token count
def perplexity(log_prob_sum, token_count):
    return math.exp(-log_prob_sum / token_count)


# ---- Bigram Interpolated Smoothing ----
# P(w2|w1) = l1 * P(w2) + l2 * P(w2|w1)

def bigram_interp_ppl(dataset, l1, l2):
    log_prob_sum = 0.0
    total = 0
    for sent in dataset:
        for i in range(1, len(sent)):
            w1, w2 = int(sent[i - 1]), int(sent[i])
            p_uni = unigram_counts[w2] / N
            ctx = bigram_contexts.get((w1,), 0)
            p_bi = bigram_counts.get((w1, w2), 0) / ctx if ctx > 0 else 0.0
            prob = l1 * p_uni + l2 * p_bi
            log_prob_sum += math.log(prob if prob > 0 else 1e-10)
            total += 1
    return perplexity(log_prob_sum, total)


best_bi_ppl = float("inf")
best_bi_lambdas = (0.5, 0.5)

for l2_i in range(1, 10):
    l2 = round(l2_i * 0.1, 1)
    l1 = round(1.0 - l2, 1)
    ppl = bigram_interp_ppl(dev_set, l1, l2)
    if ppl < best_bi_ppl:
        best_bi_ppl = ppl
        best_bi_lambdas = (l1, l2)

l1_bi, l2_bi = best_bi_lambdas
print(f"Best bigram lambdas:  l1={l1_bi}, l2={l2_bi}")
print(f"Bigram Interpolated Dev  Perplexity: {best_bi_ppl:.4f}")
print(f"Bigram Interpolated Test Perplexity: {bigram_interp_ppl(test_set, l1_bi, l2_bi):.4f}")


#  Trigram Interpolated Smoothing 
# P(w3|w1,w2) = l1 * P(w3) + l2 * P(w3|w2) + l3 * P(w3|w1,w2)

def trigram_interp_ppl(dataset, l1, l2, l3):
    log_prob_sum = 0.0
    total = 0
    for sent in dataset:
        for i in range(2, len(sent)):
            w1, w2, w3 = int(sent[i - 2]), int(sent[i - 1]), int(sent[i])
            p_uni = unigram_counts[w3] / N
            ctx_bi = bigram_contexts.get((w2,), 0)
            p_bi = bigram_counts.get((w2, w3), 0) / ctx_bi if ctx_bi > 0 else 0.0
            ctx_tri = trigram_contexts.get((w1, w2), 0)
            p_tri = trigram_counts.get((w1, w2, w3), 0) / ctx_tri if ctx_tri > 0 else 0.0
            prob = l1 * p_uni + l2 * p_bi + l3 * p_tri
            log_prob_sum += math.log(prob if prob > 0 else 1e-10)
            total += 1
    return perplexity(log_prob_sum, total)


best_tri_ppl = float("inf")
best_tri_lambdas = (0.33, 0.33, 0.34)

step_vals = [round(i * 0.1, 1) for i in range(1, 9)]
for l3 in step_vals:
    for l2 in step_vals:
        l1 = round(1.0 - l2 - l3, 1)
        if l1 < 0 or abs(l1 + l2 + l3 - 1.0) > 1e-5:
            continue
        ppl = trigram_interp_ppl(dev_set, l1, l2, l3)
        if ppl < best_tri_ppl:
            best_tri_ppl = ppl
            best_tri_lambdas = (l1, l2, l3)

l1_tri, l2_tri, l3_tri = best_tri_lambdas
print(f"Best trigram lambdas: l1={l1_tri}, l2={l2_tri}, l3={l3_tri}")
print(f"Trigram Interpolated Dev  Perplexity: {best_tri_ppl:.4f}")
print(f"Trigram Interpolated Test Perplexity: {trigram_interp_ppl(test_set, l1_tri, l2_tri, l3_tri):.4f}")


#  Quadgram Interpolated Smoothing 
# P(w4|w1,w2,w3) = l1*P(w4) + l2*P(w4|w3) + l3*P(w4|w2,w3) + l4*P(w4|w1,w2,w3)

def quadgram_interp_ppl(dataset, l1, l2, l3, l4):
    log_prob_sum = 0.0
    total = 0
    for sent in dataset:
        for i in range(3, len(sent)):
            w1, w2, w3, w4 = int(sent[i - 3]), int(sent[i - 2]), int(sent[i - 1]), int(sent[i])
            p_uni = unigram_counts[w4] / N
            ctx_bi = bigram_contexts.get((w3,), 0)
            p_bi = bigram_counts.get((w3, w4), 0) / ctx_bi if ctx_bi > 0 else 0.0
            ctx_tri = trigram_contexts.get((w2, w3), 0)
            p_tri = trigram_counts.get((w2, w3, w4), 0) / ctx_tri if ctx_tri > 0 else 0.0
            ctx_quad = quadgram_contexts.get((w1, w2, w3), 0)
            p_quad = quadgram_counts.get((w1, w2, w3, w4), 0) / ctx_quad if ctx_quad > 0 else 0.0
            prob = l1 * p_uni + l2 * p_bi + l3 * p_tri + l4 * p_quad
            log_prob_sum += math.log(prob if prob > 0 else 1e-10)
            total += 1
    return perplexity(log_prob_sum, total)


best_quad_ppl = float("inf")
best_quad_lambdas = (0.25, 0.25, 0.25, 0.25)

for l4 in step_vals:
    for l3 in step_vals:
        for l2 in step_vals:
            l1 = round(1.0 - l2 - l3 - l4, 1)
            if l1 < 0 or abs(l1 + l2 + l3 + l4 - 1.0) > 1e-5:
                continue
            ppl = quadgram_interp_ppl(dev_set, l1, l2, l3, l4)
            if ppl < best_quad_ppl:
                best_quad_ppl = ppl
                best_quad_lambdas = (l1, l2, l3, l4)

l1_q, l2_q, l3_q, l4_q = best_quad_lambdas
print(f"Best quadgram lambdas: l1={l1_q}, l2={l2_q}, l3={l3_q}, l4={l4_q}")
print(f"Quadgram Interpolated Dev  Perplexity: {best_quad_ppl:.4f}")
print(f"Quadgram Interpolated Test Perplexity: {quadgram_interp_ppl(test_set, l1_q, l2_q, l3_q, l4_q):.4f}")

# Free all n-gram tables
del unigram_counts, bigram_counts, bigram_contexts
del trigram_counts, trigram_contexts
del quadgram_counts, quadgram_contexts
del train_set, dev_set, test_set

# Training set size:    998000 sentences
# Development set size: 1000 sentences
# Test set size:        1000 sentences
# Vocabulary size: 135022
# Unique unigrams:  135022
# Unique bigrams:   3097966
# Unique trigrams:  8902722
# Unique quadgrams: 12552325
# Best bigram lambdas:  l1=0.2, l2=0.8
# Bigram Interpolated Dev  Perplexity: 260.3685
# Bigram Interpolated Test Perplexity: 293.7564
# Best trigram lambdas: l1=0.2, l2=0.5, l3=0.3
# Trigram Interpolated Dev  Perplexity: 193.0254
# Trigram Interpolated Test Perplexity: 225.8786
# Best quadgram lambdas: l1=0.2, l2=0.4, l3=0.3, l4=0.1
# Quadgram Interpolated Dev  Perplexity: 190.2800
# Quadgram Interpolated Test Perplexity: 225.1534