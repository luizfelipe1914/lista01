#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

a1 = int(input("Informe A1: "))
r = int(input("Informe a razão: "))
n = int(input("Informe a quantidade de termos que deseja calcular: "))
index = 0

while(index < n):
    print("A%d = %d" %((index + 1) , (a1 + index * r)))
    index = index + 1
