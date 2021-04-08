#!/usr/bin/env python3

import math
import csv

# Массу от 0 до 4. Длину по х,у до 10, по z до 5

def calc(x, y):
    x1 = 2
    y1 = 2
    z1 = -2
    x2 = 3
    y2 = 3
    z2 = -3
    z = 0
    weight = 1
    G = 398600.448
    r1 = math.sqrt((x1-x)*(x1-x) + (y1-y)*(y1-y) + (z1-z)*(z1-z))
    r2 = math.sqrt((x2-x)*(x2-x) + (y2-y)*(y2-y) + (z2-z)*(z2-z))
    r1r2 = (x1-x)*(x2-x) + (y1-y)*(y2-y) + (z1-z)*(z2-z)
    return ((z1-z)/r1 + (z2-z)/r2)*(G*weight/(r1*r2+r1r2))

dimension = 40
step = 1
h=round(dimension/step)

with open("data.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
    file_writer.writerow(["x", "y", "component"])
    for x in range(0, h):
      for y in range(0, h):
        print(x*step, y*step, calc(x*step, y*step))
        file_writer.writerow([x*step, y*step, calc(x*step, y*step)])


