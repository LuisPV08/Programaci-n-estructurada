#Imprime los números del 10 al 1 en orden descendente.
#Salida esperada: 10, 9, 8, ..., 1.

for i in range(10,0,-1): #Generamos un for con un rango del 10 al 0 y que vaya de forma descendente
    if i > 1: #Verificamos que el número sea mayor a 1
        print(i, end=", ") #Imprimios el resultado con ',' al final
    else: #Casi contrario
        print(i) #Imprimir el número
