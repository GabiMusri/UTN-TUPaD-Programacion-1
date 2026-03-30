# EJERCICIO 1: CAJA DE KIOSCO.
# CAJA DE KIOSCO:  Simular una compra con validaciones y cálculo de total. 
#Saluda al usuario y pide nombre de cliente.
print("Bienvenid@")
nombre = input("Por favor ingrese su nombre de cliente: ").strip()
#Verifica que sea un nombre correcto.
while nombre == " " or not nombre.isalpha():
    print("Debe ingresar un nombre sin números ni espacios.")
    nombre = input("Por favor ingrese su nombre de cliente: ").strip()
print("Hola,",nombre)
#Se solicita la cantidad de producto a ingresar. 
cant_prod_str = input("Ingrese cantidad de productos usando un número entero positivo.: ").strip()
#Se valida que no sea un número incorrecto y se pide la cantidad nuevamente
while not cant_prod_str.isdigit() or int(cant_prod_str == 0):
    print("Error, debe ingresar un número entero positivo.")
    cant_prod_str = input("Ingrese cantidad de producto usando un número entero positivo.: ").strip()

#Se convierte a número entero. 
cant_prod_int = int(cant_prod_str)
total_sin_desc = 0
total_con_desc = 0.0

#Se solicitan datos de precio y desceunto.
for i in range (1,cant_prod_int + 1):
    precio_str = input(f"Ingrese el precio del producto {i} usando números enteros positivos - Precio: $ ").strip()
    #Se valida que sea un número valido. 
    while not precio_str.isdigit() or int(precio_str) == 0:
        print("Error, ingrese un número entero positivo.")
        precio_str = input(f"Ingrese el precio del producto {i} usando números enteros positivos - Precio: $ ").strip()
#Se convierte a entero.
    precio_int = int(precio_str)
#Se consulta si el producto tiene descuento.
    desc = input("¿El prod. tiene descuento? (S para sí, N para no.): ").strip().lower()
#Se valida que se elija una opción correcta. 
    while desc != "s" and desc != "n": 
        print("Error, debe ingresar S para sí, N para no. ")
        desc = input("¿El prod. tiene descuento? (S para sí, N para no.): ").strip().lower()

    total_sin_desc += precio_int
#Se calculan los desceuentos.
    if desc == "s": 
        precio_final = (precio_int * 0.9)
    else: 
        precio_final = precio_int

    total_con_desc += precio_final

ahorro = total_sin_desc - total_con_desc
promedio  = total_con_desc / cant_prod_int
#Se imprime el total.
print(f"Total sin descuentos: $ {total_sin_desc:.2f}")
print(f"Total con descuentos: $ {total_con_desc:.2f} ")
print(f"Ahorro: $ {ahorro:.2f}")
print(f"Promedio por producto: $ {promedio:.2f}")