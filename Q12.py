#!/usr/bin/env python3

index = 3
while(index < 1000000):
    i = 2
    cont = 0
    primo = 3
    while(i < (index ** (1/2))):
        if(index % i == 0):
            cont = cont + 1
        i = i + 1
    if(cont == 0):
        if(index == primo + 2):
            print("(%d, %d)" %(primo, index))
            primo = index

    index = index + 1