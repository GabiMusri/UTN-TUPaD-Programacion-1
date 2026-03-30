#EJERCICIO 5: La Arena del Gladadior.
#Inicializar variables del juego

Vida_Gladiador = 100
Vida_Enemigo = 100
Pociones_de_Vida = 3
Daño_base_Ataque_Pesado = 15
Daño_base_del_enemigo = 12
Turno_Gladiador = True

#Ingresar nombre de jugador y validar datos.

nombre = input("Bienvenid@, Por favor ingresar tu nombre solamente usando letras y sin espacios: ").strip().capitalize()
while not nombre.isalpha():
    print("Error, debes ingresar solo letras: ")
    nombre = input("Bienvenid@, Por favor ingresar tu nombre solamente usando letras y sin espacios: ").strip().capitalize()

print("Bienvenid@,",nombre)
print("Las reglas son las siguientes: \nEl objetivo es derrotar a tu oponente, el primero que se quede sin vida, pierde.")
print(f"Tus estadísticas son: \nVida de {nombre}: {Vida_Gladiador} \nVida del enemigo: {Vida_Enemigo} \nPociones de Vida: {Pociones_de_Vida} ")

#Ingresar opciones y validar datos.

while Vida_Gladiador > 0 and Vida_Enemigo > 0:
    opcion = input("¿Qué deseas hacer? (Elige una opcíon 1, 2, o 3) \n1. Ataque Pesado \n2. Ráfaga Veloz \n3. Curar \n--- ")
    while not opcion.isdigit() and not (opcion == "1" or opcion == "3" or opcion == "3"): 
        print("Debes elegir una opción valida.")
        opcion = input("¿Qué deseas hacer? (Elige una opcíon 1, 2, o 3) \n1. Ataque Pesado \n2. Ráfaga Veloz \n3. Curar \n--- ")
    if opcion == "1":
        if Vida_Enemigo > 20:
            Vida_Enemigo -= Daño_base_del_enemigo
            print(f"atacaste a tu enemigo {Daño_base_Ataque_Pesado} por puntos.")
        elif Vida_Enemigo < 20:
            Vida_Enemigo -= (Daño_base_del_enemigo * 1.5)
            total_daño = Daño_base_del_enemigo * 1.5
            print(f"atacaste a tu enemigo {total_daño} por puntos.")
    elif opcion == "2":
        for i in range (3):
            Vida_Enemigo -= 5
            print(f"Golpe {i+1} conectado por - 5 puntos")
    elif opcion == "3":
        if Vida_Gladiador > 0 and Pociones_de_Vida > 0:
            Vida_Gladiador += 30
            Pociones_de_Vida -= 1
        elif Pociones_de_Vida == 0:
            print("¡No quedan pociones!")

    print("TURNO DEL ENEMIGO \n- ¡El enemigo te atacó por 12 puntos de daño!")
    Vida_Gladiador -=12

    print(f"Tus estadísticas son: \nVida de {nombre}: {Vida_Gladiador} \nVida del enemigo: {Vida_Enemigo} \nPociones de Vida: {Pociones_de_Vida} ")

if Vida_Gladiador > 0 and Vida_Enemigo <= 0:
    print("¡HAS GANADO!")
elif Vida_Enemigo > 0 and Vida_Gladiador <= 0:
    print("¡HAS SIDO DERROTADO!")
