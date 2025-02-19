equivalence_classes = {0: [], 1: [], 2: [], 3: [], 4: []}

for num in range(1, 10001):
    remainder = num % 5
    equivalence_classes[remainder].append(num)