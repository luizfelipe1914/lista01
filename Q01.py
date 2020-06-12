#!/usr/bin/env python3

#-*- encoding: UTF-8 -*-

"""
1)Receba uma lista de números inteiros positivos e imprima o maior e o menor deles
"""
maior = 0
menor = maior
index = 0
number = 0

while(index <= 1000000 and number >= 0):
	number = int(input("Informe um número natural: "))
	if(number >= 0 and index == 0):
		maior = menor = number
	if(number > maior):
		maior = number
	elif( number >= 0 and number < menor):
		menor = number
	index = index + 1

print("O maior valor informado foi %d" %(maior))
print("O menor valor informado foi %d" %(menor))
