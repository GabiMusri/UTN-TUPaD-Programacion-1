#EJERCICIO 4
#Escape Room: La Bóveda
print("Bienvenido, jugador/a")
print("Sos un agente que intenta abrir una bóveda con 3 cerraduras. \nTenés energía y tiempo limitados. \nSi abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás. ")
#Inicializar variables
energia = 100 
tiempo = 12 
cerraduras_abiertas = 0 
alarma = False 
codigo_parcial = ""
racha_forzar = 1
opcion = "0"
#Ingresar nombre del jugador y validar datos.
nombre_player = input("Por favor ingrese su nombre usando solo letras: ").strip()
while not nombre_player.isalpha():
    print("Error, debe ingresar solo letras. ")
    nombre_player = input("Por favor ingrese su nombre usando solo letras: ").strip()

#Establecer condición de juego.

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:
    print("Estadísticas")
    print(f"-Energía: {energia}, -Tiempo: {tiempo}, - Cerraduras abiertas: {cerraduras_abiertas}")
    print("Por favor, elija una opción: ")
    print("-OPCIONES- \n1. Forzar cerradura (costo: -20 energía, -2 tiempo) \n2. Hackear panel (costo: -10 energía, -3 tiempo) \n3. Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 de energía extra)")
    if energia < 40:
        print("Riesgo de alarma")
    elif opcion == "3" and energia < 40:
        alarma = True
    elif racha_forzar >= 3:
        alarma = True
    opcion = input(" - ")
    if opcion == "1":
        energia -= 20
        tiempo -= 2
        racha_forzar += 1
        cerraduras_abiertas += 1
    elif opcion == "2":
        energia -= 10
        tiempo -= 3
        racha_forzar = 0
        for i in range(4):
            print(f"Paso: {i+1}")
            codigo_parcial += "A"
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
    elif opcion == "3":
        if energia < 100:
            energia += 15
            tiempo -= 2
            racha_forzar = 0
        elif energia >= 100:
            print("Alcanzaste el máximo de energía.")

if (energia <= 0 or tiempo <= 0 or cerraduras_abiertas < 3) or alarma == True:
    print("HAS SIDO DERROTADO")
elif cerraduras_abiertas == 3 and alarma == False:
    print("VICTORIA, HAS GANADO")
elif alarma == True:
    print("HAS SIDO DERROTADO")
