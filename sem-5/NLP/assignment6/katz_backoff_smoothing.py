import random
import math
import numpy as np
from collections import Counter, defaultdict

# Data loading config
file_path = "../assignment1/word_tokenized.txt"
MAX_SENTENCES = 1000000
MIN_COUNT = 2
GT_THRESHOLD = 5  # apply GT discounting only for counts <= this
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

# Count of counts for GT discounting
N_c_bi   = Counter(bigram_counts.values())
N_c_tri  = Counter(trigram_counts.values())
N_c_quad = Counter(quadgram_counts.values())


# GT discount ratio d(c) = c* / c where c* is the GT smoothed count
def gt_discount(c, N_c):
    if c <= 0 or c > GT_THRESHOLD:
        return 1.0
    nc  = N_c.get(c, 0)
    nc1 = N_c.get(c + 1, 0)
    if nc > 0 and nc1 > 0:
        return ((c + 1) * nc1 / nc) / c
    return 1.0


# Precompute bigram alpha: alpha_bi[w1] = backoff weight for unseen bigram given w1
# alpha = (1 - discounted_mass_seen) / (1 - unigram_mass_seen)
disc_mass_bi = defaultdict(float)
uni_mass_bi  = defaultdict(float)

for (w1, w2), c in bigram_counts.items():
    ctx = bigram_contexts.get((w1,), 1)
    disc_mass_bi[w1] += gt_discount(c, N_c_bi) * c / ctx
    uni_mass_bi[w1]  += unigram_counts.get(w2, 0) / N

alpha_bi = {}
for w1 in disc_mass_bi:
    num = max(1.0 - disc_mass_bi[w1], 0.0)
    den = max(1.0 - uni_mass_bi[w1], 1e-10)
    alpha_bi[w1] = num / den
del disc_mass_bi, uni_mass_bi


# Precompute trigram alpha: alpha_tri[(w1,w2)] using discounted trigram and Katz bigram masses
disc_mass_tri   = defaultdict(float)
katz_bi_mass_tri = defaultdict(float)

for (w1, w2, w3), c in trigram_counts.items():
    ctx = trigram_contexts.get((w1, w2), 1)
    disc_mass_tri[(w1, w2)] += gt_discount(c, N_c_tri) * c / ctx

    c_bi  = bigram_counts.get((w2, w3), 0)
    ctx_bi = bigram_contexts.get((w2,), 0)
    if c_bi > 0 and ctx_bi > 0:
        p_katz_bi = gt_discount(c_bi, N_c_bi) * c_bi / ctx_bi
    else:
        p_katz_bi = alpha_bi.get(w2, 1.0) * unigram_counts.get(w3, 0) / N
    katz_bi_mass_tri[(w1, w2)] += p_katz_bi

alpha_tri = {}
for ctx in disc_mass_tri:
    num = max(1.0 - disc_mass_tri[ctx], 0.0)
    den = max(1.0 - katz_bi_mass_tri[ctx], 1e-10)
    alpha_tri[ctx] = num / den
del disc_mass_tri, katz_bi_mass_tri


# Precompute quadgram alpha: uses discounted quadgram and Katz trigram masses
disc_mass_quad    = defaultdict(float)
katz_tri_mass_quad = defaultdict(float)

for (w1, w2, w3, w4), c in quadgram_counts.items():
    ctx = quadgram_contexts.get((w1, w2, w3), 1)
    disc_mass_quad[(w1, w2, w3)] += gt_discount(c, N_c_quad) * c / ctx

    c_tri  = trigram_counts.get((w2, w3, w4), 0)
    ctx_tri = trigram_contexts.get((w2, w3), 0)
    if c_tri > 0 and ctx_tri > 0:
        p_katz_tri = gt_discount(c_tri, N_c_tri) * c_tri / ctx_tri
    else:
        c_bi  = bigram_counts.get((w3, w4), 0)
        ctx_bi = bigram_contexts.get((w3,), 0)
        if c_bi > 0 and ctx_bi > 0:
            p_katz_bi = gt_discount(c_bi, N_c_bi) * c_bi / ctx_bi
        else:
            p_katz_bi = alpha_bi.get(w3, 1.0) * unigram_counts.get(w4, 0) / N
        p_katz_tri = alpha_tri.get((w2, w3), 1.0) * p_katz_bi
    katz_tri_mass_quad[(w1, w2, w3)] += p_katz_tri

alpha_quad = {}
for ctx in disc_mass_quad:
    num = max(1.0 - disc_mass_quad[ctx], 0.0)
    den = max(1.0 - katz_tri_mass_quad[ctx], 1e-10)
    alpha_quad[ctx] = num / den
del disc_mass_quad, katz_tri_mass_quad


def perplexity(log_prob_sum, token_count):
    return math.exp(-log_prob_sum / token_count)


# Katz backoff probability functions
def p_katz_bi(w1, w2):
    c   = bigram_counts.get((w1, w2), 0)
    ctx = bigram_contexts.get((w1,), 0)
    if c > 0 and ctx > 0:
        return gt_discount(c, N_c_bi) * c / ctx
    return alpha_bi.get(w1, 1.0) * unigram_counts.get(w2, 0) / N


def p_katz_tri(w1, w2, w3):
    c   = trigram_counts.get((w1, w2, w3), 0)
    ctx = trigram_contexts.get((w1, w2), 0)
    if c > 0 and ctx > 0:
        return gt_discount(c, N_c_tri) * c / ctx
    return alpha_tri.get((w1, w2), 1.0) * p_katz_bi(w2, w3)


def p_katz_quad(w1, w2, w3, w4):
    c   = quadgram_counts.get((w1, w2, w3, w4), 0)
    ctx = quadgram_contexts.get((w1, w2, w3), 0)
    if c > 0 and ctx > 0:
        return gt_discount(c, N_c_quad) * c / ctx
    return alpha_quad.get((w1, w2, w3), 1.0) * p_katz_tri(w2, w3, w4)


def bigram_katz_ppl(dataset):
    log_prob_sum = 0.0
    total = 0
    for sent in dataset:
        ids = sent.tolist()
        for i in range(1, len(ids)):
            prob = p_katz_bi(ids[i-1], ids[i])
            log_prob_sum += math.log(max(prob, 1e-10))
            total += 1
    return perplexity(log_prob_sum, total)


def trigram_katz_ppl(dataset):
    log_prob_sum = 0.0
    total = 0
    for sent in dataset:
        ids = sent.tolist()
        for i in range(2, len(ids)):
            prob = p_katz_tri(ids[i-2], ids[i-1], ids[i])
            log_prob_sum += math.log(max(prob, 1e-10))
            total += 1
    return perplexity(log_prob_sum, total)


def quadgram_katz_ppl(dataset):
    log_prob_sum = 0.0
    total = 0
    for sent in dataset:
        ids = sent.tolist()
        for i in range(3, len(ids)):
            prob = p_katz_quad(ids[i-3], ids[i-2], ids[i-1], ids[i])
            log_prob_sum += math.log(max(prob, 1e-10))
            total += 1
    return perplexity(log_prob_sum, total)


print("\nBigram Katz Backoff Smoothing:")
print(f"Dev  Perplexity: {bigram_katz_ppl(dev_set):.4f}")
print(f"Test Perplexity: {bigram_katz_ppl(test_set):.4f}")

print("\nTrigram Katz Backoff Smoothing:")
print(f"Dev  Perplexity: {trigram_katz_ppl(dev_set):.4f}")
print(f"Test Perplexity: {trigram_katz_ppl(test_set):.4f}")

print("\nQuadgram Katz Backoff Smoothing:")
print(f"Dev  Perplexity: {quadgram_katz_ppl(dev_set):.4f}")
print(f"Test Perplexity: {quadgram_katz_ppl(test_set):.4f}")

del (unigram_counts, bigram_counts, bigram_contexts,
     trigram_counts, trigram_contexts,
     quadgram_counts, quadgram_contexts,
     alpha_bi, alpha_tri, alpha_quad,
     N_c_bi, N_c_tri, N_c_quad)
