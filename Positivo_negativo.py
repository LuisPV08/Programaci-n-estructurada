#Solicita al usuario un número y determina si es positivo, negativo o cero.
#Ejemplo: Entrada: -3 → Salida: "Es un número negativo".

print("***Programa para verificar si un número es postivo, negativo o cero***")
print("Ingrese un número: ") #Pedimos al usuario que ingrese un número
num = int(input()) #Guardamos el número ingresado en la variable

if num > 0: #Verificamos si es positivo
    print("Es un número positivo") #Imprimimos el resultado
elif num == 0: #Verificamos si es igual a cero
    print("Es cero") #Imprimimos el resultado
else: 
    print("Es un número negativo") #Si no se cumplen las anteriores condiciones se imprimirá que es negativo