class Agenda:
  pass

'''
Realizar una clase que administre una agenda. 
Se debe almacenar para cada contacto el nombre, el teléfono y el 
email. Además deberá mostrar un menú con las siguientes opciones

Añadir contacto
Lista de contactos
Buscar contacto
Editar contacto
Cerrar agenda

'''
class Agenda:
  
  def __init__(self):
    self.contactos=[]
  
  def menu(self):
    continuar=True
    while continuar==True:
      print("Menú de Agenda")
      print("1. Añadir Contacto")
      print("2. Lista de Contactos")
      print("3. Buscar Contacto")
      print("4. Editar Contacto")
      print("5. Cerrar Agenda")
      self.opcion=input("Ingrese una opción")
      
      if self.opcion =="1":
        self.agregar()
      elif self.opcion =="2":
        self.lista()
      elif self.opcion =="3":
        self.buscar()
      elif self.opcion =="4":
        self.editar()
      elif self.opcion =="5":
        continuar=False
      else:
        print("Opción Inválida")
    
  
  def agregar(self):
    print("")
    print("Añadir un nuevo contacto")
    print("========================")
    nom=input("Introduzca el nombre:")
    telf=int(input("Introduzca el telefono:"))
    email=input("Introduzca el mail: ")
    self.contactos.append({'nombre':nom,'telefono':telf,'email':email})
  
  def lista(self):
    print("")
    print("Lista de Contactos")
    print("========================")
    if len(self.contactos) == 0:
      print("No hay contactos en la agenda")
    else:
      for x in range(len(self.contactos)):
        print(self.contactos[x]['nombre'])
  
  def buscar(self):
    print("")
    print("Buscar Contacto")
    print("========================")
    nom=input("Ingrese el contacto a buscar")
    for x in range(len(self.contactos)):
      if nom== self.contactos[x]['nombre']:
        print("Datos del Contaco")
        print("Nombre: ", self.contactos[x]['nombre'])
        print("Telefono: ", self.contactos[x]['telefono'])
        print("Email: ", self.contactos[x]['email'])
        return x
  
  def editar(self):
    print("")
    print("Editar Contacto")
    print("========================")
    posicion=self.buscar()
    condicion=False
    while condicion == False:
      print("Selecciona que quieres editar")
      print("1. Nombre")
      print("2. Telefono")
      print("3. Email")
      print("4. Volver")
      opcion=input("Ingrese la opción")
      if opcion=="1":
        nom=input("Ingrese el nuevo nombre: ")
        self.contactos[posicion]['nombre']= nom
      elif opcion =="2":
        telf=int(input("Ingrese el nuevo telefono: "))
        self.contactos[posicion]['telefono']= telf
      elif opcion == "3":
        email=input("Ingrese el nuevo email: ")
        self.contactos[posicion]['email']= email
      elif opcion =="4":
        condicion = True
      else:
        print("Opcion Inválida")
        
        
        
        
agenda=Agenda()
agenda.menu()
  
    
    
    
    
    



'''
Realizar un programa en el cual se declaren dos valores
enteros por teclado utilizando el método `__init__`. 
Calcular después la suma, resta, multiplicación y división. 
Utilizar un método para cada una e imprimir los resultados 
obtenidos. Llamar a la clase Calculadora.

class Calculadora:
  
  def __init__(self):
    self.valor1=int(input("Ingrese el primer valor"))
    self.valor2=int(input("Ingrese el segundo valor"))
    
  def suma(self):
    suma=self.valor1 + self.valor2
    print("El resultado de la suma es: ", suma)
  
  def resta(self):
    resta=self.valor1 - self.valor2
    print("El resultado de la resta es: ", resta)
  
  def multi(self):
    producto=self.valor1 * self.valor2
    print("El resultado de la multiplicacion es: ", producto)
  
  def divi(self):
    if self.valor2 !=0:
      division=self.valor1 / self.valor2
      print("El resultado de la division es: ", division)
    else:
      print("No se puede dividir entre cero")
      


operacion=Calculadora()
operacion.suma()
operacion.resta()
operacion.multi()
operacion.divi()
'''

'''
Desarrollar un programa que cargue los datos de un triángulo. 
Implementar una clase con los métodos para inicializar los atributos, 
imprimir el valor del lado con un tamaño mayor y  el tipo de triángulo 
que es (equilátero, isósceles o escaleno).


class Triangulo:
  
  def __init__(self):
    self.lado1=int(input("Ingrese el valor del primer lado"))
    self.lado2=int(input("Ingrese el valor del segundo lado"))
    self.lado3=int(input("Ingrese el valor del tercer lado"))
  
  def imprimir(self):
    if self.lado1 > self.lado2 and self.lado1 > self.lado3:
      print("El lado mayor es: ", self.lado1)
    elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
      print("El lado mayor es: ", self.lado2)
    else:
      print("El lado mayor es: ", self.lado3)
  
  def tipo(self):
    if self.lado1 == self.lado2 and self.lado1 == self.lado3:
      print("El triangulo es EQUILÁTERO")
    elif self.lado1 != self.lado2 and self.lado1 != self.lado3:
      print("El triángulo es ESCALENO")
    else:
      print("El triángulo es ISÓCELES")
  

figura=Triangulo()
figura.imprimir()
figura.tipo()
    
'''





'''
Realizar un programa que tenga una clase Persona con las siguientes 
características. La clase tendrá como atributos el nombre y la edad 
de una persona. Implementar los métodos necesarios para inicializar
los atributos, mostrar los datos e indicar si la persona es
debe votar o no

class Persona:
  
  def __init__(self, nombre, edad):
    self.nombre=nombre
    self.edad=edad
  
  def imprimir(self):
    print("Nombre: ", self.nombre)
    print("Edad: ", self.edad)
  
  def votar(self):
    if self.edad >=18 and self.edad <=80:
      print("Tiene que votar")
    else:
      print("No tiene que votar")


votante1=Persona("Mario", 57)
votante2=Persona("Sara", 15)

votante1.votar()
votante2.votar()
'''



'''
Realizar un programa que conste de una clase llamada Alumno 
que tenga como atributos el nombre y la nota del alumno. 
Definir los métodos para inicializar sus atributos, imprimirlos y 
mostrar un mensaje con el resultado de la nota y si ha aprobado o no.


class Alumno:
  
  def __init__(self, nombre, nota):
    self.nombre=nombre
    self.nota=nota
  
  def imprimir(self):
    print("Nombre: ", self.nombre)
    print("Nota: ", self.nota)
    
  def resultado(self):
    if self.nota <4:
      print("El alumno está desaprobado")
    else:
      print("El alumno está aprobado")


DNI4596236= Alumno("Maria",10)
DNI7896513= Alumno("Horacio",3)

'''






'''
class Perro:
  #Atributos de Clase
  especie="mamífero"
  
  #Constructor, método que se ejecuta cuando se crea un objeto
  def __init__(self, nombre, raza):
    #print(f"Creando perro {nombre},{raza}")
    #Atributos de Instancia - Pertenecen a cada objeto
    self.nombre=nombre
    self.raza=raza
  
  def ladra(self):
    print("Guau!")
  
  def caminar(self,pasos):
    print("Caminando ", pasos, "pasos")
  
  def comer(self):
    print("Ñom, ñom")
  
  
mi_perro=Perro("Toby","Collie")
perro_vecino=Perro("Firulais","Ovejero")

print("Mi perro dice:")
mi_perro.ladra()

print("El perro de vecino responde:")
perro_vecino.ladra()

mi_perro.caminar(50)
perro_vecino.comer()
'''
