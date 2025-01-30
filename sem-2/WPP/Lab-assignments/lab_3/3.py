t = int(input())

for _ in range(t):
    n = int(input())
    height = 1

    for cycle in range(n):
        if cycle % 2 == 0:
            height *= 2  
        else:
            height += 1  

    print(height)
