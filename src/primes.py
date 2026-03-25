#!/usr/bin/python3
# Python program to display all the prime numbers within an interval

# Se establecen los límites inferior y superior del intervalo
lower = 1
upper = 500

# Se imprime un mensaje para el usuario
print("Prime numbers between", lower, "and", upper, "are:")

# Se itera a través de cada número en el intervalo definido por lower y upper
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
