import random
import math
import numpy as np
from collections import Counter

# Data loading config
file_path = "../assignment1/word_tokenized.txt"
MAX_SENTENCES = 1000000
MIN_COUNT = 2
random.seed(42)


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


# Load, shuffle, split
sentences = []
for sentence in read_sentences():
    sentences.append(sentence)
    if len(sentences) >= MAX_SENTENCES:
        break

random.shuffle(sentences)
dev_set_raw   = sentences[:1000]
test_set_raw  = sentences[1000:2000]
train_set_raw = sentences[2000:]
del sentences

print(f"Training set size:    {len(train_set_raw)} sentences")
print(f"Development set size: {len(dev_set_raw)} sentences")
print(f"Test set size:        {len(test_set_raw)} sentences")

# Build vocab from training set
word_counts = Counter(word for s in train_set_raw for word in s)
vocab = {word for word, cnt in word_counts.items() if cnt >= MIN_COUNT}
vocab.add("<UNK>")
del word_counts

word2id = {word: idx for idx, word in enumerate(vocab)}
unk_id = word2id["<UNK>"]
V = len(vocab)
print(f"Vocabulary size: {V}")


def encode_sentences(data):
    return [np.array([word2id.get(w, unk_id) for w in sent], dtype=np.int32)
            for sent in data]


train_set = encode_sentences(train_set_raw)
dev_set   = encode_sentences(dev_set_raw)
test_set  = encode_sentences(test_set_raw)
del train_set_raw, dev_set_raw, test_set_raw

N = sum(len(s) for s in train_set)
print(f"Training tokens: {N}")

# Single-pass build of all n-gram counts
unigram_counts    = Counter()
bigram_counts     = Counter()
bigram_contexts   = Counter()
trigram_counts    = Counter()
trigram_contexts  = Counter()
quadgram_counts   = Counter()
quadgram_contexts = Counter()

for sent in train_set:
    ids = sent.tolist()
    L = len(ids)
    for i in range(L):
        unigram_counts[ids[i]] += 1
        if i >= 1:
            bigram_counts[(ids[i-1], ids[i])] += 1
            bigram_contexts[(ids[i-1],)] += 1
        if i >= 2:
            trigram_counts[(ids[i-2], ids[i-1], ids[i])] += 1
            trigram_contexts[(ids[i-2], ids[i-1])] += 1
        if i >= 3:
            quadgram_counts[(ids[i-3], ids[i-2], ids[i-1], ids[i])] += 1
            quadgram_contexts[(ids[i-3], ids[i-2], ids[i-1])] += 1

print(f"Unique bigrams: {len(bigram_counts)}, trigrams: {len(trigram_counts)}, quadgrams: {len(quadgram_counts)}")

# Continuation counts for Kneser-Ney
# left_bi[w]  = number of unique left contexts for unigram w in bigrams
# types_bi[w] = number of unique right words following w in bigrams
left_bi  = Counter()
types_bi = Counter()
for (w1, w2) in bigram_counts:
    left_bi[w2]  += 1
    types_bi[w1] += 1

total_bi_types = len(bigram_counts)  # denominator for unigram continuation prob

# left_tri[(w2,w3)] = unique left contexts for bigram (w2,w3) in trigrams
# types_tri[(w1,w2)] = unique right words following bigram (w1,w2) in trigrams
left_tri  = Counter()
types_tri = Counter()
for (w1, w2, w3) in trigram_counts:
    left_tri[(w2, w3)]  += 1
    types_tri[(w1, w2)] += 1

total_tri_types = len(trigram_counts)  # denominator for bigram continuation prob

# left_quad[(w2,w3,w4)] = unique left contexts for trigram (w2,w3,w4) in quadgrams
# types_quad[(w1,w2,w3)] = unique right words following trigram in quadgrams
left_quad  = Counter()
types_quad = Counter()
for (w1, w2, w3, w4) in quadgram_counts:
    left_quad[(w2, w3, w4)]   += 1
    types_quad[(w1, w2, w3)]  += 1

total_quad_types = len(quadgram_counts)  # denominator for trigram continuation prob


def perplexity(log_prob_sum, token_count):
    return math.exp(-log_prob_sum / token_count)


# Kneser-Ney probability functions for each n-gram order
# P_KN(w) = continuation count / total bigram types  (unigram base)
def p_kn_uni(w):
    return left_bi.get(w, 0) / max(total_bi_types, 1)


# P_KN(w2|w1) = max(c(w1,w2)-D, 0)/c(w1) + lambda(w1)*P_KN(w2)
def p_kn_bi(w1, w2, D):
    ctx = bigram_contexts.get((w1,), 0)
    if ctx == 0:
        return p_kn_uni(w2)
    c = bigram_counts.get((w1, w2), 0)
    disc_part = max(c - D, 0.0) / ctx
    lam = D * types_bi.get(w1, 0) / ctx
    return disc_part + lam * p_kn_uni(w2)


# P_KN(w3|w1,w2) = max(c(w1,w2,w3)-D,0)/c(w1,w2) + lambda(w1,w2)*P_KN(w3|w2)
def p_kn_tri(w1, w2, w3, D):
    ctx = trigram_contexts.get((w1, w2), 0)
    if ctx == 0:
        return p_kn_bi(w2, w3, D)
    c = trigram_counts.get((w1, w2, w3), 0)
    disc_part = max(c - D, 0.0) / ctx
    lam = D * types_tri.get((w1, w2), 0) / ctx
    return disc_part + lam * p_kn_bi(w2, w3, D)


# P_KN(w4|w1,w2,w3) = max(c(quad)-D,0)/c(tri_ctx) + lambda(tri_ctx)*P_KN(w4|w2,w3)
def p_kn_quad(w1, w2, w3, w4, D):
    ctx = quadgram_contexts.get((w1, w2, w3), 0)
    if ctx == 0:
        return p_kn_tri(w2, w3, w4, D)
    c = quadgram_counts.get((w1, w2, w3, w4), 0)
    disc_part = max(c - D, 0.0) / ctx
    lam = D * types_quad.get((w1, w2, w3), 0) / ctx
    return disc_part + lam * p_kn_tri(w2, w3, w4, D)


def bigram_kn_ppl(dataset, D):
    log_prob_sum = 0.0
    total = 0
    for sent in dataset:
        ids = sent.tolist()
        for i in range(1, len(ids)):
            prob = p_kn_bi(ids[i-1], ids[i], D)
            log_prob_sum += math.log(max(prob, 1e-10))
            total += 1
    return math.exp(-log_prob_sum / total)


def trigram_kn_ppl(dataset, D):
    log_prob_sum = 0.0
    total = 0
    for sent in dataset:
        ids = sent.tolist()
        for i in range(2, len(ids)):
            prob = p_kn_tri(ids[i-2], ids[i-1], ids[i], D)
            log_prob_sum += math.log(max(prob, 1e-10))
            total += 1
    return math.exp(-log_prob_sum / total)


def quadgram_kn_ppl(dataset, D):
    log_prob_sum = 0.0
    total = 0
    for sent in dataset:
        ids = sent.tolist()
        for i in range(3, len(ids)):
            prob = p_kn_quad(ids[i-3], ids[i-2], ids[i-1], ids[i], D)
            log_prob_sum += math.log(max(prob, 1e-10))
            total += 1
    return math.exp(-log_prob_sum / total)


# Optimize discount D on dev set across a small grid
D_candidates = [0.5, 0.6, 0.7, 0.75, 0.8, 0.9]

best_bi_D, best_bi_ppl = 0.75, float("inf")
for D in D_candidates:
    ppl = bigram_kn_ppl(dev_set, D)
    if ppl < best_bi_ppl:
        best_bi_ppl, best_bi_D = ppl, D

print(f"Best D={best_bi_D} | Bigram KN Dev  Perplexity: {best_bi_ppl:.4f}")
print(f"Bigram KN Test Perplexity: {bigram_kn_ppl(test_set, best_bi_D):.4f}")

best_tri_D, best_tri_ppl = 0.75, float("inf")
for D in D_candidates:
    ppl = trigram_kn_ppl(dev_set, D)
    if ppl < best_tri_ppl:
        best_tri_ppl, best_tri_D = ppl, D

print(f"Best D={best_tri_D} | Trigram KN Dev  Perplexity: {best_tri_ppl:.4f}")
print(f"Trigram KN Test Perplexity: {trigram_kn_ppl(test_set, best_tri_D):.4f}")

print("\nOptimizing discount D for Quadgram KN on dev set...")
best_quad_D, best_quad_ppl = 0.75, float("inf")
for D in D_candidates:
    ppl = quadgram_kn_ppl(dev_set, D)
    if ppl < best_quad_ppl:
        best_quad_ppl, best_quad_D = ppl, D

print(f"Best D={best_quad_D} | Quadgram KN Dev  Perplexity: {best_quad_ppl:.4f}")
print(f"Quadgram KN Test Perplexity: {quadgram_kn_ppl(test_set, best_quad_D):.4f}")

del (unigram_counts, bigram_counts, bigram_contexts,
     trigram_counts, trigram_contexts,
     quadgram_counts, quadgram_contexts,
     left_bi, types_bi, left_tri, types_tri, left_quad, types_quad)
