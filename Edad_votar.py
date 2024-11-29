#Solicita la edad del usuario y determina si es elegible para votar (mayor o igual a 18 años).
#Ejemplo: Entrada: 17 → Salida: "No puedes votar".

print("***Programa para verificar si serás elegido para votar***")
print("Ingrese su edad: ") #Pedimos al usuario que ingrese su edad
edad = int(input()) #Guardamos la edad ingresado en la variable

if edad >= 18: #Verificamos si la edad es mayor o igual a 18
    print("Puedes votar") #Imprimimos el resultado
else:
    print("No puedes votar") #Caso contrario imprimir este resultado