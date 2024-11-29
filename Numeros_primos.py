#Encuentra e imprime todos los números primos entre 1 y 50.
#Salida esperada: 2, 3, 5, 7, ..., 47.

print("***Programa para mostrar los numeros primos entre el 1 y 50***")
for numero in range(2, 51): #Generamos un for con rango del 2 al 51
    es_primo = True #Asumimos que todos los valores son verdaderos
    

    for divisor in range(2, numero): #Generamos un for con rango desde el 2 hasta numero
        if numero % divisor == 0: #Verificamos si es divisible por cualquier número
            es_primo = False #El numero no es primo
            break #Rompremos el bucle 
    
    if es_primo: #Si la variable es_primo es True
        if numero < 47: #Si los numeros son menores a 47
            print(numero, end=", ") #Imprimir el resultado con con una ',' al final
        else: #Caso contrario
            print(numero) #Imprimos el número