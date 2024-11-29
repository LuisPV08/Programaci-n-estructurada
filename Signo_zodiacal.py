#Solicita el día y mes de nacimiento y determina el signo zodiacal del usuario.
#Ejemplo: Entrada: 22, marzo → Salida: "Tu signo es Aries".

print("***Programa para calcular su signo zodiacal***")
print("Ingrese su dia de nacimiento: ") #Solicitamos al usuario ingresar su dia de nacimiento
dia = int(input()) #Guardamos el dia en la variable
print("Ingrese su mes de nacimiento: ") #Solicitamos al usuario ingresar su mes de nacimiento 
mes = input().lower() #Guardamos la variable y la convertimos en minuscula

if (mes == "enero" and dia >= 20) or (mes == "febrero" and dia <= 18): #Verificamos el mes y dia ingresados
    print("Tu signo es Acuario") #Imprimimos el resultado
elif (mes == "febrero" and dia >= 19) or (mes == "marzo" and dia <= 20): #Verificamos el mes y dia ingresados
    print("Tu signo es Piscis") #Imprimimos el resultado
elif (mes == "marzo" and dia >= 21) or (mes == "abril" and dia <= 19): #Verificamos el mes y dia ingresados
    print("Tu signo es Aries") #Imprimimos el resultado
elif (mes == "abril" and dia >= 20) or (mes == "mayo" and dia <= 20): #Verificamos el mes y dia ingresados
    print("Tu signo es Tauro") #Este será el resultado
elif (mes == "mayo" and dia >= 21) or (mes == "junio" and dia <= 20): #Verificamos el mes y dia ingresados
    print("Tu signo es Géminis") #Imprimimos el resultado
elif (mes == "junio" and dia >= 21) or (mes == "julio" and dia <= 22): #Verificamos el mes y dia ingresados
    print("Tu signo es Cáncer") #Imprimimos el resultado
elif (mes == "julio" and dia >= 23) or (mes == "agosto" and dia <= 22): #Verificamos el mes y dia ingresados
    print("Tu signo es Leo") #Imprimimos el resultado
elif (mes == "agosto" and dia >= 23) or (mes == "septiembre" and dia <= 22): #Verificamos el mes y dia ingresados
    print("Tu signo es Virgo") #Imprimimos el resultado
elif (mes == "septiembre" and dia >= 23) or (mes == "octubre" and dia <= 22): #Verificamos el mes y dia ingresados
    print("Tu signo es Libra") #Imprimimos el resultado
elif (mes == "octubre" and dia >= 23) or (mes == "noviembre" and dia <= 21): #Verificamos el mes y dia ingresados
    print("Tu signo es Escorpio") #Imprimimos el resultado
elif (mes == "noviembre" and dia >= 22) or (mes == "diciembre" and dia <= 21): #Verificamos el mes y dia ingresados
    print("Tu signo es Sagitario") #Imprimimos el resultado
elif (mes == "diciembre" and dia >= 22) or (mes == "enero" and dia <= 19): #Verificamos el mes y dia ingresados
    print("Tu signo es Capricornio") #Imprimimos el resultado
