import math

# 1


def degreeToRadian():
    degree = int(input('Please enter the degree you want to change: '))
    print(degree * (math.pi / 180))


degreeToRadian()


# 2
def trapezoidArea(height, base1, base2):
    return 1 / 2 * (base1 + base2) * height


Height = int(input('Height: '))
Base1 = int(input('Base1: '))
Base2 = int(input('Base2: '))
print(trapezoidArea(Height, Base1, Base2))

# 3


def polygonArea(numberOfSides, length):
    return numberOfSides * pow(length, 2) / (4 * math.tan(math.pi / numberOfSides))


num_of_sides = int(input('Number of sides: '))
length = int(input('Length of side: '))
print(f"{polygonArea(num_of_sides, length):.0f}")


# 4
def parallelogramArea(base, height):
    return base * height


Base = int(input('Base: '))
Height = int(input('Height: '))
print(f"{parallelogramArea(Base, Height):.1f}")
