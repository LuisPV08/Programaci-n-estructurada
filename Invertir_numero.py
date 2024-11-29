#Solicita un número entero y muestra su versión invertida.
#Ejemplo: Entrada: 1234 → Salida: 4321.

print("***Programa para invertir los numeros ingresados***")
print("Ingrese un número entero: ") #Solicitamos al usuario ingresar un numero entero
numero = int(input()) #Guardamos el numero en la variable

numero_invertido = int(str(numero)[::-1]) #Convertimos el numero en cadena y luego a entero para guardarlo en la variable numero_invertido

print(numero_invertido) #Imprimimos el resultado