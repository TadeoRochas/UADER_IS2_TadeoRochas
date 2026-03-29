import matplotlib.pyplot as plt

def collatz_iteraciones(n):
    contador = 0

    while n != 1:
        if n % 2 == 0: #Comprueba si es par
            n = n // 2
        else: #si es impar
            n = 3 * n + 1
        contador += 1

    return contador


numeros = []
iteraciones = []

# Calcular para 1 a 10000
for i in range(1, 10001):
    pasos = collatz_iteraciones(i)
    numeros.append(i)
    iteraciones.append(pasos)

# Graficar
plt.scatter(iteraciones, numeros, s=1)  # s=1 para puntos chiquitos
plt.xlabel("Iteraciones")
plt.ylabel("Número inicial (n)")
plt.title("Conjetura de Collatz")

plt.show()