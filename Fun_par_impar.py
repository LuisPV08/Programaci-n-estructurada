#Crea una función que reciba un número y retorne True si es par y False si es impar.
#Ejemplo: Entrada: 4 → Salida: True.

def par_impar(numero): #Definimos la función par_impar con el parámetro numero
    if numero % 2 == 0: #Verificamos si el resto del numero ingresado es 0
        return True #Retorna True
    else: #Caso contrario
        return False #Retorna False
    
print("Ingrese un número: ") #Solicitamos ingresar un numero
numero = int(input()) #Guardamos la variable
print(par_impar(numero)) #Imprimimos la funcion con el parámetro asignado
