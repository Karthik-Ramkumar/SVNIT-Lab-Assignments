def generate_magic_square(n):
    if n % 2 == 1:
        return odd_magic_square(n)
    elif n % 4 == 0:
        return doubly_even_magic_square(n)
    else:
        return singly_even_magic_square(n)

def odd_magic_square(n):
    square = [[0] * n for _ in range(n)]
    num = 1
    i, j = 0, n // 2
    while num <= n * n:
        square[i][j] = num
        num += 1
        new_i, new_j = (i - 1) % n, (j + 1) % n
        if square[new_i][new_j]:
            i += 1
        else:
            i, j = new_i, new_j
    return square

def doubly_even_magic_square(n):
    square = [[(n * i + j + 1) for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if (i % 4 == j % 4) or ((i + j) % 4 == 3):
                continue
            square[i][j] = n * n + 1 - square[i][j]
    return square

def singly_even_magic_square(n):
    half = n // 2
    sub_square = odd_magic_square(half)
    square = [[0] * n for _ in range(n)]
    add = [0, 2 * half * half, 3 * half * half, half * half]

    for i in range(half):
        for j in range(half):
            for k in range(4):
                r = i + (k // 2) * half
                c = j + (k % 2) * half
                square[r][c] = sub_square[i][j] + add[k]

    # Swap columns
    k = (n - 2) // 4
    for i in range(half):
        for j in range(n):
            if (j < k or j >= n - k) or (j == k and i == k):
                if j % n < half:
                    square[i][j], square[i + half][j] = square[i + half][j], square[i][j]
    return square

def print_magic_square(square):
    for row in square:
        print(' '.join(f'{x:2d}' for x in row))
    print()

for n in [4, 5, 6, 7, 8]:
    print(f'Magic Square of size {n}:\n')
    print_magic_square(generate_magic_square(n))
