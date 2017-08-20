from abc import ABCMeta, abstractmethod
from consultor import *


class Command():
    listo = False
    com = None
    grado = None
    curso = None
    grupo = None
    nombre = None
    _metaclass_ = ABCMeta
    consultor = Consultor()
    @classmethod
    def estaListo(self):
        return self.listo

    @abstractmethod
    def ejecutar(self): raise NotImplementedError


class CommandHorarios(Command):

    def __init__(self, grado, curso, grupo, asignatura=None):
        self.grado = grado
        self.curso = curso
        self.grupo = grupo
        self.nombre = asignatura

    def ejecutar(self):
        if self.nombre != None:  # Horario de una asignatura concreta
            pass
        elif self.nombre == None:  # Horario de un curso completo
           return self.consultor.consultaHorarios(self.grado, self.curso, self.grupo)


class CommandTutoriaAsignatura(Command):

    def __init__(self,asignatura ):
        self.nombre = asignatura

    def ejecutar(self):
        return self.consultor.consultaTutoriasAsignatura(self.nombre)


class CommandTutoriaProfesor(Command):
    apellido = None
    apellido2 = None

    def __init__(self, nombre, apellido, apellido2):
        self.nombre = nombre
        self.apellido = apellido
        self.apellido2 = apellido2

    def ejecutar(self):
        return self.consultor.consultaTutoriasProfesor(self.nombre, self.apellido, self.apellido2)


class CommandTutoriaClase(Command):
    cuatrimestre = None

    def __init__(self, grado, curso, grupo, cuatrimestre, asignatura=None):
        self.grado = grado
        self.curso = curso
        self.grupo = grupo
        self.nombre = asignatura
        self.cuatrimestre = cuatrimestre

    def ejecutar(self):
        return self.consultor.consultaTutoriasClase(self.nombre, self.cuatrimestre, self.grado, self.curso, self.grupo)


class CommandProfesor(Command):
    apellido = None
    apellido2 = None

    def __init__(self, nombre, apellido, apellido2):
        self.nombre = nombre
        self.apellido = apellido
        self.apellido2 = apellido2

    def ejecutar(self):
        return self.consultor.consultaProfesor(self.nombre, self.apellido2, self.apellido2)


class CommandFichas(Command):

    def __init__(self, grado, curso):
        self.curso = curso
        self.grado = grado

    def ejecutar(self):
        return self.consultor.consultaFichas(self.grado, self.curso)


class CommandFicha(Command):
    def __init__(self, nombre):
        self.nombre = nombre

    def ejecutar(self):
        return self.consultor.consultaFicha(self.nombre)
