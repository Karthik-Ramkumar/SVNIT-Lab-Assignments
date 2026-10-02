import json

sentences = []
with open("../assignment1/sentence_tokenized.json", "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        line = line.strip()
        if line in ["[", "]"]:
            continue
        if line.endswith(","):
            line = line[:-1]
        if not line:
            continue
        try:
            sentence = json.loads(line)
            sentences.append(sentence)
        except Exception as e:
            print(f"Error on line {i}: {line} -> {e}")
            break
        if len(sentences) >= 10:
            break

for s in sentences:
    print(s)
