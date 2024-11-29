#Una tienda ofrece un 20% de descuento si el cliente gasta más de $100. 
#Escribe un programa que calcule el monto final.
# #Ejemplo: Entrada: $120 → Salida: "Monto final: $96".

print("***Programa para verificar si el cliente tendrá un descuento del 20%***")
print("Ingrese el valor: ") #Pedimos al usuario que ingrese el valor
compra = int(input()) #Guardamos el valor ingresado en la variable
monto_final = float() #Inicializamos la variable que usaremos para mostrar el valos final

if compra > 100: #Verificamos que la compra sea mayor a 100
    monto_final = compra - (compra * 0.20) #Aplicará la fórmula a la compra

print(f"Monto final: ${monto_final}") #Mostramos el resultado