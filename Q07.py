#!/usr/bin/env python3
#-*- encoding: UTF- 8 -*-

number = int(input("Informe um número natural: "))
index = 2
contador = 0

while(index <= (number ** (1/2))):
	if(number % index == 0):
		contador = contador + 1
	index = index + 1
if(contador == 0):
	print("O número informado é primo.")
else:
	print("O número informado não é primo.")