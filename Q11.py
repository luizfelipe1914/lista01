#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

from math import sqrt

number = int(input("informe um número: "))
maior = 0
index = 1

while(index < (number // 2)):
    if(number % index == 0):
        i = 2
        cont = 0
        while(i < sqrt(index)):
            if(index % i == 0):
                cont = cont + 1
            i = i + 1
        if(cont == 0):
            if(maior < index):
                maior = index
    index = index + 1
print("O maior fator primo de %d é %d" %(number, maior))