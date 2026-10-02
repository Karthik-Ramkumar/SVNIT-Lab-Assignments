import random
import math
import numpy as np
from collections import Counter

# Data loading config
file_path = "../assignment1/word_tokenized.txt"
MAX_SENTENCES = 1000000
MIN_COUNT = 2
ALPHA = 0.4  # backoff penalty per order
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


def perplexity(log_prob_sum, token_count):
    return math.exp(-log_prob_sum / token_count)


# Bigram Stupid Backoff: MLE if seen, else ALPHA * P_unigram
def bigram_sb_ppl(dataset):
    log_prob_sum = 0.0
    total = 0
    for sent in dataset:
        ids = sent.tolist()
        for i in range(1, len(ids)):
            w1, w2 = ids[i-1], ids[i]
            c_bi = bigram_counts.get((w1, w2), 0)
            ctx  = bigram_contexts.get((w1,), 0)
            if c_bi > 0 and ctx > 0:
                prob = c_bi / ctx
            else:
                prob = ALPHA * unigram_counts.get(w2, 0) / N
            log_prob_sum += math.log(max(prob, 1e-10))
            total += 1
    return perplexity(log_prob_sum, total)


# Trigram Stupid Backoff: cascade through bigram then unigram
def trigram_sb_ppl(dataset):
    log_prob_sum = 0.0
    total = 0
    for sent in dataset:
        ids = sent.tolist()
        for i in range(2, len(ids)):
            w1, w2, w3 = ids[i-2], ids[i-1], ids[i]
            c_tri = trigram_counts.get((w1, w2, w3), 0)
            ctx_tri = trigram_contexts.get((w1, w2), 0)
            if c_tri > 0 and ctx_tri > 0:
                prob = c_tri / ctx_tri
            else:
                c_bi = bigram_counts.get((w2, w3), 0)
                ctx_bi = bigram_contexts.get((w2,), 0)
                if c_bi > 0 and ctx_bi > 0:
                    prob = ALPHA * c_bi / ctx_bi
                else:
                    prob = ALPHA * ALPHA * unigram_counts.get(w3, 0) / N
            log_prob_sum += math.log(max(prob, 1e-10))
            total += 1
    return perplexity(log_prob_sum, total)


# Quadgram Stupid Backoff: cascade through trigram, bigram, unigram
def quadgram_sb_ppl(dataset):
    log_prob_sum = 0.0
    total = 0
    for sent in dataset:
        ids = sent.tolist()
        for i in range(3, len(ids)):
            w1, w2, w3, w4 = ids[i-3], ids[i-2], ids[i-1], ids[i]
            c_quad = quadgram_counts.get((w1, w2, w3, w4), 0)
            ctx_quad = quadgram_contexts.get((w1, w2, w3), 0)
            if c_quad > 0 and ctx_quad > 0:
                prob = c_quad / ctx_quad
            else:
                c_tri = trigram_counts.get((w2, w3, w4), 0)
                ctx_tri = trigram_contexts.get((w2, w3), 0)
                if c_tri > 0 and ctx_tri > 0:
                    prob = ALPHA * c_tri / ctx_tri
                else:
                    c_bi = bigram_counts.get((w3, w4), 0)
                    ctx_bi = bigram_contexts.get((w3,), 0)
                    if c_bi > 0 and ctx_bi > 0:
                        prob = ALPHA * ALPHA * c_bi / ctx_bi
                    else:
                        prob = ALPHA ** 3 * unigram_counts.get(w4, 0) / N
            log_prob_sum += math.log(max(prob, 1e-10))
            total += 1
    return perplexity(log_prob_sum, total)


print("\nBigram Stupid Backoff (alpha=0.4):")
print(f"Dev  Perplexity: {bigram_sb_ppl(dev_set):.4f}")
print(f"Test Perplexity: {bigram_sb_ppl(test_set):.4f}")

print("\nTrigram Stupid Backoff (alpha=0.4):")
print(f"Dev  Perplexity: {trigram_sb_ppl(dev_set):.4f}")
print(f"Test Perplexity: {trigram_sb_ppl(test_set):.4f}")

print("\nQuadgram Stupid Backoff (alpha=0.4):")
print(f"Dev  Perplexity: {quadgram_sb_ppl(dev_set):.4f}")
print(f"Test Perplexity: {quadgram_sb_ppl(test_set):.4f}")

del (unigram_counts, bigram_counts, bigram_contexts,
     trigram_counts, trigram_contexts,
     quadgram_counts, quadgram_contexts)
