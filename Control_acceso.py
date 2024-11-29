#Solicita un nombre de usuario y contraseña, y valida si ambos son correctos. Permite tres intentos antes de bloquear el acceso.
#Ejemplo: Entrada: Usuario: admin, Contraseña: 1234 → Salida: "Bienvenido, admin.".

print("***Programa para validar usuario y contraseña***")
usuario = "" #Incializamos la variable usuario
contraseña = "" #Inicializamos la variable contraseña
usuario_valido = "admin" #Asiganmos el valor del usuario valido
contraseña_valida = "1234" #Asignamos el valor de la contraseña valida
intentos = int(3) #Inicializamos los intentos permitidos por el usuario

while True: #Utilizamos el bucle while true para validar la información
    print("Ingrese su usuario: ") #Solicitamos al usuario ingresar el usuario
    usuario = input() #Guardamos el usuario en la variable
    print("Ingrese su contraseña: ") #Solicitamos al usuario ingresar la contraseña
    contraseña = input() #Guardamos la contraseña en la variable
    if usuario == usuario_valido and contraseña == contraseña_valida: #Verificamos si el usuario y contraseña son correctos
        print("Bienvenido, admin") #Imprmimos el resultado
        break #Rompemos el bucle
    else: #Caso contrario
        print("Usuario o contraseña inválido") #Imprimimos el mensaje 
        print(f"Quedan {intentos} intentos") #Mostramos los intentos restantes
        intentos -= 1 #Restamos la cantidad de intentos en cada ingreso equivocado
        if intentos == -1: #Verificamos si los intentos llegan a ser -1
            print("Acceso bloqueado") #Imprimimos el resultado
            break #Rompemos el bucle
