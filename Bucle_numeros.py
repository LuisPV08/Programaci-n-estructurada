#Usa un bucle para mostrar los números del 1 al 10 en la consola.
#Salida esperada: 1, 2, 3, ..., 10.

print("***Programa para imprimir números del 1 al 10***")

for i in range(1,11): #Generamos un for con un rango del 1 al 11 para imprimir hasta el 10
    if i < 10: #Verificamos que el numero impreso sea menor que 10
        print(i, end=", ") #Imprimirá el resultado con una ',' al final
    else: #Caso contrario
        print(i) #Imprimir el número
