#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

class Factorial:

    def __init__(self):
        pass 

    def calcular(self, num):
        if num < 0:
            print("Factorial de un número negativo no existe")
            return 0
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact

    def run(self, minimo, maximo):
        for num in range(minimo, maximo + 1):
            print("Factorial", num, "! es", self.calcular(num))


# ---------------- Cuerpo Principal ----------------

if len(sys.argv) < 2:
    print("Debe informar un rango!")
    sys.exit()

rango = sys.argv[1]

if rango.startswith("-"):
    hasta = int(rango[1:])
    desde = 1

elif rango.endswith("-"):
    desde = int(rango[:-1])
    hasta = 60

else:
    partes = rango.split("-")
    desde = int(partes[0])
    hasta = int(partes[1])

# Crear objeto y ejecutar
f = Factorial()
f.run(desde, hasta)