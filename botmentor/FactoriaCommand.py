from Commands import *


class FactoriaCommand:
    @staticmethod
    def creaComando(c):
        comando = Command
        if c[0] == '/horarios':
            if len(c) >= 4: comando = CommandHorarios(c[1], c[2], c[3])
        elif c[0] == '/horario':
            if len(c) >= 5: comando = CommandHorario(c[1], c[2], c[3], c[4])
        elif c[0] == '/ficha':
            if len(c) >= 2: comando = CommandFicha(c[1])
        elif c[0] == '/fichas':
            if len(c) >= 4: comando = CommandFichas(c[1],c[2])
        elif c[0] == '/profesor':
            if len(c) >= 3: comando = CommandProfesor(c[1], c[2], c[3])
        elif c[0] == '/clase':
            if len(c) >= 5: comando = Command(c[1], c[2], c[3], c[4])
        elif c[0] == '/tutoria':
            if len(c) >= 5: comando = CommandTutoriaClase(c[1], c[2], c[3], c[4])
        elif c[0] == '/tutoria':
            if len(c) >= 2: comando = CommandTutoriaAsignatura(c[1])
        elif c[0] == '/tutoria':
            if len(c) >= 3: comando = CommandTutoriaProfesor(c[1], c[2], c[3])

        return comando
