import suds
class Consultor:
    def __init__(self):
        url = 'http://localhost:8080/BMWS/WS?WSDL'
        client = suds.client.Client(url)


    def prueba(self):
        respuesta = self.client.service.consultarGrupos('3','GII')
        print respuesta[0].grado


    def consultarGrupos(self,grado, curso):
        respuesta = self.client.service.consultarGrupos(grado,curso)

        print respuesta[0].grado


    def consultaGrupo(self,grado, curso, grupo):
        respuesta = self.client.service.consultarGrupo(grado, curso, grupo)
        print respuesta


    def consultaHorarios(self, grado, curso, grupo):
        respuesta = self.client.service.consultarGrupo(grado, curso, grupo)
        print respuesta


    def consultaProfesor(self, nombre, apellido, apellido2):
        respuesta = self.client.service.consultarProfesor(apellido + ' ' + apellido2 + ', ' + nombre)
        print respuesta


    def consultaFicha(self, nombre):
        respuesta = self.client.service.consultarFichaDocente(nombre)
        print respuesta


    def consultaFichas(self, grado,curso):
        respuesta = self.client.service.consultarFichasDocentes(grado, curso)
        print respuesta


    def consultaAsignatura(self,nombre):
        respuesta = self.client.service.consultarAsignatura(nombre)
        print respuesta


    def consultaTutoriasAsignatura(self,nombre):
        respuesta = self.client.service.consultarTutoriasA(nombre)
        print respuesta


    def consultaTutoriasProfesor(self,nombre, apellido, apellido2):
        respuesta = self.client.service.consultarTutoriasP(apellido + " " + apellido2 + ", " + nombre)
        print respuesta


    def consultaTutoriasClase(self,asignatura, cuatrimestre, grado, curso, grupo):
        respuesta = self.client.service.consultarTutoriasC(asignatura, cuatrimestre, grado, curso, grupo)
        print respuesta


