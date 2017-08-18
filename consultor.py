import suds
def prueba():
    url = 'http://localhost:8080/BMWS/WS?WSDL'
    client = suds.client.Client(url)
    respuesta = client.service.consultarGrupos('GRADO EN INGENIERIA DE SOFTWARE','3')
    print respuesta
