import math

number1 = int(input("Please enter number of balls: "))

count = 1
volume = 0

for i in range(0, number1, count):
    count = count + i + 1
    base = count - 1
    volume = volume + base
    print(base)
print("Volume of pyramid:", volume)

baseL = 0
