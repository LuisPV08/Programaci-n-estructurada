#Imprime todos los números pares entre 1 y 20.
#Salida esperada: 2, 4, 6, ..., 20.

print("***Programa para imprimir los numero pares entre el 1 y 20***")

for i in range(1,21): #Generamos un for con rango del 1 al 21
    if i % 2 == 0: #Verificamos que el número sea divisible para 2
        if i < 20: #Verificamos que sea menor a 20
            print(i, end=", ") #Imprimos el número con ',' al final
        else: #Caso contrario
            print(i) #Imprimimos el número
