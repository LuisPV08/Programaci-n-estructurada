#Solicita dos números y una operación (+, -, *, /) y realiza el cálculo correspondiente.
#Ejemplo: Entrada: 3, 2, '+' → Salida: "Resultado: 5".

print("***Programa para hacer operaciones matemáticas básicas***")
print("Ingrese el primer número: ") #Solicitamos que ingrese el primer número
a = int(input()) #Guardamos el número en la variable
print("Ingrese el segundo número: ") #Solicitamos que ingrese el segundo número
b = int(input()) #Guardamos el número en la variable
print("Que operación desea realizar (+,-,*,/)") #Solicitamos la operación a realizar
op = input() #Guardamos en la varible

if op == '+': #Verificamos si la operacion es una suma
    print("Resultado:", a + b) #Imprimimos el resultado
elif op == '-': #Verificamos si la operacion es una resta
    print("Resultado:", a - b) #Imprimimos el resultado
elif op == '*': #Verificamos si la operacion es una multiplicación
    print("Resultado:", a * b) #Imprimimos el resultado
elif op == '/': #Verificamos si la operacion es una división
    print("Resultado:", a / b) #Imprimimos el resultado
else:
    print("Ingrese una operación válida") #Caso contrario imprimir este resultado