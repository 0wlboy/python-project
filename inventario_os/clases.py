import datetime

class Producto:
  def __init__(self, nombre, precio, cantidad, categoria):
    self.nombre = nombre
    self.precio = precio
    self.cantidad = cantidad
    self.categoria = categoria
    self.fechaCreacion = datetime.date.today()

  def actualizar(self):
    print(f"Actualizando Producto: {self.nombre}")

    nuevo_nombre = input('Nuevo nombre (dejar en blanco para no cambiar): ')
    if nuevo_nombre:  
      self.nombre = nuevo_nombre

    nuevo_precio = input('Nuevo precio (dejar en blanco para no cambiar): ')
    if nuevo_precio:  
      self.precio = nuevo_precio

    nueva_cantidad = input('Nueva cantidad (dejar en blanco para no cambiar): ')
    if nueva_cantidad:  
      self.cantidad = nueva_cantidad
    
    nueva_categoria = input('Nueva categoria (dejar en blanco para no cambiar): ')
    if nueva_categoria:  
      self.categoria = nueva_categoria

    print('Producto modificado correctamente.')

  

class Usuarios:
  def __init__(self, nombre, email, telefono, direccion):
    self.nombre = nombre 
    self.email = email 
    self.telefono = telefono
    self.direccion = direccion
  
  def actualizar(self):
    print(f"Actualizando usuario: {self.nombre}")

    nuevo_nombre = input('Nuevo nombre (dejar en blanco para no cambiar): ')
    if nuevo_nombre:  
      self.nombre = nuevo_nombre

    nuevo_email = input('Nuevo email (dejar en blanco para no cambiar): ')
    if nuevo_email:  
      self.email = nuevo_email

    nuevo_telefono = input('Nuevo telefono (dejar en blanco para no cambiar): ')
    if nuevo_telefono:  
      self.telefono = nuevo_telefono
    
    nueva_direccion= input('Nueva direccion (dejar en blanco para no cambiar): ')
    if nueva_direccion:  
      self.categoria = nueva_direccion

    print('Usuario modificado correctamente.')