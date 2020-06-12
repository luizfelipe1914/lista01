#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

"""
	5)Receba uma lista de números inteiros positivos e imprima a média deles.
"""

index = 0 
number = 0
contador = 0
soma = 0
while(index < 1000000 and number >= 0):
	number = int(input("Informe um número natural: "))
	if(number >= 0):
		soma = soma + number
		contador = contador + 1
	index = index + 1
print("A média é %.2f" %(soma / contador))