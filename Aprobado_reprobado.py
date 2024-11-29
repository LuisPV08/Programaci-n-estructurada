#Solicita la calificación de un estudiante y determina si está aprobado (mayor o igual a 7) o reprobado.
#Ejemplo: Entrada: 6.5 → Salida: "Reprobado".

print("***Programa para verificar si un estudinte aprueba o no***")
print("Ingrese su calificación: ") #Pedimos al usuario que ingrese su calificación
calif = float(input()) #Guardamos el número ingresado en la variable

if calif >= 7: #Verificamos si es mayor o igual a 7
    print("Aprobado") #Imprimimos el resultado
else:
    print("Reprobado") #Caso contrario imprimir este resultado