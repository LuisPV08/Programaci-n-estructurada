#Solicita una calificación numérica y devuelve la letra correspondiente:
#90-100: A.
#80-89: B.
#70-79: C.
#60-69: D.
#Menor a 60: F.
#Ejemplo: Entrada: 85 → Salida: "Tu calificación es B".

print("***Programa para puntuar tu calificación***")
print("Ingrese su nota (0-100):") #Solicitamos al usuario ingresar su nota
nota = int(input()) #Guardamos la nota en la variable

if nota >= 0 and nota < 60: #Verificamos la nota
    print("Tu calificación es F") #Imprimimos el resultado
elif nota >= 60 and nota < 70: #Verificamos la nota
    print("Tu calificación es D") #Imprimimos el resultado
elif nota >= 70 and nota < 80: #Verificamos la nota
    print("Tu calificación es C") #Imprimimos el resultado
elif nota >= 80 and nota < 90: #Verificamos la nota
    print("Tu calificación es B") #Imprimimos el resultado
elif nota >= 90 and nota <= 100: #Verificamos la nota
    print("Tu calificación es A") #Imprimimos el resultado
else:
    print("Ingrese una calificación válida") #Caso contrario imprimir esto
