# -*- coding: UTF-8 -*-
import sqlite3 as dbapi 
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


class training_asignaturas:
    """ docstring for trainingAsignaturas
        Clase para entrenar (Asignaturas)
    """
    c = 0
 
    #Constructor
    def __init__(self, chatbotX):
        
        super(training_asignaturas, self).__init__()

        self.db = dbapi.connect("dbScraping.sqlite3")
        self.chatbot = chatbotX
        #a.trainingAsignaturaInfo()
        #a.trainingAsignaturaProfesores()
        #a.trainingAsignaturaClases()
       

    def trainingAsignaturaInfo(self):
           
        cursor = self.db.cursor();

        a = cursor.execute("""select * from Asignaturas """)

        listaAsignaturas =''
        for c, rowA in enumerate (a.fetchall()):
            listaAsignaturas =  listaAsignaturas + str(c) +": "+ rowA[1] +" -> "+ rowA[3] +" ("+ rowA[2]+"-"+str(rowA[0])+")\n"
        
        #print (listaAsignaturas)
        converInfoAsignaturas = [

            "me gustarias tener la lista de asignaturas que hay en la facultada?",
            listaAsignaturas

        ]       
        self.chatbot.set_trainer(ListTrainer)
        self.chatbot.train(converInfoAsignaturas)
        converInfoAsignaturas = [

            "asignaturas que hay en la facultada?",
            listaAsignaturas

        ]       
        self.chatbot.set_trainer(ListTrainer)
        self.chatbot.train(converInfoAsignaturas)
        converInfoAsignaturas = [

            "asignaturas",
            listaAsignaturas

        ]       
        self.chatbot.set_trainer(ListTrainer)
        self.chatbot.train(converInfoAsignaturas)
        converInfoAsignaturas = [

            "que asignaturas hay?",
            listaAsignaturas

        ]       
        self.chatbot.set_trainer(ListTrainer)
        self.chatbot.train(converInfoAsignaturas)
        converInfoAsignaturas = [

            "lista de asignaturas ?",
            listaAsignaturas

        ]       
        self.chatbot.set_trainer(ListTrainer)
        self.chatbot.train(converInfoAsignaturas)

    def trainingAsignaturaProfesores(self):

        cursor = self.db.cursor();
        
        a = cursor.execute("""select * from Asignaturas """)
        
        for rowA in a.fetchall():
            
            cp = cursor.execute("select p.nombre, p.apellidos, c.cuatrimestre from clases as c, Profesores as p Where c.id_asignatura = '"+str(rowA[0])+"' and c.id_profesor = p.id_profesor ")
            cadena = ''
            for rowCP in cp.fetchall():
                cadena = cadena + rowCP[0] + " " + rowCP[1] +" en cuatrimestre "+str(rowCP[2]) +"\n"
                

            if( cadena == ' '):
                cadena = "ningún porfesor imparte esta asignatura"
            converAsigProfesor = [

                "quiero saber los profesores que imparten "+ rowA[2] + " en el grado "+ rowA[1],
                "la asignatura "+rowA[2]+" en el grado "+ rowA[1] +" esta impartida por: \n" + cadena

            ]  
            
            self.chatbot.set_trainer(ListTrainer)
            self.chatbot.train(converAsigProfesor)
         
    def trainingAsignaturaClases(self):
        
        cursor = self.db.cursor();
        
        a = cursor.execute("""select * from Asignaturas """)
        
        for rowA in a.fetchall():
            
            c = cursor.execute("select * from clases Where id_asignatura = '"+str(rowA[0])+"'")
            cadena = ''
            for rowC in c.fetchall():
                cadena = cadena + rowC[4] + " " + rowC[5] + " " + rowC[6] +" en cuatrimestre "+str(rowC[3]) +"\n"
                

            if( cadena == ' '):
                cadena = "ninguna clase para esta asignatura"
            converAsigClases = [

                "quiero saber las clases de la asignatura "+ rowA[2] + " en el grado "+ rowA[1],
                "las clases en la asignatura "+rowA[2]+" en el grado "+ rowA[1] +" son: \n" + cadena

            ]  
            
            self.chatbot.set_trainer(ListTrainer)
            self.chatbot.train(converAsigClases)


    def trainingAsignaturaFichaDocente(self):

        cursor = self.db.cursor();
        
        f = cursor.execute("""select * from Fichas """)
        
        for rowF in f.fetchall():
            
            
            a = cursor.execute("select  * from asignaturas  Where id_asignatura = "+str(rowF[3])+" and grado ='"+rowF[1]+"' ")
            
            asignatura = ''
            for c,rowA in enumerate(a.fetchall()):
                asignatura = rowA[2]
          
            converAsigFicha = [

                "quiero saber la ficha docente de la asignatura "+ str(asignatura) + " en el grado "+ rowF[1],
                "la ficha docente de la asignatura "+str(asignatura)+" en el grado "+ rowF[1] +" es: \n" + rowF[5] + "\n"

            ]  
            
            self.chatbot.set_trainer(ListTrainer)
            self.chatbot.train(converAsigFicha)