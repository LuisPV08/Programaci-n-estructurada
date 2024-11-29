#Solicita tres números y determina cuál es el mayor.
#Ejemplo: Entrada: 4, 9, 2 → Salida: "El número mayor es 9".

print("***Programa para verificar el número mayor entre 3***")
print("Ingrese el primer número: ") #Solicitamos el ingreso del primer número
a = int(input()) #Guardamos la variable ingresada
print("Ingrese el segundo número: ") #Solicitamos el ingreso del segundo número
b = int(input()) #Guardamos la variable ingresada
print("Ingrese el tercer número: ") #Solicitamos el ingreso del tercer número
c = int(input()) #Guardamos la variable ingresada

if a > b and a > c: #Verificamos si el primer valor es el mayor
    print("El número mayor es", a) #Imprimimos el resultado
elif b > a and b > c: #Verificamos si el segundo valor es el mayor
    print("El número mayor es", b) #Imprimimos el resultado
elif c > a and c > b: #Verificamos si el tercer valor es el mayor
    print("El número mayor es", c) #Imprimimos el resultado
else: #En caso de que no se cumplan las condiciones anteriores
    print("El valor mayor se repite 2 o mas veces") #Imprimimos el resultado