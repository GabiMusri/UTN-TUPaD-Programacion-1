#EJERCICIO 3: AGENDA DE TURNOS CON NOMBRE. 
#Definir cantidad de turnos para cada día: 
turnos_disponibles_lunes = 4
pac_1_lun = ""
pac_2_lun = ""
pac_3_lun = ""
pac_4_lun = ""
turnos_disponibles_martes = 3
pac_1_mar = ""
pac_2_mar = ""
pac_3_mar = ""
#Solicitar nombre de operador y verificar que sean letras las ingresadas.
nombre_operador = input("Ingrese nombre de operador: ").strip().upper()
while not nombre_operador.isalpha():
    nombre_operador = input("Error. Ingrese nombre válido: ").strip().upper()

print(f"Bienvenid@ {nombre_operador}")

opcion = ""
#Mostrar menú de opciones
while opcion != "5":
    print("-OPCIONES DEL MENÚ-")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen")
    print("5. Salir")

    opcion = input("Ingrese una opción del 1 al 5: ")

    #Opciones de agendar turno: 
    if opcion == "1":
        dia = input("1 para lunes, 2= para martes: ")
        #Solicitar nombre y comprobar que sean letras
        nombre = input("Nombre paciente: ").strip().upper()
        while not nombre.isalpha():
            nombre = input("Error, debe ingresar solo letras: ").strip().upper()

        if dia == "1":
            if nombre == pac_1_lun or nombre == pac_2_lun or nombre == pac_3_lun or nombre == pac_4_lun:
                print("Este paciente está repetido")
            else:
                if pac_1_lun == "":
                    pac_1_lun = nombre
                    turnos_disponibles_lunes -= 1
                elif pac_2_lun == "":
                    pac_2_lun = nombre
                    turnos_disponibles_lunes -= 1
                elif pac_3_lun == "":
                    pac_3_lun = nombre
                    turnos_disponibles_lunes -= 1
                elif pac_4_lun == "":
                    pac_4_lun = nombre
                    turnos_disponibles_lunes -= 1
                else:
                    print("No hay turnos lunes")
        elif dia == "2":
            if nombre == pac_1_mar or nombre == pac_2_mar or nombre == pac_3_mar:
                print("Paciente repetido")
            else:
                if pac_1_mar == "":
                    pac_1_mar = nombre
                    turnos_disponibles_martes -= 1
                elif pac_2_mar == "":
                    pac_2_mar = nombre
                    turnos_disponibles_martes -= 1
                elif pac_3_mar == "":
                    pac_3_mar = nombre
                    turnos_disponibles_martes -= 1
                else:
                    print("No hay turnos martes")
    #Cancelación de turnos por nombre.
    #Ingresar el día y nombre del paciente a cancelar.
    elif opcion == "2":
        dia = input("1 para lunes, 2= para martes: ")

        nombre = input("Nombre del paciente a cancelar: ").strip().upper()
        while not nombre.isalpha():
            nombre = input("Error, debe ingresar solo letras: : ").strip().upper()

        if dia == "1":
            if pac_1_lun == nombre:
                pac_1_lun = ""
                turnos_disponibles_lunes += 1
            elif pac_2_lun == nombre:
                pac_2_lun = ""
                turnos_disponibles_lunes += 1
            elif pac_3_lun == nombre:
                pac_3_lun = ""
                turnos_disponibles_lunes += 1
            elif pac_4_lun == nombre:
                pac_4_lun = ""
                turnos_disponibles_lunes += 1
            else:
                print("No encontrado")

        elif dia == "2":
            if pac_1_mar == nombre:
                pac_1_mar = ""
                turnos_disponibles_martes += 1
            elif pac_2_mar == nombre:
                pac_2_mar = ""
                turnos_disponibles_martes += 1
            elif pac_3_mar == nombre:
                pac_3_mar = ""
                turnos_disponibles_martes += 1
            else:
                print("No encontrado")
    #Ver agenda de tunos como solicita la actividad. 
    elif opcion == "3":
        dia = input("1 para lunes, 2= para martes: ")

        if dia == "1":
            print("1:", pac_1_lun if pac_1_lun != "" else "(libre)")
            print("2:", pac_2_lun if pac_2_lun != "" else "(libre)")
            print("3:", pac_3_lun if pac_3_lun != "" else "(libre)")
            print("4:", pac_4_lun if pac_4_lun != "" else "(libre)")

        elif dia == "2":
            print("1:", pac_1_mar if pac_1_mar != "" else "(libre)")
            print("2:", pac_2_mar if pac_2_mar != "" else "(libre)")
            print("3:", pac_3_mar if pac_3_mar != "" else "(libre)") 
    
    #Resumen final de turnos: 
    elif opcion == "4":
        ocupados_lunes = 4 - turnos_disponibles_lunes
        ocupados_martes = 3 - turnos_disponibles_martes

        print("Lunes:", ocupados_lunes, "ocupados,", turnos_disponibles_lunes, "libres")
        print("Martes:", ocupados_martes, "ocupados,", turnos_disponibles_martes, "libres")

        if ocupados_lunes > ocupados_martes:
            print("Más turnos: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Más turnos: Martes")
        else:
            print("Empate")

else: 
    print("Gracias por usar mi programa.")