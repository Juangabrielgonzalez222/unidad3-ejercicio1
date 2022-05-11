from Carrera import Carrera

class Facultad:
    __codigo=0
    __nombre=''
    __direccion=''
    __localidad=''
    __telefono=''
    __listaCarreras=[]
    def __init__(self,codigo=0,nombre='',direccion='',localidad='',telefono='',lista=[]):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__direccion=direccion
        self.__localidad=localidad
        self.__telefono=telefono
        self.__listaCarreras=[]
        for carrera in lista:
            self.__listaCarreras.append(Carrera(int(carrera[1]),carrera[2],carrera[3],carrera[4],carrera[5]))
    def verificarId(self,numero):
        return self.__codigo==numero
    def mostrarDatos(self):
        print('Facultad:',self.__nombre)
        print('Carreras:')
        for carrera in self.__listaCarreras:
            print(carrera)
    def mostrarDatosCarreraYFacultad(self,iCarrera):
        if iCarrera<len(self.__listaCarreras) and iCarrera>=0:
            print('Codigo:{}, Nombre:{}, Localidad:{}'.format(str(self.__codigo)+str(self.__listaCarreras[iCarrera].getCodigo()),self.__nombre,self.__localidad))
        else:
            print('La carrera no se encontro, verifique la posicion.')
    def buscarCarrera(self,nombreCarrera):
        resultado=-1
        cantidadCarreras=len(self.__listaCarreras)
        bandera=True
        i=0
        while i<cantidadCarreras and bandera:
            if self.__listaCarreras[i].verificarNombre(nombreCarrera):
                resultado=i
                bandera=False
            else:
                i+=1
        return resultado
    def test(self):
        print('Comienza test Facultad')
        lista=[]
        lista.append(['1','10','Ingenieria en Metalúrgica Extractiva','Ingeniero Metalurgista','Diez Semestres','Grado'])
        lista.append(['1','7','Ingenieria Mecánica','Ingeniero Mecánico','Once Semestres','Grado'])
        facultad=Facultad(1,'Facultad de Ingeniería','Libertador General San Martin 1109 (O)','Capital,SanJuan','0264-4222074 - 4222643',lista)
        print('Metodo verificarId:')
        print(facultad.verificarId(1))
        print('Metodo mostrarDatos:')
        facultad.mostrarDatos()
        print('Metodo buscarCarrera:')
        resultado1=facultad.buscarCarrera('Prueba')
        resultado2=facultad.buscarCarrera('Ingenieria Mecánica')
        print(resultado1,resultado2)
        print('Metodo mostrarDatosCarreraYFacultad:')
        facultad.mostrarDatosCarreraYFacultad(resultado1)
        facultad.mostrarDatosCarreraYFacultad(resultado2)
        print('Fin test Facultad. \n')