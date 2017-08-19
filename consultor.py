import suds
def prueba():
    url = 'http://localhost:8080/BMWS/WS?WSDL'
    client = suds.client.Client(url)
    respuesta = client.service.consultarGrupos('3','GII')
    print respuesta[0].grado

def consultarGrupos(grado, curso):
    url = 'http://localhost:8080/BMWS/WS?WSDL'
    client = suds.client.Client(url)
    respuesta = client.service.consultarGrupos(grado,curso)

    print respuesta[0].grado

def consultaGrupo(grado, curso, grupo):
    url = 'http://localhost:8080/BMWS/WS?WSDL'
    client = suds.client.Client(url)
    respuesta = client.service.consultarGrupo(grado, curso, grupo)
    print respuesta

def consultaHorarios(grado, curso, grupo):
    url = 'http://localhost:8080/BMWS/WS?WSDL'
    client = suds.client.Client(url)
    respuesta = client.service.consultarGrupo(grado, curso, grupo)
    print respuesta

def consultaProfesor(nombre, apellido):
    url = 'http://localhost:8080/BMWS/WS?WSDL'
    client = suds.client.Client(url)
    respuesta = client.service.consultarProfesor(apellido+', '+ nombre)
    print respuesta

def consultaFicha(nombre):
    url = 'http://localhost:8080/BMWS/WS?WSDL'
    client = suds.client.Client(url)
    respuesta = client.service.consultarFichaDocente(nombre)
    print respuesta

def consultaFichas(grado, curso):
    url = 'http://localhost:8080/BMWS/WS?WSDL'
    client = suds.client.Client(url)
    respuesta = client.service.consultarFichasDocentes(grado, curso)
    print respuesta

def consultaAsignatura(nombre):
    url = 'http://localhost:8080/BMWS/WS?WSDL'
    client = suds.client.Client(url)
    respuesta = client.service.consultarAsignatura(nombre)
    print respuesta

def consultaTutoriasAsignatura(nombre):
    url = 'http://localhost:8080/BMWS/WS?WSDL'
    client = suds.client.Client(url)
    respuesta = client.service.consultarTutoriasA(nombre)
    print respuesta

def consultaTutoriasProfesor(nombre, apellido):
    url = 'http://localhost:8080/BMWS/WS?WSDL'
    client = suds.client.Client(url)
    respuesta = client.service.consultarTutoriasP(apellido + ', ' + nombre)
    print respuesta

def consultaTutoriasClase(asignatura, cuatrimestre, grado, curso, grupo):
    url = 'http://localhost:8080/BMWS/WS?WSDL'
    client = suds.client.Client(url)
    respuesta = client.service.consultarTutoriasC(asignatura, cuatrimestre, grado, curso, grupo)
    print respuesta

