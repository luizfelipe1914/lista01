#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

number = int(input("Informe um número natural: "))
index = 1

while(index < (number // 2)):
	if(number % index == 0):
		print("%d x %d = %d " %(index , (number / index), number))
	index = index + 1