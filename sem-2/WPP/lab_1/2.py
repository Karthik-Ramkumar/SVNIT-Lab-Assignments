import random
nums = []
for i in range(101):
    nums.append(random.randint(0,1))

count = 0
streak = 0
for num in nums:
    if num == 0:
        count += 1
        streak = max(streak, count)
    else:
        count = 0

print("Longest streak of 0:",streak)