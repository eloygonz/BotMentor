from abc import ABCMeta, abstractmethod
from Consultor import *


class Command():
    listo = False
    com = None
    grado = None
    curso = None
    grupo = None
    nombre = None
    apellido = None
    apellido2 = None
    _metaclass_ = ABCMeta

    @classmethod
    def __init__(self,c):
        self.com = c[0]
        if len(c) == 2:
            self.nombre = c[1]
        elif len(c) == 4 and (self.com == '/profesor' or self.com == 'tutoria'):
            self.nombre = c[1]
            self.apellido = c[2]
            self.apellido2 = c[3]
        elif len(c) == 4 and not(self.com == '/profesor' or self.com == 'tutoria'):
            self.grado = c[1]
            self.curso = c[2]
            self.grupo = c[3]
        elif len(c) == 5:
            self.grado = c[1]
            self.curso = c[2]
            self.grupo = c[3]
            self.nombre = c[4]


    @classmethod
    def estaListo(self):
        return True

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
            return consultaHorarios(self.nombre, self.grado, self.curso, self.grupo)
        elif self.nombre == None:  # Horario de un curso completo
           return consultaHorarios(self.grado, self.curso, self.grupo)


class CommandTutoriaAsignatura(Command):

    def __init__(self,asignatura ):
        self.nombre = asignatura

    def ejecutar(self):

        return consultaTutoriasAsignatura(self.nombre)


class CommandTutoriaProfesor(Command):
    apellido = None
    apellido2 = None

    def __init__(self, nombre, apellido, apellido2):
        self.nombre = nombre
        self.apellido = apellido
        self.apellido2 = apellido2

    def ejecutar(self):
        return consultaTutoriasProfesor(self.nombre, self.apellido, self.apellido2)


class CommandTutoriaClase(Command):
    cuatrimestre = None

    def __init__(self, grado, curso, grupo, cuatrimestre, asignatura=None):
        self.grado = grado
        self.curso = curso
        self.grupo = grupo
        self.nombre = asignatura
        self.cuatrimestre = cuatrimestre

    def ejecutar(self):
        return consultaTutoriasClase(self.nombre, self.cuatrimestre, self.grado, self.curso, self.grupo)


class CommandProfesor(Command):
    apellido = None
    apellido2 = None

    def __init__(self, nombre, apellido, apellido2):
        self.nombre = nombre
        self.apellido = apellido
        self.apellido2 = apellido2

    def ejecutar(self):
        return consultaProfesor(self.nombre, self.apellido, self.apellido2)


class CommandFichas(Command):

    def __init__(self, grado, curso):
        self.curso = curso
        self.grado = grado

    def ejecutar(self):
        return consultaFichas(self.grado, self.curso)


class CommandFicha(Command):
    def __init__(self, nombre):
        self.nombre = nombre

    def ejecutar(self):
        return consultaFicha(self.nombre)
