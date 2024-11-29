#Calcula y muestra la suma de los números del 1 al 10.
#Salida esperada: 55.

print("***Programa para imprimir la suma de los numeros del 1 al 10***")
suma = 0 #Inicializamos la variable suma

for i in range(1,11): #Generamos un for con un rango del 1 al 11
    suma += i #Sumamos los valores de cada vuelta y las almacenamos en la variable suma

print(suma) #Imprimimos el resultado