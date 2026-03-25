#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

# Se verifica que se haya informado un número como argumento al programa
if len(sys.argv) < 2:
   print("Debe informar un número!")
   sys.exit()

# Se separa el argumento usando el guion '-'
rango = sys.argv[1].split("-")

desde = int(rango[0])
hasta = int(rango[1])

# Se recorre el rango desde el valor de "desde" hasta el valor de "hasta" y se imprime el factorial de cada número en ese rango
for num in range(desde, hasta + 1):
    print("Factorial ",num,"! es ", factorial(num)) 

