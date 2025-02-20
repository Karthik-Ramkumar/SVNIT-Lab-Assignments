t = int(input())

for _ in range(t):
    w = list(input().strip())
    #checking from right
    for i in range(len(w) - 2, -1, -1):
        if w[i] < w[i + 1]:
            break
    else:
        print("no answer")
        continue
    
    #finding smallest character on the right side 
    for j in range(len(w) - 1, i, -1):
        if w[j] > w[i]:
            w[i], w[j] = w[j], w[i]  
            break
    
    w = w[:i + 1] + w[i + 1:][::-1]
    
    print("".join(w))
print(f"Input: {t}")
for _ in range(t):
    w = list(input().strip())
    print(f"Original string: {''.join(w)}")
    #checking from right
    for i in range(len(w) - 2, -1, -1):
        if w[i] < w[i + 1]:
            print(f"Found decreasing character at index {i}")
            break
    else:
        print("no answer")
        continue
    
    #finding smallest character on the right side 
    for j in range(len(w) - 1, i, -1):
        if w[j] > w[i]:
            print(f"Swapping characters at indices {i} and {j}")
            w[i], w[j] = w[j], w[i]  
            break
    
    w = w[:i + 1] + w[i + 1:][::-1]
    print(f"Result: {''.join(w)}")
    print("".join(w))