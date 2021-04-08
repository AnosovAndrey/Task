#!/usr/bin/env python3

import math
import csv
import random

# Массу от 0 до 4. Длину по х,у до 10, по z до 5

def calc(x1, x2, y1, y2, z1, z2, weight, x, y):
    z = 0
    G = 6.67191
    r1 = math.sqrt((x1-x)*(x1-x) + (y1-y)*(y1-y) + (z1-z)*(z1-z))
    r2 = math.sqrt((x2-x)*(x2-x) + (y2-y)*(y2-y) + (z2-z)*(z2-z))
    r1r2 = (x1-x)*(x2-x) + (y1-y)*(y2-y) + (z1-z)*(z2-z)
    return ((z1-z)/r1 + (z2-z)/r2)*(G*weight/(r1*r2+r1r2))


weight = random.uniform(0, 4)

x1 = random.uniform(0, 40)
temp = random.uniform(1, 10)
x2 = (x1 + temp) if ((x1 + temp) < 40) else (x1 - temp)

y1 = random.uniform(0, 40)
temp = random.uniform(1, 10)
y2 = (y1 + temp) if ((y1 + temp) < 40) else (y1 - temp)

z1 = -random.uniform(0, 5)
z2 = z1 - random.uniform(1, 5)

with open("otrezok.csv", mode="a", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
    file_writer.writerow(["x1", "x2", "y1", "y2", "z1", "z2", "weight"])
    file_writer.writerow([x1, x2, y1, y2, z1, z2, weight])


dimension = 40
step = 1
h=round(dimension/step)

with open("data.csv", mode="a", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
    file_writer.writerow(["x", "y", "component"])
    for x in range(0, h):
      for y in range(0, h):
        #print(x*step, y*step, calc(x1, x2, y1, y2, z1, z2, weight, x*step, y*step))
        file_writer.writerow([x*step, y*step, calc(x1, x2, y1, y2, z1, z2, weight, x*step, y*step)])

print("done")


