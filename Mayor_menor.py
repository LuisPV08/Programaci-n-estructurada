#Escribe un programa que solicite un número y determine si es mayor o menor que 10.
#Ejemplo: Entrada: 5 → Salida: "Es menor que 10".

print("***Programa para calcular si número ingresado es mayor o menor que 10***")
print("Ingrese el número: ") #Pedimos al usuario ingresa el número
num = int(input()) #Guardamos el número en la variable

if num > 10: #Verificamos si es mayor que 10
    print("Es mayor que 10") #Imprimimos este texto en caso de ser mayor
elif num == 10: #Verificamos si es igual que 10
    print("Es igual que 10") #Imprimimos este texto en caso de ser igual
else:
    print("Es menor que 10") #Si no se cumplen las anteriores condiciones imprimimos por defecto que es menor
