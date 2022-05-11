
from Carrera import Carrera
from Facultad import Facultad
from ManejaFacultades import ManejaFacultades


class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            1:self.opcion1,
            2:self.opcion2,
            3:self.test,
            4:self.salir
        }
    def lanzarMenu(self,manejador):
        #Menu opciones
        i=len(self.__opciones)
        opcion=0
        while(i!=opcion):
            print('Menu:')
            print('-Ingrese 1 para dado el código  de una facultad y mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad.')
            print('-Ingrese 2 para dado el nombre de una carrera, mostrar código , nombre y localidad de la facultad donde esta se dicta.')
            print('-Ingrese 3 para ejecutar un test.')
            print('-Ingrese 4 para salir.')
            opcion=self.cargarNumeroEntero('Ingrese opcion:\n')
            ejecutar=self.__opciones.get(opcion,self.error)
            if opcion>0 and opcion<3:
                ejecutar(manejador)
            else:
                ejecutar()
    def opcion1(self,manejador):
        codigo=self.cargarNumeroEntero('Ingrese codigo de facultad:\n')
        manejador.mostrarDatosFacultad(codigo)
    def opcion2(self,manejador):
        nombreCarrera=input('Ingrese nombre de la carrera:\n')
        manejador.buscarCarrera(nombreCarrera)
    def cargarNumeroEntero(self,mensaje='Ingrese valor:'):
        numero=None
        bandera=True
        while bandera:
            try:
                numero=int(input(mensaje))
            except ValueError:
                print('ERROR: Se debe ingresar un numero entero.')
            else:
                bandera=False
        return numero
    def test(self):
        manejador=ManejaFacultades()
        carrera=Carrera()
        facultad=Facultad()
        carrera.test()
        facultad.test()
        manejador.test()
        
    def error(self):
        #Mensaje cuando ingresa opcion incorrecta
        print('Opción incorrecta')
    def salir(self):
        #Mensaje cuando decide salir
        print('Se cerro el menú')