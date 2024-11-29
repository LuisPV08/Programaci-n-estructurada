#Solicita una edad y clasifica al usuario como niño (0-12), adolescente (13-17) o adulto (18+).
#Ejemplo: Entrada: 15 → Salida: "Eres adolescente".

print("***Programa para clasificar usuario por edad***")
print("Ingrese su edad: ") #Solicitamos al usuario ingresar su edad
edad = int(input()) #Guardamos la edad en la variable

if edad >= 0 and edad <= 12: #Verificamos si está dentro del rango de 0-12
    print("Eres un niño") #Imprimimos el resultado
elif edad > 12 and edad < 18: #Verificamos si está dentro del rango de 13-17
    print("Eres adolecente") #Imprimimos el resultado
elif edad > 18: #Verificamos si es mayor a 18
    print("Eres adulto") #Imprimimos el resultado
else:
    print("Ingrese una edad válida") #Caso contrario imprimir este resultado