import time
import os
import funciones 

listaProductos = []  # Inicializa tus listas
listaUsuarios = []

while True:  # Bucle principal para el menú de inicio
    print('Bienvenido a Inventarie OS.')
    print('')

    while True:  # Bucle para validar la entrada del usuario
        print('Desea ingresar a:\n1) Lista de productos\n2) Lista de usuarios\n3) Salir')
        opcion = input('Ingrese un número correspondiente a las opciones ya dadas: ')
        if opcion in ('1', '2', '3'):
            break
        print('Por favor ingrese un número válido')
        time.sleep(1)
        os.system('cls')

    time.sleep(1)
    os.system('cls')

    if opcion == '1':
        while True:  # Bucle para el menú de productos
            while True:  # Bucle para validar la entrada del usuario
                print('1) Ingresar nuevo producto\n2) Eliminar producto\n3) Modificar producto\n4) Ver lista\n5) Exportar a csv \n6) Salir')
                opcion_producto = input('Ingrese un número correspondiente a las opciones ya dadas: ')
                if opcion_producto in ('1', '2', '3', '4', '5','6'):
                    break
                print('Por favor ingrese un número válido')
                time.sleep(1)
                os.system('cls')

            time.sleep(1)
            os.system('cls')

            match opcion_producto:
                case '1':
                    funciones.agregarProducto(listaProductos)
                case '2':
                    funciones.eliminar(listaProductos)
                case '3':
                    funciones.update(listaProductos,1)
                case '4':
                    funciones.verLista(listaProductos, 1)
                case '5':
                    funciones.export_csv(listaProductos,1)
                case '6':
                    break  # Sale del menú de productos y regresa al menú principal

            time.sleep(1)
            os.system('cls')

    elif opcion == '2':
        while True:  # Bucle para el menú de usuarios
            while True:  # Bucle para validar la entrada del usuario
                print('1) Ingresar nuevo Usuario\n2) Eliminar Usuario\n3) Modificar Usuario\n4) Ver lista\n5) Exportar a csv \n6) Salir')
                opcion_usuario = input('Ingrese un número correspondiente a las opciones ya dadas: ')
                if opcion_usuario in ('1', '2', '3', '4', '5','6'):
                    break
                print('Por favor ingrese un número válido')
                time.sleep(1)
                os.system('cls')

            time.sleep(1)
            os.system('cls')

            match opcion_usuario:
                case '1':
                    funciones.agregarUsuarios(listaUsuarios)
                case '2':
                    funciones.eliminar(listaUsuarios)
                case '3':
                    funciones.update(listaUsuarios,2)
                case '4':
                    funciones.verLista(listaUsuarios, 2)
                case '5':
                    funciones.export_csv(listaUsuarios,2)
                case '6':
                    break
            time.sleep(1)
            os.system('cls')

    elif opcion == '3':
        print('Adiós. ')
        time.sleep(2)
        os.system('cls')
        break  # Sale del bucle principal y termina el programa