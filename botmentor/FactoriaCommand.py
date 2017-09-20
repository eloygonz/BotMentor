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
            if len(c) >= 3:
                d = ""
                for i in range(1, len(c)):
                    d = d + ' ' + c[i]
                c2 = d.split(',')
                c2[0] = c2[0][:2].replace(' ', '') + c2[0][2:]
                nombre = c2[0]
                c2[1] = c2[1][:2].replace(' ', '') + c2[1][2:]
                apellidos = c2[1]
                comando = CommandProfesor(nombre, apellidos)
        elif c[0] == '/clase':
            if len(c) >= 5: comando = Command(c[1], c[2], c[3], c[4])
        elif c[0] == '/tutoria':
            if len(c) >= 3:
                d = ""
                for i in range(1, len(c)):
                    d = d + ' ' + c[i]
                c2 = d.split(',')
                c2[0] = c2[0][:2].replace(' ', '') + c2[0][2:]
                nombre = c2[0]
                c2[1] = c2[1][:2].replace(' ', '') + c2[1][2:]
                apellidos = c2[1]
                comando = CommandTutoriaProfesor(nombre,apellidos)

        return comando
        """          
        elif c[0] == '/tutoria':
            if len(c) >= 5: comando = CommandTutoriaClase(c[1], c[2], c[3], c[4])
        elif c[0] == '/tutoria':
            if len(c) >= 2: comando = CommandTutoriaAsignatura(c[1])
   """