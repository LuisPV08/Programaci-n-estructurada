#Crea una función que reciba un nombre como parámetro y retorne un saludo.
#Ejemplo: Entrada: María → Salida: "Hola, María!".

def saludo(nombre): #Creamos la funcion que tomará el parámetro nombre
    print(f"Hola, {nombre}!") #Se imprimirá el resultado

print("Ingrese su nombre: ") #Solicitamos ingresar el nombre
nombre = input() #Guardamos el nombre en la variable
saludo(nombre) #Llamamos a la funcion a ejecutarse
