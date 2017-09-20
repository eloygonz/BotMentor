from abc import ABCMeta, abstractmethod
from consultor import *


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
        elif self.com == '/profesor' or self.com == '/tutoria':
            d = ""
            for i in range(1,len(c)):
                d = d + ' ' + c[i]
            c2 = d.split(',')
            c2[0] = c2[0][:2].replace(' ', '') + c2[0][2:]
            self.nombre = c2[0]
            c2[1] = c2[1][:2].replace(' ', '') + c2[1][2:]
            self.apellido = c2[1]
        elif len(c) == 4 and not(self.com == '/profesor' or self.com == '/tutoria'):
            self.grado = c[1]
            self.curso = c[2]
            self.grupo = c[3]
        elif len(c) == 5:
            self.grado = c[1]
            self.curso = c[2]
            self.grupo = c[3]
            self.nombre = c[4]

    @classmethod
    def numCurso(self):
        if self.grado == 'MII':
            cursos = 2
        elif self.grado == 'GDV':
            cursos = 3
        elif self.grado == 'OP':
            cursos = 0
        else:
            cursos = 4
        return cursos

    @classmethod
    def parseGrupo(self):
        res = consultaGrupo(self.grado, self.curso, self.grupo)
        if res.id != -1:
            return True
        else:
            return False

    @classmethod
    def existeAsignatura(self, nombre):
        res = consultaAsignatura(nombre)
        if res.id > 0:
            return True
        else:
            return False
    @classmethod
    def existeProfesor(self, nombre, apellido):
        res = consultaProfesor(nombre,apellido)
        if res.id > 0:
            return True
        else:
            return False

    @classmethod
    def parseCommand(self):
        # type: (object, object) -> object
        listaComandosCompletos = ['/horarios', '/fichas']
        listaComandosSimples = ['ayuda', '/start']
        listaComandosEspecificos = ['/horario', '/clase']
        listaGrados = ['GII', 'GIS', 'GIC', 'GDV', 'II', 'MII', 'DGMI']
        if self.com in listaComandosCompletos:
            if self.grado is not None and self.grado in listaGrados:
                if self.curso is not None and self.numCurso() >= int(self.curso) and int(self.curso) >= 0:
                    return self.parseGrupo
        elif self.com in listaComandosSimples:
            return True
        elif self.com in listaComandosEspecificos:
            if self.grado is not None and self.grado in listaGrados:
                if self.curso is not None and self.numCurso() >= int(self.curso) and int(self.curso) >= 0:
                    return self.parseGrupo() and self.existeAsignatura(self.nombre)
        elif (self.com == '/profesor' or self.com =='/tutoria') and self.nombre is not None and self.apellido is not None:

            return self.existeProfesor(self.nombre, self.apellido)
        elif self.com == '/ficha' and self.nombre is not None:
            return self.existeAsignatura(self.nombre)

    @abstractmethod
    def estaListo(self): raise NotImplementedError

    @abstractmethod
    def ejecutar(self): raise NotImplementedError


class CommandHorarios(Command):

    def __init__(self, grado, curso, grupo, asignatura=None):
        self.grado = grado
        self.curso = curso
        self.grupo = grupo

    def ejecutar(self):
        return consultaHorarios(self.grado, self.curso, self.grupo)
    def estaListo(self):
        if self.grado is not None and self.curso is not None and self.grupo is not None:
            return True
        else:
            return False
class CommandHorario(Command):

    def __init__(self, grado, curso, grupo, asignatura):
        self.grado = grado
        self.curso = curso
        self.grupo = grupo
        self.nombre = asignatura

    def ejecutar(self):
 # Horario de una asignatura concreta
        return consultaHorario(self.nombre, self.grado, self.curso, self.grupo)
    def estaListo(self):
        if self.grado is not None and self.curso is not None and self.grupo is not None and self.nombre is not None:
            return True
        else:
            return False

class CommandTutoriaAsignatura(Command):

    def __init__(self,asignatura ):
        self.nombre = asignatura

    def ejecutar(self):

        return consultaTutoriasAsignatura(self.nombre)

    def estaListo(self):
        if self.nombre is not None:
            return True
        else:
            return False

class CommandTutoriaProfesor(Command):
    apellido = None

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def ejecutar(self):
        return consultaTutoriasProfesor(self.nombre, self.apellido)


    def estaListo(self):
        if self.nombre is not None and self.apellido is not None:
            return True
        else:
            return False


class CommandTutoriaClase(Command):
    cuatrimestre = None

    def __init__(self, grado, curso, grupo, cuatrimestre, asignatura):
        self.grado = grado
        self.curso = curso
        self.grupo = grupo
        self.nombre = asignatura
        self.cuatrimestre = cuatrimestre

    def ejecutar(self):
        return consultaTutoriasClase(self.nombre, self.cuatrimestre, self.grado, self.curso, self.grupo)

    def estaListo(self):
        if self.grado is not None and self.curso is not None and self.grupo is not None and self.nombre is not None and self.cuatrimestre is not None:
            return True
        else:
            return False

class CommandProfesor(Command):
    apellido = None

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def ejecutar(self):
        return consultaProfesor(self.nombre, self.apellido)

    def estaListo(self):
        if self.nombre is not None and self.apellido is not None:
            return True
        else:
            return False


class CommandFichas(Command):

    def __init__(self, grado, curso):
        self.curso = curso
        self.grado = grado

    def ejecutar(self):
        return consultaFichas(self.grado, self.curso)

    def estaListo(self):
        if self.grado is not None and self.curso is not None:
            return True
        else:
            return False


class CommandFicha(Command):
    def __init__(self, nombre):
        self.nombre = nombre

    def ejecutar(self):
        return consultaFicha(self.nombre)

    def estaListo(self):
        if self.nombre is not None:
            return True
        else:
            return False

class CommandStart(Command):
    def __init__(self, nombre):
        self.nombre = nombre

    def ejecutar(self):
        return consultaFicha(self.nombre)

    def estaListo(self):
        if self.nombre is not None:
            return True
        else:
            return False


class CommandVolver(Command):
    def __init__(self, nombre):
        self.com = nombre

    def ejecutar(self):

        return consultaFicha(self.nombre)

    def estaListo(self):
        if self.nombre is not None:
            return True
        else:
            return False


class CommandMenu(Command):
    def __init__(self, nombre):
        self.nombre = nombre

    def ejecutar(self):
        return consultaFicha(self.nombre)

    def estaListo(self):
        if self.nombre is not None:
            return True
        else:
            return False
