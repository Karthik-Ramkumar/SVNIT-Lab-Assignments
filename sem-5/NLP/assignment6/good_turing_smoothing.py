import random
import math
import numpy as np
from collections import Counter

# Data loading config
file_path = "../assignment1/word_tokenized.txt"
MAX_SENTENCES = 1000000
MIN_COUNT = 2
GT_THRESHOLD = 5
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
dev_set_raw  = sentences[:1000]
test_set_raw = sentences[1000:2000]
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
unigram_counts   = Counter()
bigram_counts    = Counter()
bigram_contexts  = Counter()
trigram_counts   = Counter()
trigram_contexts = Counter()
quadgram_counts  = Counter()
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

# Count of counts for each n-gram order
N_c_bi   = Counter(bigram_counts.values())
N_c_tri  = Counter(trigram_counts.values())
N_c_quad = Counter(quadgram_counts.values())


# Good-Turing smoothed count for a raw count c using count-of-counts table
def gt_smooth(c, N_c):
    if c <= 0 or c > GT_THRESHOLD:
        return float(c)
    nc  = N_c.get(c, 0)
    nc1 = N_c.get(c + 1, 0)
    if nc > 0 and nc1 > 0:
        return (c + 1) * nc1 / nc
    return float(c)


# Reserved probability mass for unseen n-grams: N1 / total_ngram_tokens
# Distributed proportional to unigram probability of the last word
total_bi_tokens   = sum(bigram_counts.values())
total_tri_tokens  = sum(trigram_counts.values())
total_quad_tokens = sum(quadgram_counts.values())

p0_bi_mass   = N_c_bi.get(1, 0)   / max(total_bi_tokens, 1)
p0_tri_mass  = N_c_tri.get(1, 0)  / max(total_tri_tokens, 1)
p0_quad_mass = N_c_quad.get(1, 0) / max(total_quad_tokens, 1)


def perplexity(log_prob_sum, token_count):
    return math.exp(-log_prob_sum / token_count)


# Bigram Good-Turing perplexity
def bigram_gt_ppl(dataset):
    log_prob_sum = 0.0
    total = 0
    for sent in dataset:
        ids = sent.tolist()
        for i in range(1, len(ids)):
            w1, w2 = ids[i-1], ids[i]
            c   = bigram_counts.get((w1, w2), 0)
            ctx = bigram_contexts.get((w1,), 0)
            if c == 0 or ctx == 0:
                prob = p0_bi_mass * unigram_counts.get(w2, 0) / N
            else:
                prob = gt_smooth(c, N_c_bi) / ctx
            log_prob_sum += math.log(max(prob, 1e-10))
            total += 1
    return perplexity(log_prob_sum, total)


# Trigram Good-Turing perplexity
def trigram_gt_ppl(dataset):
    log_prob_sum = 0.0
    total = 0
    for sent in dataset:
        ids = sent.tolist()
        for i in range(2, len(ids)):
            w1, w2, w3 = ids[i-2], ids[i-1], ids[i]
            c   = trigram_counts.get((w1, w2, w3), 0)
            ctx = trigram_contexts.get((w1, w2), 0)
            if c == 0 or ctx == 0:
                prob = p0_tri_mass * unigram_counts.get(w3, 0) / N
            else:
                prob = gt_smooth(c, N_c_tri) / ctx
            log_prob_sum += math.log(max(prob, 1e-10))
            total += 1
    return perplexity(log_prob_sum, total)


# Quadgram Good-Turing perplexity
def quadgram_gt_ppl(dataset):
    log_prob_sum = 0.0
    total = 0
    for sent in dataset:
        ids = sent.tolist()
        for i in range(3, len(ids)):
            w1, w2, w3, w4 = ids[i-3], ids[i-2], ids[i-1], ids[i]
            c   = quadgram_counts.get((w1, w2, w3, w4), 0)
            ctx = quadgram_contexts.get((w1, w2, w3), 0)
            if c == 0 or ctx == 0:
                prob = p0_quad_mass * unigram_counts.get(w4, 0) / N
            else:
                prob = gt_smooth(c, N_c_quad) / ctx
            log_prob_sum += math.log(max(prob, 1e-10))
            total += 1
    return perplexity(log_prob_sum, total)


print("\nBigram Good-Turing Smoothing:")
print(f"Dev  Perplexity: {bigram_gt_ppl(dev_set):.4f}")
print(f"Test Perplexity: {bigram_gt_ppl(test_set):.4f}")

print("\nTrigram Good-Turing Smoothing:")
print(f"Dev  Perplexity: {trigram_gt_ppl(dev_set):.4f}")
print(f"Test Perplexity: {trigram_gt_ppl(test_set):.4f}")

print("\nQuadgram Good-Turing Smoothing:")
print(f"Dev  Perplexity: {quadgram_gt_ppl(dev_set):.4f}")
print(f"Test Perplexity: {quadgram_gt_ppl(test_set):.4f}")

del (unigram_counts, bigram_counts, bigram_contexts,
     trigram_counts, trigram_contexts,
     quadgram_counts, quadgram_contexts,
     N_c_bi, N_c_tri, N_c_quad)
