from ManejaFacultades import ManejaFacultades
from Menu import Menu

if __name__== '__main__':
    manejadorFacultades=ManejaFacultades()
    manejadorFacultades.cargarDesdeArchivo()
    menu=Menu()
    menu.lanzarMenu(manejadorFacultades)