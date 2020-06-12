#!/usr/bin/env/python3
#-*- encoding: UTF-8 -*-

number = int(input("Informe um número natural: "))
index = 3

while(index < number):
	if(number == (index -1) * (index - 2) * (index - 3)):
		print("É triangular!")
		break
	index = index + 1