import time
import os
import clases
import re
import pandas as pd
import yagmail

regex_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
regex_telefono = r"^(?:\+?1[-.\s]?)?(?:\(\d{3}\)[-.\s]?|\d{3}[-.\s]?)(?:\d{3}[-.\s]?\d{4})$"

def atributo_repetido(nuevo_valor, lista, atributo):
    for item in lista:
        valor_item = getattr(item, atributo)  # Obtiene el valor del atributo dinámicamente
        if atributo == "email":
            if  nuevo_valor == valor_item:
                print('Este correo ya esta registrado')
                return True  # El email ya existe
        elif atributo == "nombre":
            if nuevo_valor == valor_item:
                print('Este producto ya esta registrado')
                return True  # El nombre ya existe
    return False  # El valor no existe

def enviarCorreo(receptor, nombre):
  asunto = 'Confirmacion de registro'
  cuerpo = f'{nombre} a sido registrado en el sistema de Inventarios OS'
  remitente = 'cesarcordero496@gmail.com'
  password = os. environ.get('password')

  if not password:
    print('Error: La contraseña no está definida en la variable de entorno password')
    return False

  try:
    yag = yagmail.SMTP(remitente,password)
    yag.send(receptor,asunto,cuerpo)
    print('Correo enviado')
    return True
  except yagmail.SMTPAuthenticationError as e:
    print(f'Error de autenticación SMTP: {e}')
    return False 
  except Exception as e:
    print(f'Error al enviar el correo: {e}') 

def agregarProducto(lista):
  
  while True:
    nombre = input('Nombre del producto: ')
    if not atributo_repetido(nombre, lista, 'nombre') and not nombre == '':
      break
    print('El nombre no deberia de quedar vacio ni ser repetido.')
  
  while True: 
    try: 
      precio = float(input('Precio de producto en decimales '))
      if not precio <= 0:
        break
      print('Ingrese un numero mayor a 0')
    except ValueError:
      print('Ingrese un numero decimal valido valido')

  while True: 
    try:
      cantidad = int(input('Cantidad de producto: '))
      if not cantidad <= 0:
        break
      print('Porfavor ingrese una cantidad mayor a 0')
    except ValueError:
      print('Ingrese un numero entero valido')
  
  
  while True :
    categoria = input('Categoria del producto: ').upper()
    if not categoria =='':
      break
    print('La categoria no deberia de quedar vacia.')
  
  item = clases.Producto(nombre,precio,cantidad,categoria)
  lista.append(item)
  print('Producto añadido correctamente.')
  time.sleep(1)

def agregarUsuarios(lista):
  while True:
    nombre = input('Nombre del usuario: ')
    if not nombre == '':
      break
    print('El nombre no deberia de quedar vacio.')
    
  
  
  while True:
    email = input('Email de usuario: ')
    if re.match(regex_email, email):
      if not atributo_repetido(email, lista, 'email'):
        break
    print('Email invalido') 
      
  while True: 
    telefono = input('Telefono del usuario: ')
    if re.match(regex_telefono,telefono): 
      break;
    print('Porfavor ingrese un numero telefonico valido')
    
  while True:
    direccion = input('Direccion del usuario: ')
    if not direccion == '':
      break
    print('La direccion no deberia de quedar vacia.')
  
  item = clases.Usuarios(nombre,email,telefono,direccion)
  lista.append(item)
  print('Usuario añadido correctamente.')
  time.sleep(1)


def eliminar(lista):
  if len(lista) == 0:
    print('No hay items en la lista.')
    return
  while True: 
    try:
      nombre = ''
      nombre = int(input('Ingrese el nombre del item a eliminar (dejelo en blanco si no quiere eliminar nada): '))
      if nombre == '':
        print('Cerrando funcion')
        return
      indice = buscar(lista, nombre)
      if (0 <=indice < len(lista)): 
        del lista[indice]
        print('Item eliminado correctamente')
        break
      print('Fuera de rango')
    except ValueError:
      print('Ingrese un nombre valido') 
  time.sleep(1)

def update(lista):
  if len(lista) == 0:
    print('No hay items en la lista.')
    return
  while True: 
    try:
      nombre = ''
      nombre = int(input('Ingrese el nombre del item a actualizar (dejelo en blanco si no quiere actualizar nada): '))
      if nombre == '':
        print('Cerrando funcion')
        return
      indice = buscar(lista, nombre)
      if (0 <=indice < len(lista)): 
        del lista[indice]
        print('Item actualizado correctamente')
        break
      print('Fuera de rango')
    except ValueError:
      print('Ingrese un nombre valido') 
  time.sleep(1)

def verLista(lista, num):
  if not lista:
        print('No hay elementos en la lista')
        return

  lista_diccionarios = [vars(item) for item in lista]

  df = pd.DataFrame(lista_diccionarios)
  if num == 1:
    print('Inventario:')
  else:
    print('Usuarios: ')

  for i in range(0, len(df), 12):
    grupo = df.iloc[i:i + 12]

    if not grupo.empty:
      print(grupo.to_string(index=True))
      print("--------------------------------------------------")
      time.sleep(1)


def buscar(lista, nombre):
    for i, item in enumerate(lista):
        if item.nombre == nombre:
            print('Item encontrado')
            return i  # Retorna el objeto si lo encuentra
    print('No se encontro el item')
    return None  # Retorna None si no lo encuentra