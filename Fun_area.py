#Crea una función que reciba el radio de un círculo y retorne su área.
#Fórmula: Área = π * radio^2.
#Ejemplo: Entrada: 3 → Salida: 28.27 (aproximado).

pi = 3.14159 #Definimos el valor de pi

def area(radio): #Definimos la funcion area con el parámetro radio
    return pi * radio**2 #Retornamos la operación

print("Ingrese el radio para calcular el area del circulo: ") #Solicitamos ingresar el radio
radio = float(input()) #Guardamos en la variable
print("{:.2f} (aproximado)".format(area(radio))) #Imprimos el resultado con solo 2 decimales
