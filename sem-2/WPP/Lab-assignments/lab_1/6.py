import math

coords = []
for i in range(3):
    coords.append(input("Enter X-Y-Z separated by - "))  
nearest_neighbors = []

for coord in coords:
    X, Y, Z = map(int, coord.split("-"))
    shortest = float('inf')
    nearest = None

    for coord1 in coords:
        if coord1 == coord:
            continue 

        X1, Y1, Z1 = map(int, coord1.split("-"))
        short = math.sqrt((X - X1) ** 2 + (Y - Y1) ** 2 + (Z - Z1) ** 2)

        if short < shortest:
            shortest = short
            nearest = coord1

    nearest_neighbors.append((coord, nearest))

print(nearest_neighbors)