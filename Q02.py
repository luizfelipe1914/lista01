#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

"""

	2)Receba uma lista de números inteiros positivos e imprima o produto dos números ímpares e a soma dos números pares.

"""

index = 0
soma = 0
produto = 1
number = 0

while(index <= 1000000 and number >= 0):
	number = int(input("Informe um número natural: "))
	if(number % 2 == 0):
		soma = soma + number
	else:
		if(number > 0):
			produto = produto * number
	index = index + 1

print("Soma dos pares = %d" %(soma))
print("Produto dos pares = %d " %(produto))