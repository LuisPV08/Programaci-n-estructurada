#Solicita un número al usuario y muestra su tabla de multiplicar del 1 al 10.
#Ejemplo: Entrada: 5 → Salida: 5 x 1 = 5, ..., 5 x 10 = 50.

print("***Programa para mostrar una tabla de multiplicar***")
print("Ingrese el número de la tabla que desea mostrar: ") #Solicitamos al usuario ingresar el número
numero = int(input()) #Guardamos la variable

for i in range(1,11): #Generamos un for con rango del 1 al 11
    resultado = i #Guardamos el valor de i de cada vuelta en la variable
    print(numero, "x", i, "=", numero * resultado) #Imprimimos el resultado generado por cada vuelta que da el for