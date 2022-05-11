import csv
from Facultad import Facultad

class ManejaFacultades:
    __listaFacultades=[]
    def __init__(self):
        self.__listaFacultades=[]
    def agregarFacultad(self,facultad):
        if type(facultad)==Facultad:
            self.__listaFacultades.append(facultad)
        else:
            print('Error, no se pudo agregar una facultad a la lista, el tipo de datos es incorrecto.')
    def cargarDesdeArchivo(self):
        nombreArchivo='Facultades.csv'
        try:
            archivo=open(nombreArchivo,encoding='utf-8')
            reader=csv.reader(archivo,delimiter=';')
        except FileNotFoundError:
            print('No se encontro el archivo:"{}", compruebe el nombre o ruta del archivo csv.'.format(nombreArchivo))
        else:
            bandera=True
            facultad=None
            listaCarreras=[]
            for fila in reader:
                if bandera:
                    bandera= not bandera
                    facultad=fila
                else:
                    if(facultad[0]==fila[0]):
                        listaCarreras.append(fila)
                    else:
                        self.agregarFacultad(Facultad(int(facultad[0]),facultad[1],facultad[2],facultad[3],facultad[4],listaCarreras))
                        facultad=fila
                        listaCarreras=[]
            self.agregarFacultad(Facultad(int(facultad[0]),facultad[1],facultad[2],facultad[3],facultad[4],listaCarreras))
            archivo.close()
            print('Fin de la carga desde: ',nombreArchivo)
    def buscarFacultad(self,codigo):
        resultado=-1
        bandera=True
        cantidadFacultades=len(self.__listaFacultades)
        i=0
        while i<cantidadFacultades and bandera:
            if self.__listaFacultades[i].verificarId(codigo):
                bandera=not bandera
                resultado=i
            else:
                i+=1
        return resultado
    def mostrarDatosFacultad(self,codigo):
        iFacultad=self.buscarFacultad(codigo)
        if iFacultad!=-1:
            self.__listaFacultades[iFacultad].mostrarDatos()
        else:
            print('No se encontro la facultad')
    def buscarCarrera(self,nombreCarrera):
        bandera=True
        iFacultad=None
        iCarrera=None
        cantidadFacultades=len(self.__listaFacultades)
        i=0
        while i<cantidadFacultades and bandera:
            busqueda=self.__listaFacultades[i].buscarCarrera(nombreCarrera)
            if busqueda!=-1:
                bandera=False
                iFacultad=i
                iCarrera=busqueda
            else:
                i+=1
        if bandera:
            print('No se encontro la carrera.')
        else:
            self.__listaFacultades[iFacultad].mostrarDatosCarreraYFacultad(iCarrera)
    def test(self):
        print('Comienza test ManejaFacultades')
        manejador=ManejaFacultades()
        print('Metodo cargarDesdeArchivo:')
        manejador.cargarDesdeArchivo()
        print('Metodo agregarFacultad:')
        manejador.agregarFacultad(Facultad(20,'Facultad de Test','Direccion de Test','Capital, San Juan','4233333',[]))
        print('Metodo buscarFacultad:')
        resultado1=manejador.buscarFacultad(20)
        resultado2=manejador.buscarFacultad(30)
        print(resultado1,resultado2)
        print('Metodo mostrarDatosFacultad:')
        manejador.mostrarDatosFacultad(2)
        print('Metodo buscarCarrera:')
        manejador.buscarCarrera('Prueba')
        manejador.buscarCarrera('Ingeniería en Agronómica')
        print('Fin test ManejaFacultades. \n')