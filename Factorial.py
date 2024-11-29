#Calcula el factorial de un número ingresado por el usuario (n!).
#Ejemplo: Entrada: 5 → Salida: 120.

print("***Programa para mostrar el factorial de un número***")
print("Ingrese un número para ver su factorial: ") #Solicitamos al usuario un número
num = int(input()) #Guardamos el numero en la variable
resultado = 1 #Inicializamos la variable resultado
for i in range(1,num+1): #Generamos un for con rango del 1 hasta el numero agregado + 1
    resultado *= i #Guardamos el resultado de la multiplicación de cada vuelta del bucle en resultado
    
print(resultado) #Imprimimos el resultado
