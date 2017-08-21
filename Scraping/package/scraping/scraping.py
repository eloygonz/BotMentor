# -*- coding: utf-8 -*-
__author__ = 'PedroSanchez y EloyGonzalez'

from bs4 import BeautifulSoup
import requests


class Scraping:
    """ docstring for Scraping
        Clase para hacer scraping de la 
        facultad de informatica
    """
    #url = "https://web.fdi.ucm.es/Docencia/Horarios.aspx?fdicurso=2016&CodCurso=42&grupo=B&tipo=0"

    #Constructor
    def __init__(self):
        
        super(Scraping, self).__init__()

    #Metodo que hace scraping a las tablas horarios
    def scrapTutorias(self):
        #url = "http://informatica.ucm.es/informatica/profesores-y-tutorias";
        
        url = "https://web.fdi.ucm.es/alumnos/Tutorias.asp?doc=S&fdicurso=2016-2017"
        # Realizamos la petición a la web
        req = requests.get(url)
        

        # Comprobamos que la petición nos devuelve un Status Code = 200
        statusCode = req.status_code
        if statusCode == 200:
        
            # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()

            html = BeautifulSoup(req.text, "html.parser") 

    

            # Array con las tablas. Cada tabla es de un  grado
            tabla = html.find_all('table') 
                       
            
            tablas = [] # Cada tabla es sector de la infraestructura de los profesores (Sistemas Informáticos y Computación)

            cuaTuto = {"1t":[],"2t":[]} # Objeto con 1 y 2 cuatrimestre  para tutorias
            cua = {"1c":[],"2c":[]} # Objeto con 1 y 2 cuatrimestre  para el curso en general
            graDir = dict() # Diccionario con que tendra las aulas {"(803336-GS-3ºE)": {"1-Aula 1": [LX:09-09:50, 10-10:50]}}
            aulDir = dict() # Diccionario con que tendra las aulas {"1-Aula 1": [LX:09-09:50, 10-10:50]}
            antAul = "" # ID aula "1-Aula 1"
            antHor = [] # [LX:09-09:50, 10-10:50]
            tut = []  # Array tutorias []        
            hor = []  # Array horario []

            
            idGra = ""
            finds = False;
            finCu1 = False;
            finCu2 = False;

            '''
                Tablas --> Matriz --> lista [nombre, email, telefono, despacho, graDir {...}]
            '''

            n = "1c"
            # Sacamos una matriz con las filas y columnas de las tablas y las metemos en un array de tablas
            for t,tab in enumerate(tabla):
                
                matriz = [] # Matriz con la tabla correpondiente a cada sector (filas)

                #find_all saca un array con todos los tr encontrados
                trs = tab.find_all('tr')
                
                #Recorro filas
                for f,tr in enumerate(trs):
                    
                    matriz.append([])

                    #find_all saca un array con todos los td encontrados
                    tds = tr.find_all('td')
            
                    lista = [] # Lista que compone las columnas de cada tabla
                    
                    #Recorro columnas 
                    for c,td in enumerate(tds):
                        
                        #find_all saca un array con solo el texto (text = True) del td 
                        p = td.find_all(text=True);

                        #Recorro varias columnas
                        for cont,s in enumerate(p):

                            if(s == "PROFESORES_TXT"):
                                '''
                                Inicializacion de los atributos a usar, 
                                ya que siempre se empiza con un profesor nuevo
                                '''
                                tut = []
                                hor = []
                                cua = {"1c":[],"2c":[]}
                                cuaTuto = {"1t":[],"2t":[]}
                                graDir = dict()
                                aulDir = dict()
                                contAl = 0

                                n = "1c"
                                finCu1 = False;
                                finCu2 = False;

                                #Se añade el profesor
                                lista.append(p[len(p)-1]) 

                            elif s == "EMAIL_TXT":
                                #find para sacar enlace de la imgaen y split para texto
                                im = td.find('image');
                                a = im['src'].split('=')
                                if len(a) > 0:
                                    lista.append(a[1])

                            elif s == "TELEFONO_TXT":
                                
                                lista.append(p[len(p)-1])
                            elif s == "Prof_Lugar_TXT":
                                
                                lista.append(p[len(p)-1])

                            elif '->' in s: # Si contiene una "->" "tutoria"
                                tut.append(s)
                                
                            elif '(' in s: # Si contiene una "(" Asignatura
                                '''
                                Dicionario donde se metera el las aulas o lab 
                                correpondientes a la asignatura concreta
                                '''
                                aulDir = dict()
                                graDir[s] = aulDir;
                                idGra = s;
                                finds = True;

                            elif 'Aula' in s  or 'Lab' in s: # Si contiene una aula o lab
                                
                                hor = []
                                '''
                                str transforma dato en cadena (1-Aula 14) 
                                Esto lo hago porque las aulas y lab se repiten 
                                y por lo tanto se pisan en el diccionario
                                '''
                                antAul = str(contAl)+"-"+s
                                
                                aulDir[antAul] = antHor;
                                
                                contAl = contAl +1

                                graDir[idGra] = aulDir;
                                
                                #print("c: ",cont, " aula ", s)
                            elif ':' in s: # Si contiene un :  para horarios
                                
                                hor.append(s)
                                antHor = hor
                                aulDir[antAul] = antHor;
                                #print("c: ",cont," hoara ", s)

                            if ('2º Cuatr.' in s) :
                                n = "2c"
                                graDir = dict()
                                aul = []
                                hor = []
                            elif '1º Cuatr.' in s:
                                n = "1c"
                                graDir = dict()
                                aul = []
                                hor = []

                    if len(graDir) > 0 and finds:
                        
                        if n == "1c":
                            cua["1c"] = graDir;
                            if not  finCu1:
                                cuaTuto["1t"] = tut;
                                tut = []
                                finCu1 = True;
                                finCu2 = False;
                        elif n == "2c" :
                            cua["2c"] = graDir;
                            if not  finCu2:
                                cuaTuto["2t"] = tut;
                                tut = []
                                finCu1 = False;
                                finCu2 = True;

                        finds = False;
                        #print(gra)

                    if(len(lista) > 1):
                        
                        lista.append(cua)
                        lista.append(cuaTuto)
                        matriz[f].append(lista)
                        
                        #print(lista)
                        
                tablas.append(matriz)


            '''
            for t in tablas:
                for f in t:
                    for c in f:
                        print(c)
            '''

            return tablas;
           

        else:
            print ("Status Code", statusCode)
            


    def scrapAsignaturas(self):

        url = "https://informatica.ucm.es/listado-de-asignaturas-2016-2017";
        # Realizamos la petición a la web
        req = requests.get(url)
            
        # Comprobamos que la petición nos devuelve un Status Code = 200
        statusCode = req.status_code
        if statusCode == 200:
                
            tablas = []

            # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
                
            #html = BeautifulSoup(req.text)
               

            html = BeautifulSoup(req.text, "html.parser") 

            #vemos lo que ha optenido

            # Array con las tablas. Cada tabla es de un  grado
            tabla = html.find_all('table') 

            # Sacamos una matriz con las filas y columnas de las tablas y las metemos en un array de tablas
            for t,tab in enumerate(tabla):
                    
                matriz = []

                trs = tab.find_all('tr')
                  
                for f,tr in enumerate(trs):
                        
                    matriz.append([])
                    tds = tr.find_all('td')
                        
                    for c,td in enumerate(tds):
                            
                        p = td.find('p')
                        a = p.find('a')
                            
                        if a != None:
                            #Sacamos los grados
                            matriz[f].append(a['name'])
                        else:
                            matriz[f].append(p)
                       
                tablas.append(matriz)
                '''
                for t in tablas:

                    for f in t:
                        
                        for c in f:

                            print(c.getText());
                '''
            return tablas;

        else:
            print ("Status Code", statusCode)

    def scrapCursos(self):

        url = "https://web.fdi.ucm.es/alumnos/info_grupos.asp?cod=1&fdicurso=2016-2017";
        # Realizamos la petición a la web
        req = requests.get(url)
            
        # Comprobamos que la petición nos devuelve un Status Code = 200
        statusCode = req.status_code
        if statusCode == 200:
                
   
            cursos = dict()
            # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()

            html = BeautifulSoup(req.text, "html.parser") 

            #vemos lo que ha optenido

            # Array con las tablas. Cada tabla es de un  grado
            li = html.find_all('li') 

            # Sacamos una matriz con las filas y columnas de las tablas y las metemos en un array de tablas
                   
            
            key = ''
            for t, l in enumerate(li):

                p = l.find(text=True);
                        
                if ('GRADO' in p ) or ('INFORMÁTICA' in p): 

                    key = p
                    array = []
                else:
                    array.append(p);   
                    cursos[key] = array;
                    
            
            return cursos;                               

        else:
            print ("Status Code", statusCode)


    def scrapInformacionDocente(self):

        url = "http://informatica.ucm.es/informatica/informacion-docente";
        # Realizamos la petición a la web
        req = requests.get(url)
            
        # Comprobamos que la petición nos devuelve un Status Code = 200
        statusCode = req.status_code
        if statusCode == 200:
                
   
            # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
              
            html = BeautifulSoup(req.text, "html.parser") 

            a = html.find_all('a') 
           
            links = []
            ficha = dict()
            for ar in a:

                p = ar.find(text=True);
               
                if "Fichas docentes del curso 2016/2017" == p:
                    links.append(ar['href'])
                    
            for l in links:

                self.scrapFichasDocentes(l, ficha)

            return(ficha)

        else:
            print ("Status Code", statusCode)



    def scrapFichasDocentes(self, url, fichaALL):

        #url = "http://informatica.ucm.es/informatica/informacion-docente";
        # Realizamos la petición a la web
        req = requests.get(url)
            
        # Comprobamos que la petición nos devuelve un Status Code = 200
        statusCode = req.status_code
        if statusCode == 200:
                
            ficha = dict()
            # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
                
            html = BeautifulSoup(req.text, "html.parser") 

            td = html.find_all('td')

            ax = html.find_all('a')
            #print(tabla)

            key = ''
            keyALL =''
            for t in td:
                tex = t.find(text= True)
                
                if (None != tex and 'GRADO' in tex) or (None != tex and 'MÁSTER' in tex):
                    keyALL = tex
                            
                elif None != tex and 'CURSO' in tex:
                    key = tex
                    array = []
                else:

                    a = t.find('a')

                    if None != a and 'Guias_Docentes' not in a['href']:
                        p=a.find(text = True)
                        
                        objeto = p, a['href']
                        array.append(objeto)
                        ficha[key] = array

            fichaALL[keyALL]=ficha
                            

        else:
            print ("Status Code", statusCode)

