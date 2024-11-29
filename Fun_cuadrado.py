#Escribe una función que reciba un número y retorne su cuadrado.
#Ejemplo: Entrada: 5 → Salida: 25.

def cuadrado(numero): #Definimos al funcion cuadrado con el parámetro numero 
    return numero * numero #Retornamos la operación

print("Ingrese un número para ver si cuadrado: ") #Solicitamos ingresar un número
numero = int(input()) #Guardamos en la variable
print(cuadrado(numero)) #Imprimimos la funcion con su parámetro
