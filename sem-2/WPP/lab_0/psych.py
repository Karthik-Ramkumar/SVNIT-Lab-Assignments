'''
# try 1
num = int(input("Enter number of people to swap: "))
order = input("Enter height order: ")
order_store = list(map(int, order.split(" ")))
print(order_store)
count = 0
for i in range(num-1):
    j = i+1
    if order_store[i] > order_store[j]:
        temp = order_store[i]
        order_store[i] = order_store[j]
        order_store[j] = temp
        numberOfSwap = numberOfSwap + 1
print(numberOfSwap)
print(order_store)
# try 2

 num = int(input("Enter number of people to swap: "))
order = input("Enter height order: ")
order_store = list(map(int, order.split()))

numberOfSwap = 0
for i in range(num):
    while order_store[i] != i + 1:
        temp = order_store[i]
        order_store[i] = order_store[temp - 1]
        order_store[temp - 1] = temp
        numberOfSwap += 1

print(numberOfSwap)
print(order_store)'''

num_of_elements = int(input("Enter the number of elements needed in the array: "))
array = []
count = 0

print("Enter the elements into the array:")
for i in range(num_of_elements):
    inp = int(input("Enter the number into the array:->"))
    array.append(inp)

print(array)

for i in range(num_of_elements):
    min_index = i
    for j in range(i + 1, num_of_elements):
        if array[j] < array[min_index]:
            min_index = j
    if min_index != i:
        array[i], array[min_index] = array[min_index], array[i]
        count += 1

print("The number of times the swap occurs:", count)
print(array)