# -*- coding: utf-8 -*-
__author__ = 'PedroSanchez y EloyGonzalez'

from bs4 import BeautifulSoup
import requests


class ScraTutorias:
    """ docstring for ScraTutorias
        Clase para hacer scraping en Tutorias
    """
    #url = "https://web.fdi.ucm.es/Docencia/Horarios.aspx?fdicurso=2016&CodCurso=42&grupo=B&tipo=0"

    #Constructor
    def __init__(self):
        
        super(ScraTutorias, self).__init__()

    #Metodo que hace scraping a las tablas horarios
    def scrap(self):
        #url = "http://informatica.ucm.es/informatica/profesores-y-tutorias";
        
        url = "https://web.fdi.ucm.es/alumnos/Tutorias.asp?doc=S&fdicurso=2016-2017"
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
            
            #tabla = div.find_all('table') 

            
            
            tut = []
          
            aul = []
            hor = []
            cua = {"1c":[],"2c":[]}
            cuaTuto = {"1t":[],"2t":[]}

            graDir = dict()
            graAli = ""
            finds = False;
            finCu1 = False;
            finCu2 = False;

            n = "1c"
            # Sacamos una matriz con las filas y columnas de las tablas y las metemos en un array de tablas
            for t,tab in enumerate(tabla):
                
                matriz = []

                trs = tab.find_all('tr')
                
                #Recorro filas
                for f,tr in enumerate(trs):
                    
                    matriz.append([])
                    tds = tr.find_all('td')
            
                    lista = []
                    
                    #Recorro columnas 
                    for c,td in enumerate(tds):
                        
                        
                        p = td.find_all(text=True);
                        #print(p)
                        #Recorro varias columnas
                        for cont,s in enumerate(p):

                            #print(s)
                            if(s == "PROFESORES_TXT"):
                                tut = []
                                aul = []
                                hor = []

                                cua = {"1c":[],"2c":[]}
                                cuaTuto = {"1t":[],"2t":[]}
                                graDir = dict()

                                n = "1c"
                                finCu1 = False;
                                finCu2 = False;

                                lista.append(p[len(p)-1])
                            elif s == "EMAIL_TXT":
                                im = td.find('image');
                                a =im['src'].split('=')
                                if len(a) > 0:
                                    lista.append(a[1])
                            elif s == "TELEFONO_TXT":
                                
                                lista.append(p[len(p)-1])
                            elif s == "Prof_Lugar_TXT":
                                
                                lista.append(p[len(p)-1])

                            elif '->' in s:
                                tut.append(s)
                                
                            elif '(' in s:
                                aul = []
                                graDir[s] = aul;
                                graAli = s;
                                finds = True;
                            elif 'Aula' in s  or 'Lab' in s:
                                hor = []
                                aul.append(s)
                                graDir[graAli] = aul;
                                #print("c: ",cont, " aula ", s)
                            elif ':' in s:
                                hor = []
                                hor.append(s)
                                aul.append(hor)  
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


            
            for t in tablas:
                for f in t:
                    for c in f:
                        print(c)
            

            return tablas;
           

        else:
            print ("Status Code", statusCode)
            

