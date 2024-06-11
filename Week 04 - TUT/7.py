import random

count = 0
double = 0
first = 0
second = 0

for i in range(100):
    first = random.randint(1,6)
    second = random.randint(1,6)

    if first == second:
        double = double + 1

print("Out of 100 you rolled",double,"doubles")
