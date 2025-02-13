import re 

regex_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
regex_telefono = r"^(?:\+?1[-.\s]?)?(?:\(\d{3}\)[-.\s]?|\d{3}[-.\s]?)(?:\d{3}[-.\s]?\d{4})$"
regex_categoria = r'^[a-zA-Z]+$'
regex_nombres = r'^[a-zA-Z\s]+$'


def atributo_repetido(nuevo_valor, lista, atributo):
    for item in lista:
        valor_item = getattr(item, atributo)  # Obtiene el valor del atributo dinámicamente
        if atributo == "email":
            if  nuevo_valor == valor_item:
                print('Este correo ya esta registrado')
                return True  # El email ya existe
        elif atributo == "nombre":
            if nuevo_valor.upper() == valor_item.upper():
                print('Este producto ya esta registrado')
                return True  # El nombre ya existe
    return False  # El valor no existe

#Productos
def validar_nombre_productos(lista):
    while True:
      nombre = input('Nombre de Producto: ')
      if re.match(regex_nombres,nombre):
          if not atributo_repetido(nombre, lista, 'nombre'):
              return nombre
      else:
          print('Nombre invalido, unicamente debe de contener letras y espacios')

def validar_precio():
    while True:
      try: 
        precio = float(input('Precio de producto en decimales '))
        if not precio <= 0:
          return precio
        print('Ingrese un numero mayor a 0')
      except ValueError:
        print('Ingrese un numero decimal valido valido')

def validar_cantidad():
    while True: 
      try:
        cantidad = int(input('Cantidad de producto: '))
        if not cantidad <= 0:
          return cantidad
        print('Porfavor ingrese una cantidad mayor a 0')
      except ValueError:
        print('Ingrese un numero entero valido')

def validar_categoria():
   while True :
    categoria = input('Categoria del producto: ').upper()
    if re.match(regex_categoria, categoria) and not categoria == '':
      return categoria
    else:
       print('La categoría solo debe contener letras y unicamente tener letras')
              


#Usuarios
def validar_nombre_usuario():
    while True:
        nombre = input('Nombre del usuario: ')
        if not nombre == '':  # Verifica si el nombre no está vacío o solo contiene espacios en blanco
            return nombre
        else:
            print('El nombre no debe quedar vacío.')
            

def validar_email(lista):
    while True:
        email = input('Email del usuario: ')
        if re.match(regex_email, email):
            if not atributo_repetido(email, lista, 'email'):
              return email
        else:
            print('Email inválido.')

def validar_telefono():
    while True:
        telefono = input('Teléfono del usuario: +58')
        if re.match(regex_telefono, telefono):
            return '+58' + telefono
        else:
            print('Por favor, ingrese un número telefónico válido (9 dígitos sin el +58).')

def validar_direccion():
    while True:
        direccion = input('Dirección del usuario: ')
        if not direccion =='':
            return direccion  
        else:
           print('La dirección no debe quedar vacía.')
            