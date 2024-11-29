#Solicita calificaciones al usuario (hasta que ingrese -1) y calcula el promedio.
#Ejemplo: Entradas: 5, 7, 8, -1 → Salida: Promedio: 6.67.

suma_calif = 0 #Inicializamos la variable suma_calif
cant_calif = 0 #Inicializamos la variable cant_calif

while True: #Entramos al bucle hasta cumplir la condición que lo rompa
    print("Ingrese su calificación (ingrese -1 para terminar): ") #Solicitamos al usuario ingresar su calificación
    calificación = int(input()) #Guardamos la variable 
    if calificación == -1: #Verificamos si calificación es -1
        break #Rompemos el bucle
    
    if calificación >= 0: #Verificamos si calificación es mayor o igual a 0
        suma_calif += calificación #Sumamos las calificaciones y las guardamos en la variable suma_calif
        cant_calif += 1 #Aumentamos el contador de la cantidad de calificaciones con cada vuelta
    
promedio = suma_calif / cant_calif #Creamos la operación del promedio
print(f"Promedio: {promedio:.2f}") #Imprimos el resultado
