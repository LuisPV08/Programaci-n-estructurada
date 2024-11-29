#Solicita un número entero y calcula la suma de sus dígitos.
#Ejemplo: Entrada: 123 → Salida: 6 (1 + 2 + 3).

print("***Programa para sumar todos los dígitos de un número***")
print("Ingrese una cifra: ") #Solicitamos al usuario una cifra de números
numero = int(input()) #Guardamos la variable ingrada
resultado = 0 #Inicializamos la variable resultado

for i in str(numero): #Generamos un for hasta la cantidad de numeros ingresados
    resultado += int(i) #Sumamos cada número y lo guardamos en la variable resultado

print(resultado) #Imprimos el resultado
