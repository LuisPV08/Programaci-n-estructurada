#Escribe un programa que solicite una contraseña y valide si es correcta (ejemplo: contraseña fija es 12345).
#Ejemplo: Entrada: 12345 → Salida: "Acceso concedido".

print("***Programa para validar si la contraseña ingresada es correcta***")
print("Ingrese la contraseña: ") #Solicitamos al usuario la contraseña
contraseña = int(input()) #Guardamos la contraseña en la variable
contraseña_valida = 12345 #Declaramos la contraseña válida

if contraseña == contraseña_valida: #Verificamos si la contraseña ingresada es válida
    print("Acceso concedido") #Imprimimos el resulado
else:
    print("Acceso denegado") #Caso contrario imprimir este resultado