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

    



    def selectHorarios(self):

        cursor = self.db.cursor();
        

        #cursor.execute("""insert into horarios values (3, 'GIS2', 'segundo', 'fp', '2017-03-17', 8, 10)""")

        self.db.commit()

        #cursor.execute("""select * from horarios where curso = 'GIS2' """)  
        cursor.execute("""select * from horarios""")  
        
        for tupla in cursor.fetchall():
            print (tupla)

    def insertarCursos(self, tablas):

        cursor = self.db.cursor();

        reg = ()
        
       
        cont = 0;
        for key, value in tablas.items():
         
            for v  in value:
                #req = (id_curso, grado, curso, grupo)
                
            
                if ('Optativas' in v ):
                    lista = v.split('Optativas')
                    reg = (cont, key, 0, lista[len(lista)-1])
        
                else:

                    lista = v.split('º')
                   
                    reg = (cont, key, lista[0], lista[1])

                print(reg)
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
                    #req = ("id_profesor", "nombre","correo","telefono", "despacho")
                    
                    if(len(c) == 6):
                        reg = (cont, c[0], c[1], c[2], c[3])
                        
                        n = self.insertarClasesBBDD(c[4], cont, n, cursor)
                        
                        self.insertarTutoriasBBDD(c[5], cont, cursor)
                    else:
                        reg = (cont, c[0], c[1], c[2], " ")

                        n = self.insertarClasesBBDD(c[3], cont, n, cursor)

                        self.insertarTutoriasBBDD(c[4], cont, cursor)

                    
                    cursor.execute("INSERT INTO profesores VALUES (?,?,?,?,?)", reg)
    
                    cont = cont + 1

        self.db.commit()            

    def insertarClasesBBDD(self, h, id_profesor, cont, cursor):

        n = 0;
        if len(h['1c']) > 1:
            cua1 = h['1c']
        #    print (cua1)
            for k, v in cua1.items():

                lista = k.split('(');
                lista = lista[1].split(')')
                lista = lista[0].split('-')
                
                #req = ("id_clase", id_profesor", id_asignatura "cuatrimestre", "curso")

                reg = (cont, id_profesor,  lista[0], '1', lista[2])
                
                
                cursor.execute("INSERT OR REPLACE INTO Clases VALUES (?,?,?,?,?)", reg)
               
                self.insertarAulasHorariosBBDD(v, cont, cursor)

                cont = cont + 1

        if len(h['2c']) > 1:
            cua2 = h['2c']
        #    print (cua1)
            for k, v in cua2.items():

                lista = k.split('(');
                lista = lista[1].split(')')
                lista = lista[0].split('-')

                #req = ("id_clase", id_profesor", id_asignatura "cuatrimestre", "curso")
                
                if(len(lista) == 3):

                    reg = (cont, id_profesor, lista[0], '2', lista[2])
                    
                    cursor.execute("INSERT OR REPLACE INTO Clases VALUES (?,?,?,?,?)", reg)
                    self.insertarAulasHorariosBBDD(v, cont, cursor)

                cont = cont + 1

        return cont

    def insertarAulasHorariosBBDD(self, a, id_clase, cursor):

        idA = 0
        cambio = False
        hora = ""
        #print ("idH: ", id_clase, " -> ", a)

        for k, v in a.items():

            au = k.split('-')
            au = au[1]
            
            #reqA = ("id_aulas", id_clase", "Aula_lab")
            regA = (self.c, id_clase, au)
            
            cursor.execute("INSERT INTO Aulas VALUES (?,?,?)", regA)

            for s in v:

                #reqH = ("id_Aula", "hora")
                regH = (self.c, s)
                
                cursor.execute("INSERT INTO Horarios VALUES (?,?)", regH)

            self.c = self.c + 1


    def insertarTutoriasBBDD(self, t, id_profesor, cursor):

        for k, v in t.items():
           
            for s in v:
                #req = ("id_profesor", "cuatrimestre", "hora")
                reg = (id_profesor, k, s) 
                cursor.execute("INSERT INTO Tutorias VALUES (?,?,?)", reg)