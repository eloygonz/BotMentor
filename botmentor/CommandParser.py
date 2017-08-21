# coding=utf-8
from Consultor import *
from Commands import Command
def numCurso(self, grado):
    if grado == 'MII':
        cursos = 2
    elif grado == 'DV':
        cursos = 3
    elif grado == 'OP':
        cursos = 0
    else:
        cursos = 4
    return cursos



def parseGrupo(self,command):
    res = consultaGrupo(command.curso, command.grado, command.grupo)
    if res:
        return True
    else:
        return False

def existeAsignatura(self, nombre):
    return True


def existeProfesor(nombre, apellido):
    return True


def parseCommand(self, command):
    # type: (object, object) -> object
    listaComandosCompletos = ['/horarios', '/fichas']
    listaComandosSimples = ['ayuda', '/start']
    listaComandosEspecificos = ['/horario', '/tutoria', '/clase']
    listaGrados = ['GII', 'GIS', 'GIC', 'GDV', 'II', 'MII', 'DGMI']
    if command.com in listaComandosCompletos:
        if command.grado != None and command.grado in listaGrados:
            if command.curso != None and numCurso(self,command.grado) >= command.curso and command.curso >= 0:
                if parseGrupo(self,command):
                    return True
    elif command.com in listaComandosSimples:
                return True
    elif command.com in listaComandosEspecificos:
        if command.grado != None and command.grado in listaGrados:
            if command.curso != None and numCurso(self, command.grado) >= command.curso and command.curso >= 0:
                if parseGrupo(self, command):
                    return existeAsignatura(self, command.nombre)
    elif command.com == '/profesor' and command.nombre != None and command.apellido != None and command.apellido2 != None:
        return existeProfesor(command.nombre, command.apellido)
    elif command.com == '/ficha' and  command.nombre != None:
        return existeAsignatura(self, command.nombre)
