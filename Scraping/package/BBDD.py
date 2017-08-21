import sqlite3 as dbapi  

class DBHorarios:
    """ docstring for DBHorarios
        Clase para hacer scraping en Horarios
    """
    #url = "https://web.fdi.ucm.es/Docencia/Horarios.aspx?fdicurso=2016&CodCurso=42&grupo=B&tipo=0"

    c = 0
    #Constructor
    def __init__(self):
        
        super(DBHorarios, self).__init__()

        self.db = dbapi.connect("db.dat")
       


    #Metodo que hace scraping a las tablas horarios
    def selectAsignaturas(self):

    	cursor = self.db.cursor();
    	

    	#cursor.execute("""insert into horarios values (3, 'GIS2', 'segundo', 'fp', '2017-03-17', 8, 10)""")

    	#self.db.commit()

    	#cursor.execute("""select * from horarios where curso = 'GIS2' """)  
    	cursor.execute("""select * from asignaturas""")  
        
    	for tupla in cursor.fetchall():
    		print (tupla)  

    def selectCursos(self):

        cursor = self.db.cursor();
        

        #cursor.execute("""insert into horarios values (3, 'GIS2', 'segundo', 'fp', '2017-03-17', 8, 10)""")

        #self.db.commit()

        #cursor.execute("""select * from horarios where curso = 'GIS2' """)  
        cursor.execute("""select * from Cursos where grado='GII' and curso=3 and grupo='A'""")  
        
        for tupla in cursor.fetchall():
            print (tupla) 



    def selectHorarios(self):

        cursor = self.db.cursor();
        

        #cursor.execute("""insert into horarios values (3, 'GIS2', 'segundo', 'fp', '2017-03-17', 8, 10)""")

        self.db.commit()

        #cursor.execute("""select * from horarios where curso = 'GIS2' """)  
        cursor.execute("""select * from horarios""")  
        
        for tupla in cursor.fetchall():
            print (tupla)

    def insertarFichasDocentes(self, tablas):

        cursor = self.db.cursor();

        reg = ()
        grado = ''
        curso = ''
       
        cont = 0;
        for key, value in tablas.items():


            if 'MÁSTER INGENIERÍA INFORMÁTICA (Máster)' == key:
                grado = 'MII'
            elif 'GRADO EN INGENIERÍA DE COMPUTADORES (Grados)' == key:
                grado = 'GIC'
            elif 'GRADO EN INGENIERÍA INFORMÁTICA (Grados)' == key:
                grado = 'GII'
            elif 'GRADO EN INGENIERÍA DEL SOFTWARE (Grados)' == key:
                grado = 'GIS'
            elif 'GRADO EN DESARROLLO DE VIDEOJUEGOS (Grados)' == key:
                grado = 'GDV'
            elif 'DOBLE GRADO DE MATEMÁTICAS E INFORMÁTICA (Grados)' == key:
                grado = 'DGMI'

            for k, v in value.items():

                if 'PRIMER CURSO' == k:
                    curso = '1'
                elif 'SEGUNDO CURSO' == k:
                    curso = '2'
                elif 'TERCER CURSO' == k:
                    curso = '3'
                elif 'CUARTO CURSO' == k:
                    curso = '4'
                elif 'OPTATIVAS DE TERCER Y CUARTO CURSO' == k:
                    curso = "3-4"

                #req = (id_ficha, grado, curso, id_asignatura, asignatura, documento)
                
                for q in v:

                    aux = q[0].split("-")
                    id_asignatura = aux[0].strip()

                    if len(aux) > 2:
                        asignatura = aux[1]+"-"+aux[2]
                    elif len(aux) == 2:
                        asignatura = aux[1]
                    
                    documento = q[1]

                    reg = (cont, grado, curso, id_asignatura, asignatura.strip(), documento)
                    
                    
                    cursor.execute("INSERT INTO Fichas VALUES (?,?,?,?,?,?)", reg)

                    cont = cont + 1

                
        self.db.commit()

    def insertarCursos(self, tablas):

        cursor = self.db.cursor();

        reg = ()
        
       
        cont = 0;
        for key, value in tablas.items():

            keyX = ''

            if 'INGENIERO EN INFORMÁTICA' == key:
                keyX = 'II'
            elif 'MÁSTER INGENIERÍA INFORMÁTICA' == key:
                keyX = 'MII'
            elif 'GRADO EN INGENIERÍA DE COMPUTADORES' == key:
                keyX = 'GIC'
            elif 'GRADO EN INGENIERÍA INFORMÁTICA' == key:
                keyX = 'GII'
            elif 'GRADO EN INGENIERÍA DEL SOFTWARE' == key:
                keyX = 'GIS'
            elif 'GRADO EN DESARROLLO DE VIDEOJUEGOS' == key:
                keyX = 'GDV'
            elif 'DOBLE GRADO DE MATEMÁTICAS E INFORMÁTICA' == key:
                keyX = 'DGMI'

            for v  in value:
                #req = (id_curso, grado, curso, grupo)
                    
                if ('Optativas' in v ):
                    lista = v.split('Optativas')
                    reg = (cont, keyX, 0, lista[len(lista)-1].strip())
        
                else:

                    lista = v.split('º')
                   
                    reg = (cont, keyX, lista[0], lista[1].strip())

                cursor.execute("INSERT INTO Cursos VALUES (?,?,?,?)", reg)
                cont = cont + 1

                
        self.db.commit()


    def insertarAsignaturas(self, tablas):

        cursor = self.db.cursor();

        reg = ()
        
       

        for t in tablas:

            for f in t:
                
                if len(f) == 1:
                    
                    grado =  f[0];##Aqui puedo sacar los grados 

                if len(f) == 3:
                    
                    
                    if (f[2].getText() != 'Cod_Gea') and (f[2].getText() != '\xa0'):
                        a  = int(f[2].getText())
                        
                        reg = (a, grado, f[0].getText(), f[1].getText())
                       
                        cursor.execute("INSERT INTO Asignaturas VALUES (?,?,?,?)", reg)
                    

        self.db.commit()

    def insertarScrapingBBDD(self, tablas):

        cursor = self.db.cursor();

        reg = ()
        
        cont = 0;
        n = 0;

        for t in tablas:
            for f in t:
                for c in f:
                    #req = ("id_profesor", "nombre", "apellidos", "correo","telefono", "despacho")
                    
                    if(len(c) == 6):

                        aux = c[0].split(",")

                        reg = (cont, aux[1].strip(), aux[0].strip(), c[1].strip(), c[2].strip(), c[3].strip())
                        
                        n = self.insertarClasesBBDD(c[4], cont, n, cursor)

                        
                        self.insertarTutoriasBBDD(c[5], cont, cursor)
                    else:

                        aux = c[0].split(",")

                        reg = (cont, aux[1].strip(), aux[0].strip(), c[1].strip(), c[2].strip(), " ")
                    
                        n = self.insertarClasesBBDD(c[3], cont, n, cursor)
                        
                        self.insertarTutoriasBBDD(c[4], cont, cursor)

                 
                    cursor.execute("INSERT INTO profesores VALUES (?,?,?,?,?,?)", reg)
    
                    cont = cont + 1

        self.db.commit()            

    def insertarClasesBBDD(self, h, id_profesor, cont, cursor):
        curso=" "
        grupo=" "
        grado=" "
        n = 0;
        if len(h['1c']) > 0:
            cua1 = h['1c']
            
            for k, v in cua1.items():
            
                lista = k.split('(');
                lista = lista[1].split(')')
                lista = lista[0].split('-')

                id_asignatura = lista[0]

                #req = ("id_clase", id_profesor", id_asignatura "cuatrimestre", "curso", "grupo", "aula", "horario")
                aux = lista[2].split("º")
                if len(aux) == 2:
                    grado = lista[1]
                    if 'opIT4' in aux:
                        curso = '4'
                        grupo = aux[1]
                    elif 'opIT3' in aux:
                        curso = '3'
                        grupo = aux[1]
                    else:
                        curso= aux[0]
                        grupo = aux[1]
                elif len(aux) == 3:
                    curso = '3-4'           
                    grupo = aux[2]  
                    grado = lista[1]  
                
                
                self.insertarAulasHorariosBBDD(v, cont, cursor)

                reg = (cont, id_profesor,  id_asignatura, '1', grado, curso, grupo)              

                cursor.execute("INSERT INTO Clases VALUES (?,?,?,?,?,?,?)", reg)
                
                cont = cont + 1        
                

        if len(h['2c']) > 0:
            cua2 = h['2c']
        
            for k, v in cua2.items():

                lista = k.split('(');
                lista = lista[1].split(')')
                lista = lista[0].split('-')
                
                id_asignatura = lista[0]
                #req = ("id_clase", id_profesor", id_asignatura "cuatrimestre", "curso", "grupo", "aula", "horario") 

                if(len(lista) == 3):

                    aux = lista[2].split("º")
                    if len(aux) == 2:
                        grado = lista[1]
                        if 'opIT4' in aux:
                            curso = '4'
                            grupo = aux[1]
                        elif 'opIT3' in aux:
                            curso = '3'
                            grupo = aux[1]
                        elif 'opt5' in aux:
                            curso = '4'
                            grupo = aux[1]
                        else:
                            curso = aux[0]
                            grupo = aux[1]
                            

                    elif len(aux) == 3:
                        curso = '3-4'
                        grupo = aux[2] 
                        grado = lista[1]              
                
             
                self.insertarAulasHorariosBBDD(v, cont, cursor)

                reg = (cont, id_profesor,  id_asignatura, '2', grado, curso, grupo)
                
                cursor.execute("INSERT INTO Clases VALUES (?,?,?,?,?,?,?)", reg)
    
                cont = cont + 1

        return cont
    
    def insertarAulasHorariosBBDD(self, a, id_clase, cursor):

        for k, v in a.items():

            aula = k.split('-')
            aula = aula[1].strip()
            
            #req = ("id_aulas", id_clase", "Aula_lab", hora)

            for s in v:                
            
                reg = (self.c, id_clase, aula, s)    
                cursor.execute("INSERT INTO Aulas_Horarios VALUES (?,?,?,?)", reg)

                self.c = self.c + 1

    """
    def insertarAulasHorariosBBDD(self, a, id_clase, cursor):

        idA = 0
        cambio = False
        hora = ""
        #print ("idH: ", id_clase, " -> ", a)

        for k, v in a.items():

            au = k.split('-')
            au = au[1].strip()
            
            #reqA = ("id_aulas", id_clase", "Aula_lab")
            regA = (self.c, id_clase, au)
            
            cursor.execute("INSERT INTO Aulas VALUES (?,?,?)", regA)

            for s in v:

                #reqH = ("id_Aula", "hora")
                regH = (self.c, s)
                
                cursor.execute("INSERT INTO Horarios VALUES (?,?)", regH)

            self.c = self.c + 1
    """

    def insertarTutoriasBBDD(self, t, id_profesor, cursor):

        for k, v in t.items():
           
            for s in v:
                #req = ("id_profesor", "cuatrimestre", "hora")
                reg = (id_profesor, k, s) 
                cursor.execute("INSERT INTO Tutorias VALUES (?,?,?)", reg)