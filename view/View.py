from view.contents.Home import Home
from view.contents.Popup import Popup
from view.contents.Alumnos import Alumnos
from view.contents.FormAlumno import FormAlumno
from view.contents.FormSocios import FormSocios
from view.contents.Socios import Socio
from PyQt5.QtWidgets import QApplication
import math

class View:
    def __init__(self, generalController):
        self.generalController = generalController
        self.alumnosView = None
    
    def iniciarVista(self):
        self.app = QApplication([])
        self.homeView = Home(self)
        self.homeView.start()
    
    def mostrarModuloAlumnos(self):
        if self.alumnosView is not None:
            cantidadAlumnos = self.alumnosView.cantidadAlumnos
            if cantidadAlumnos is None or cantidadAlumnos <= 0:
                self.alumnosView = Alumnos(self)
            else:
                cantPaginas = math.ceil(cantidadAlumnos/self.alumnosView.cantidadElementos)
                self.alumnosView = Alumnos(self, cantPaginas)
        else:
            self.alumnosView = Alumnos(self)            
        self.alumnosView.start()

    def mostrarFormAlumno(self, title, update=False, alumnoUpdate=None):
        if title is False:
            title = "Nuevo alumno | CEP"
        self.formAlumno = FormAlumno(self, title=title, update=update, alumnoUpdate=alumnoUpdate)
        self.formAlumno.start()        
    
    def mostrarFormSocio(self):
        self.formSocio = FormSocios(self)
        self.formSocio.start()
    
    def mostrarModuloSocio(self):
        self.socioView = Socio(self)
        self.socioView.start()
    
    def salir(self):
        self.app.exit()

    def mostrarPopup(self, titleWindow, title, message):
        self.popup = Popup(view=self, title=title, titleWindow=titleWindow, message=message)
        self.popup.start()