#EJERCICIO 2: “ACCESO AL CAMPUS Y MENÚ SEGURO"
#Login con intentos + menú de acciones con validación estricta.
print("Bienvenid@")
usuario_correcto = "alumno"
contrasena_correcta = "python123"
intentos_permitidos = 3
cant_intentos = 1

print(f"Intento {cant_intentos} / 3")
nombre_usuario = input("Ingrese su nombre de usuario: ")
contrasena = input("Ingrese su contraseña: ")

while cant_intentos < intentos_permitidos and (nombre_usuario != usuario_correcto and contrasena != contrasena_correcta):
    cant_intentos += 1
    print(f"Intento {cant_intentos} / 3")
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
if cant_intentos < intentos_permitidos and (nombre_usuario == usuario_correcto and contrasena == contrasena_correcta):
    print("Elija una opción usando los números del 1 al 4: \n 1. Ver estado de inscripción. \n 2. Cambiar clave \n 3. Mostrar mensaje motivacional. \n 4. Salir ")
    opcion = input( )
    if opcion.isdigit() and (opcion == "1" or opcion == "2" or opcion == "3" or opcion == "4"): 
        if opcion == "1":
            print ("Estado de la inscripción: Inscripto.")
        elif opcion == "2": 
            nueva_clave = input("Ingrese su nueva clave de mayor a 6 dígitos: ")
            confirmacion = input("Confirme su nueva clave: ")
            i = len(nueva_clave)
            if nueva_clave == confirmacion and (i >= 6):
                print("Clave cambiada con éxito.")
            elif nueva_clave != confirmacion or (i < 6):
                print("Las claves no coinciden o no tienen el largo necesario.")
        elif opcion == "3": 
            print("Solo falla quien se da por vencido. ¡Sigue adelante!")
        elif opcion == "4": 
            print("Adios")
    else: 
        print("Ingrese un dígito valido.")
else:
    print("¡Cuenta bloqueada!")
    