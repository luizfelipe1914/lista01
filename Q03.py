#!/usr/bin/env python3
#-*- encoding: UTF- 8 -*-

"""
3)Receba um inteiro ncomo entrada e imprima os nnúmeros de Fibonacci. 
Lembre-se que uma série de Fibonacci tem o padrão:1   1  2 3  5  8  13  21  34  55  89 ...
"""

number = int(input("Informe um número natural: "))
index = 0
ant = 0
prox = 0
while(index <= number):
	prox = ant + prox
	ant = prox - ant
	if(prox == 0):
		prox = prox + 1
	print("Fibonacci[%d] = %d" %(index, prox))
	index = index + 1