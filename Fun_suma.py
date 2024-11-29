#Escribe una función que reciba dos números como parámetros y retorne su suma.
#Ejemplo: Entrada: 3, 7 → Salida: 10.

def suma(a,b): #Definimos la funcion suma que tomará los parámetros a y b
    return print(a + b) #Retornamos la operación

print("Ingrese el primer número: ") #Solicitamos ingresar el primer numero
a = int(input()) #Guardamos el numero en la variable
print("Ingrese el segundo número: ") #Solicitamos ingresar el segundo numero
b = int(input()) #Guardamos en la variable
suma(a,b) #Llamamos a la funcion asignando sus parámetros
