import suds
def prueba():
    url = 'http://localhost:8080/BMWS/WS?WSDL'
    client = suds.client.Client(url)
    respuesta = client.service.consultarGrupos('3','GII')

    print respuesta[0].grado

def consultaGrupo(grado, curso, grupo):
    url = 'http://localhost:8080/BMWS/WS?WSDL'
    client = suds.client.Client(url)
    respuesta = client.service.consultarGrupos(curso, grado, grupo)
    print respuesta
