import suds

url = 'http://localhost:8080/BMWS/WS?WSDL'
client = suds.client.Client(url)

def prueba():
    respuesta = client.service.consultarGrupos('3','GII')
    print respuesta[0].grado


def consultarGrupos(grado, curso):
    respuesta = client.service.consultarGrupos(grado,curso)

    print respuesta[0].grado


def consultaGrupo(grado, curso, grupo):
    respuesta = client.service.consultarGrupo(grado, curso, grupo)
    return respuesta


def consultaHorario(asignatura, grado, curso, grupo):
    respuesta = client.service.consultarHorariosA(asignatura, grado, curso, grupo)
    return respuesta


def consultaHorarios(grado, curso, grupo):
    respuesta = client.service.consultarHorariosC(grado, curso, grupo)
    return respuesta


def consultaProfesor( nombre, apellido):
    respuesta = client.service.consultarProfesor(nombre, apellido)
    return respuesta


def consultaFicha(nombre):
    respuesta = client.service.consultarFichaDocente(nombre)
    return respuesta


def consultaFichas(grado,curso):
    respuesta = client.service.consultarFichasDocentes(grado, curso)
    return respuesta


def consultaAsignatura(nombre):
    respuesta = client.service.consultarAsignatura(nombre)
    return respuesta


def consultaTutoriasAsignatura(nombre):
    respuesta = client.service.consultarTutoriasA(nombre)
    return respuesta


def consultaTutoriasProfesor(nombre, apellido):
    respuesta = client.service.consultarTutoriasP(nombre, apellido)
    return respuesta


def consultaTutoriasClase(asignatura, cuatrimestre, grado, curso, grupo):
    respuesta = client.service.consultarTutoriasC(asignatura, cuatrimestre, grado, curso, grupo)
    return respuesta


