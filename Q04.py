#!/usr/bin/env python3
#-*- encoding: UTF- 8 -*-

"""
	4)Imprima o quinto número maior do 100 que é divisível por 3 e por 7 ao mesmo tempo.
"""

contador = 0
index = 100
number = 0

while(contador < 5):
	if(index % 3 == 0):
		if(index % 7 == 0):
			number = index
			contador = contador + 1
	index = index + 1
print(number)