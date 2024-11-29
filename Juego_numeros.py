#Genera un número aleatorio entre 1 y 10 y solicita al usuario que adivine el número.
#Usa if para verificar si acertó o no.
#Ejemplo: Entrada: 5 → Salida: "¡Felicidades, acertaste!" o "Intenta de nuevo.".

import random #Importamos la librería random

print("***Programa para adivinar un número aleatorio***")
print("Ingrese un número del 1-10: ") #Solicitamos al usuario ingresar un numero de l-10
num = int(input()) #Guardamos el numero en la variable
num_random = random.randint(1, 10) #Generamos un número aleatorio en otra variable

if num == num_random: #Verificamos si ambos números son iguales
    print("¡Felicidades, acertaste!") #Imprimimos el resultado
else:
    print("Intenta de nuevo") #Caso contrario imprimir el resultado