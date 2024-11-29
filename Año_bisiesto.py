#Solicita un año y determina si es bisiesto (divisible entre 4 pero no entre 100,
#excepto si es divisible entre 400).
#Ejemplo: Entrada: 2024 → Salida: "Es bisiesto".

print("***Programa para determinar si el año es bisiesto***")
print("Ingrese el año:") #Solicitamos que ingrese el año
año = int(input()) #Guardamos el año en la variable

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0): #Verificamos si el año ingresado cumple con la condición
    print("Es bisiesto") #Imprimir el resultado
else:
    print("No es bisiesto") #Caso contrario imprimir este resultado