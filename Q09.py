#!/usr/bin/env python3
#-*-encoding: UTF-8 -*-

print("C°| F°")
print("---------------------")
for var in range(0, 101):
    fahrenheit = (var * (9/5)) + 32
    print("%d° C° | %.2f° F°" %(var, fahrenheit))
    print("---------------------")