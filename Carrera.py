class Carrera:
    __codigo=0
    __nombre=''
    __titulo=''
    __duracion=''
    __tipo=''
    def __init__(self,codigo=0,nombre='',titulo='',duracion='',tipo=''):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__titulo=titulo
        self.__duracion=duracion
        self.__tipo=tipo
    def verificarNombre(self,nombre):
        return self.__nombre==nombre
    def getCodigo(self):
        return self.__codigo
    def __str__(self):
        return 'Nombre:{}, Duracion:{}'.format(self.__nombre,self.__duracion)
    def test(self):
        print('Comienza test Carrera')
        carrera=Carrera(10,'Ingenieria en Metalúrgica Extractiva','Ingeniero Metalurgista','Diez Semestres','Grado')
        print('Metodo verificarNombre:')
        print(carrera.verificarNombre('Ingenieria en Metalúrgica Extractiva'))
        print('Metodo getCodigo:')
        print(carrera.getCodigo())
        print(carrera)
        print('Fin test Carrera. \n')