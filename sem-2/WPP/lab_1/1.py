# 1 a
nums = []
for i in range(50):
    nums.append(i)

print(nums)

# 1 b
square = []
for i in range(51):
    square.append(int(i*i))

print(square)

#1 c
letter = []
count = 1
ch = ord("a")
while count < 27:
    letter.append(chr(ch)*count)
    count += 1
    ch += 1

print(letter)