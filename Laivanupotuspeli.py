import random

print("Laivanupotuspeli 1.0")

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

for row in number_grid:
    print(row)

a = random.randint(0,2)

laivan_x = a
laivan_y = a
laiva = number_grid[laivan_x][laivan_y]
upotus = False

def uppoaminen():
    print("Osuit ja laiva upposi")

def hutiosuma():
    print("Ammuit ohi")

while not(upotus):
    x = int(input("Anna koordinaatti x: "))
    y = int(input("Anna koordinaatti y: "))


    if x == laivan_x and y == laivan_y:
        uppoaminen()
        upotus = True
    else:
        hutiosuma()

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(number_grid[x][y])