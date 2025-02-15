import time
import os
import clases
import pandas as pd
import yagmail
from dotenv import load_dotenv
import pywhatkit as kit
import datetime
import inputFunctions

load_dotenv()

def enviarWhastapp(numero,nombre):
  now = datetime.datetime.now()
  minutos_envio = now.minute + 3

  try:
    kit.sendwhatmsg(numero, f'{nombre} este es un mensaje de cesar', now.hour, minutos_envio, 20, True)
    print('Mensaje de whatsapp enviado')
  except Exception as e:
    print(f"Error al enviar mensaje de WhatsApp: {e}")

def enviarCorreo(receptor, nombre):
    asunto = 'Confirmación de registro'
    cuerpo = f'{nombre} ha sido registrado en el sistema de Inventarios OS'
    remitente = 'cesarcordero496@gmail.com'
    app_key = os.environ.get('APP_KEY')  # Recupera la contraseña de una variable de entorno

    if not app_key:
        print('Error: La contraseña no está definida en la variable de entorno APP_KEY')
        return False  # Retorna False si la contraseña no está definida

    if not app_key.strip():
      print('Error: La contraseña en la variable de entorno APP_KEY está vacía')
      return False

    try:
        yag = yagmail.SMTP(remitente, app_key)
        yag.send(receptor, asunto, cuerpo)
        print('Correo enviado')
        return True  # Retorna True si el correo se envió correctamente
    except Exception as e:
        print(f'Error al enviar el correo: {type(e).__name__} - {e}')
        return False  # Retorna False si hay otro error

def export_csv(lista,tipo):
  if not lista:
      print('No hay elementos en la lista')
      return
  lista_diccionarios = [vars(item) for item in lista]
  df = pd.DataFrame(lista_diccionarios)

  if tipo==1:
     nombre_base = 'tabla de Productos'
  else:
     nombre_base = 'tabla de usuarios'

  fecha_hora = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
  ruta_carpeta = 'csv'

  if not os.path.exists(ruta_carpeta):
     os.makedirs(ruta_carpeta)

  nombre_archivo = os.path.join(ruta_carpeta,f'{nombre_base}_{fecha_hora}.csv')
  


  try:  
    df.to_csv(nombre_archivo, index=False, sep=';')
    print(f'Lista exportada bajo el nombre de: {nombre_archivo}')
    return True
  except Exception as e:
    print(f'Error al exportar DataFrame: {type(e).__name__} - {e}')
    return False




def agregarProducto(lista):
  try:
    nombre = inputFunctions.validar_nombre_productos(lista)
    precio = inputFunctions.validar_precio()
    cantidad = inputFunctions.validar_cantidad()
    categoria = inputFunctions.validar_categoria()

    item = clases.Producto(nombre,precio,cantidad,categoria)
    lista.append(item)
    print('Producto añadido correctamente.')
    time.sleep(1)
  except Exception as e:
    print(f'Error al agregar usuario: {type(e).__name__} - {e}')

def agregarUsuarios(lista):
  try:
    nombre = inputFunctions.validar_nombre_usuario()
    email = inputFunctions.validar_email(lista)
    telefono = inputFunctions.validar_telefono()
    direccion = inputFunctions.validar_direccion()
  
    item = clases.Usuarios(nombre,email,telefono,direccion)
    lista.append(item)
    #enviarCorreo(email,nombre)
    #enviarWhastapp(telefono, nombre)
    print('Usuario añadido correctamente.')
    time.sleep(1)
  except Exception as e:
    print(f'Error al agregar usuario: {type(e).__name__} - {e}')


def eliminar(lista):
  if len(lista) == 0:
    print('No hay items en la lista.')
    return
  
  while True: 
    try:
      nombre = input('Ingrese el nombre del item a eliminar (dejelo en blanco si no quiere eliminar nada): ')
      if nombre == '':
        print('Cerrando funcion')
        return
      
      indice = buscar(lista, nombre)
      if (0 <=indice < len(lista)): 
        confirmacion = input(f'¿Está seguro que desea eliminar el elemento "{lista[indice].nombre}"? (s/n)').lower
        if confirmacion == 's':
          del lista[indice]
          print('Item eliminado correctamente')
          break
        else:
           print('Elimnacion cancelada.')
      else:
        print('No se encontro ningun elemento con ese nombre.')
    except ValueError:
      print('Ingrese un nombre valido') 
  time.sleep(1)

def update(lista, tipo):
  if len(lista) == 0:
    print('No hay items en la lista.')
    return
  
  while True:
      if tipo == 1:  
        nombre = input('Ingrese el nombre del producto a actualizar (dejelo en blanco si no quiere actualizar nada): ')
      if tipo == 2:
        nombre = input('Ingrese el nombre del usuario a actualizar (dejelo en blanco si no quiere actualizar nada): ')
      if not nombre:
        print('Cerrando funcion')
        return
      
      indice = buscar(lista, nombre)
      if (0 <=indice < len(lista)): 
        item_actualizar = lista[indice]
        print(f'Actualizando item: {item_actualizar.nombre}')

        try:
          if tipo == 1: 
              item_actualizar.nombre = inputFunctions.validar_nombre_productos(lista)
              item_actualizar.precio = inputFunctions.validar_precio()
              item_actualizar.cantidad = inputFunctions.validar_cantidad()
              item_actualizar.categoria = inputFunctions.validar_categoria()

          if tipo == 2:
            item_actualizar.nombre = inputFunctions.validar_nombre_usuario()
            item_actualizar.email = inputFunctions.validar_email(lista)
            item_actualizar.telefono = inputFunctions.validar_telefono()
            item_actualizar.direccion = inputFunctions.validar_direccion()
    
          print('Item actualizado correctamente')
          break
      
        except AttributeError as e:
          print(f'Error: El objeto no tiene el atributo {e}')
          return
        except ValueError as e:
          print('Error: {e}')
          return
        except Exception as e:
          print(f'Error inesperado: {e}')
          return
        
      print('Fuera de rango')
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

  while True:
    try:
      for i in range(0, len(df), 12):
        grupo = df.iloc[i:i + 12]

        if not grupo.empty:
          print(grupo.to_string(index=True))
          print("--------------------------------------------------")

          continuar = input('Presione Enter para continuar (o escriba "s" para salir): ')
          if continuar.lower() == 's':
             return
          
      print('No hay mas elementos para mostrar')
      return
    
    except AttributeError as e:
      print(f'Error: El objeto no tiene el atributo {e}')
      return
    except Exception as e:
      print(f'Error inesperado: {e}')
      return

def buscar(lista, nombre):
    for i, item in enumerate(lista):
        if item.nombre.lower() == nombre.lower():
            print('Item encontrado')
            return i  
    print('No se encontro el item')
    return -1  