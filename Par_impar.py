#Solicita un número al usuario y determina si es par o impar.
#Ejemplo: Entrada: 4 → Salida: "Es par".

print("***Programa para verificar si un número es par o impar***")
print("Ingrese un número: ") #Pedimos al usuario que ingrese un número
num = int(input()) #Guardamos el número ingresado en la variable

if num % 2: #Verificamos si el número es impar
    print("Es impar") #Imprimimos el resultado
else:
    print("Es par") #Imprimimos este resultado en caso contrario