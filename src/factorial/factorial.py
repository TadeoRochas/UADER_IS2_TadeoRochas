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

rango = sys.argv[1]

# Caso "-hasta"
if rango.startswith("-"):
    hasta = int(rango[1:])
    desde = 1
# Caso "desde-"
elif rango.endswith("-"):
    desde = int(rango[:-1])
    hasta = 60
# Caso normal "desde-hasta"
else:
    partes = rango.split("-")
    desde = int(partes[0])
    hasta = int(partes[1])
# Recorrer e imprimir factoriales
for num in range(desde, hasta + 1):
    print("Factorial", num, "! es", factorial(num))
