# -*- coding: UTF-8 -*-
import sqlite3 as dbapi 
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


class training_profesores:
    """ docstring for trainingProfesores
        Clase para entrenar (Profesores)
    """
    c = 0
 
    #Constructor
    def __init__(self, chatbotX):
        
        super(training_profesores, self).__init__()

        self.db = dbapi.connect("dbScraping.sqlite3")
        self.chatbot = chatbotX
        #t.trainingProfesorInfo()
        #t.trainingCorreoElectronicoProfesor()
        #t.trainingTelefonoProfesor()
        #t.trainingDespachoProfesor()
        #t.trainingTutorias()
        #t.trainingClases()
       

    def trainingProfesorInfo(self):
        chatbot.set_trainer(ChatterBotCorpusTrainer)

        """
        chatbot.train(
            "chatterbot.corpus.spanish"
        )
        """
       
        cursor = self.db.cursor();

        cursor.execute("""select * from Profesores """)

        listaProfesores =''
        for c, rowP in enumerate (cursor.fetchall()):
            listaProfesores =  listaProfesores + str(c) +": "+ rowP[1] +" "+ rowP[2] + "\n"
        

        converInfoProfesor = [

            "me gustarias tener la lista de profesores que hay en la facultada?",
            listaProfesores

        ]       
        self.chatbot.set_trainer(ListTrainer)
        self.chatbot.train(converInfoProfesor)
        converInfoProfesor = [

            "profesores que hay en la facultada?",
            listaProfesores

        ]       
        self.chatbot.set_trainer(ListTrainer)
        self.chatbot.train(converInfoProfesor)
        converInfoProfesor = [

            "profesores",
            listaProfesores

        ]       
        self.chatbot.set_trainer(ListTrainer)
        self.chatbot.train(converInfoProfesor)
        converInfoProfesor = [

            "que profesores hay?",
            listaProfesores

        ]       
        self.chatbot.set_trainer(ListTrainer)
        self.chatbot.train(converInfoProfesor)
        converInfoProfesor = [

            "lista de profesores ?",
            listaProfesores

        ]       
        self.chatbot.set_trainer(ListTrainer)
        self.chatbot.train(converInfoProfesor)

    def trainingCorreoElectronicoProfesor(self):

        cursor = self.db.cursor();

        cursor.execute("""select * from Profesores """)

        for tupla in cursor.fetchall():
        
            converCorreoProfesor = [

                "quiero saber el correo electronico del profesor "+ tupla[1] +" " + tupla[2],
                "el correo del profesor "+ tupla[1] +" " + tupla[2] +" es "+ tupla[3]

            ]       
            self.chatbot.set_trainer(ListTrainer)
            self.chatbot.train(converCorreoProfesor)

            converCorreoProfesor = [

                "quiero saber el email del profesor "+ tupla[1] +" " + tupla[2],
                "el correo del profesor "+ tupla[1] +" " + tupla[2] +" es "+ tupla[3]

            ]       
            self.chatbot.set_trainer(ListTrainer)
            self.chatbot.train(converCorreoProfesor)

            converCorreoProfesor = [

                "quiero saber el email del profesor "+ tupla[1] +" " + tupla[2],
                "el correo del profesor "+ tupla[1] +" " + tupla[2] +" es "+ tupla[3]

            ]       
            self.chatbot.set_trainer(ListTrainer)
            self.chatbot.train(converCorreoProfesor)

            converCorreoProfesor = [

                "cual es el correo electronico del profesor "+ tupla[1] +" " + tupla[2]+" ?",
                "el correo del profesor "+ tupla[1] +" " + tupla[2] +" es "+ tupla[3]

            ]       
            self.chatbot.set_trainer(ListTrainer)
            self.chatbot.train(converCorreoProfesor)

            converCorreoProfesor = [

                "cual es el correo del profesor "+ tupla[1] +" " + tupla[2] +" ?",
                "el correo del profesor "+ tupla[1] +" " + tupla[2] +" es "+ tupla[3]

            ]       
            self.chatbot.set_trainer(ListTrainer)
            self.chatbot.train(converCorreoProfesor)

            converCorreoProfesor = [

                "cual es el email del profesor "+ tupla[1] +" " + tupla[2] +" ?",
                "el correo del profesor "+ tupla[1] +" " + tupla[2] +" es "+ tupla[3]

            ]       
            self.chatbot.set_trainer(ListTrainer)
            self.chatbot.train(converCorreoProfesor)

            converCorreoProfesor = [

                "correo electronico del profesor "+ tupla[1] +" " + tupla[2] +" ?",
                "el correo del profesor "+ tupla[1] +" " + tupla[2] +" es "+ tupla[3]

            ]       
            self.chatbot.set_trainer(ListTrainer)
            self.chatbot.train(converCorreoProfesor)

            converCorreoProfesor = [

                "correo del profesor "+ tupla[1] +" " + tupla[2] +" ?",
                "el correo del profesor "+ tupla[1] +" " + tupla[2] +" es "+ tupla[3]

            ]       
            self.chatbot.set_trainer(ListTrainer)
            self.chatbot.train(converCorreoProfesor)

            converCorreoProfesor = [

                "email del profesor "+ tupla[1] +" " + tupla[2] +" ?",
                "el correo del profesor "+ tupla[1] +" " + tupla[2] +" es "+ tupla[3]

            ]       
            self.chatbot.set_trainer(ListTrainer)
            self.chatbot.train(converCorreoProfesor)


    def trainingTelefonoProfesor(self):
        
        cursor = self.db.cursor();

        cursor.execute("""select * from Profesores """)

        for tupla in cursor.fetchall():
        
            converTelefonoProfesor = [

                "cual es el número de telefono del profesor "+ tupla[1] +" " + tupla[2],
                "el número de telefono del profesor "+ tupla[1] +" " + tupla[2] +" es "+ tupla[4]

            ]       
            self.chatbot.set_trainer(ListTrainer)
            self.chatbot.train(converTelefonoProfesor)
           
            converTelefonoProfesor = [

                "quiero sabe el número de telefono del profesor "+ tupla[1] +" " + tupla[2],
                "el número de telefono del profesor "+ tupla[1] +" " + tupla[2] +" es "+ tupla[4]

            ]       
            self.chatbot.set_trainer(ListTrainer)
            self.chatbot.train(converTelefonoProfesor)
            converTelefonoProfesor = [

                "quiero saber el telefono del profesor "+ tupla[1] +" " + tupla[2],
                "el número de telefono del profesor "+ tupla[1] +" " + tupla[2] +" es "+ tupla[4]

            ]       
            
            self.chatbot.set_trainer(ListTrainer)
            self.chatbot.train(converTelefonoProfesor)
            converTelefonoProfesor = [

                "cual es el telefono del profesor "+ tupla[1] +" " + tupla[2],
                "el número de telefono del profesor "+ tupla[1] +" " + tupla[2] +" es "+ tupla[4]

            ]       
            self.chatbot.set_trainer(ListTrainer)
            self.chatbot.train(converTelefonoProfesor)
            
            converTelefonoProfesor = [

                "telefono del profesor "+ tupla[1] +" " + tupla[2],
                "el número de telefono del profesor "+ tupla[1] +" " + tupla[2] +" es "+ tupla[4]

            ]       
            self.chatbot.set_trainer(ListTrainer)
            self.chatbot.train(converTelefonoProfesor)

    def trainingDespachoProfesor(self):
        
        cursor = self.db.cursor();

        cursor.execute("""select * from Profesores """)

        for rowP in cursor.fetchall():

            if(rowP[5] != " "):

                converTelefonoProfesor = [

                    "cual es el despacho "+ rowP[1] +" " + rowP[2],
                    "el despacho de "+ rowP[1] +" " + rowP[2] +" es "+ rowP[5]

                ]       
                self.chatbot.set_trainer(ListTrainer)
                self.chatbot.train(converTelefonoProfesor)
                
                converTelefonoProfesor = [

                    "quiero saber el despacho del profesor "+ rowP[1] +" " + rowP[2],
                    "el despacho de "+ rowP[1] +" " + rowP[2] +" es "+ rowP[5]

                ]       
                self.chatbot.set_trainer(ListTrainer)
                self.chatbot.train(converTelefonoProfesor)
                        
                converTelefonoProfesor = [

                    "despacho del profesor "+ rowP[1] +" " + rowP[2],
                    "el despacho de "+ rowP[1] +" " + rowP[2] +" es "+ rowP[5]

                ]       
                self.chatbot.set_trainer(ListTrainer)
                self.chatbot.train(converTelefonoProfesor)
            else:
                converTelefonoProfesor = [

                    "cual es el despacho "+ rowP[1] +" " + rowP[2],
                    "el profesor "+ rowP[1] +" " + rowP[2] +" no tiene despacho asignado"

                ]       
                self.chatbot.set_trainer(ListTrainer)
                self.chatbot.train(converTelefonoProfesor)

                converTelefonoProfesor = [

                    "quiero saber el despacho del profesor "+ rowP[1] +" " + rowP[2],
                    "el profesor "+ rowP[1] +" " + rowP[2] +" no tiene despacho asignado"

                ]       
                self.chatbot.set_trainer(ListTrainer)
                self.chatbot.train(converTelefonoProfesor)
                
                converTelefonoProfesor = [

                    "despacho del profesor "+ rowP[1] +" " + rowP[2],
                    "el profesor "+ rowP[1] +" " + rowP[2] +" no tiene despacho asignado"

                ]       
                self.chatbot.set_trainer(ListTrainer)
                self.chatbot.train(converTelefonoProfesor)


    def trainingTutorias(self):
        
        cursor = self.db.cursor();

        p = cursor.execute("""select * from Profesores """)
        
        for rowP in p.fetchall():

            cadena1 = ''
            cadena2 = ''
            t = cursor.execute("select * from Tutorias Where id_profesor = "+str(rowP[0]) )
            for rowT in t.fetchall():
                if(rowT[1] == 1):
                    
                    cadena1 = cadena1 + " en el primer cuatrimestre el dia(s) " 
                    if(rowT[2] == "no tiene tutorias en este cuatrimestre"):
                        
                        cadena1 = cadena1 + "no tiene tutorias"
                
                    else:

                        cadena1 = cadena1 + rowT[2]

                elif(rowT[1] == 2):
                    
                    cadena2 = cadena2 + " en el segundo cuatrimestre el dia(s) "

                    if(rowT[2] == "no tiene tutorias en este cuatrimestre"):
                        
                        cadena2 = cadena2 + "no tiene tutorias"

                    else:

                        cadena2 = cadena2 + rowT[2]

            
            converTutoriaProfesor = [

                "quiero saber las tutorias del profesor "+ rowP[1] +" " + rowP[2] ,
                "las tutorias del profesor "+ rowP[1] +" " + rowP[2] +" son: \n "+ cadena1 + " \n " + cadena2
            ]
                
            
            self.chatbot.set_trainer(ListTrainer)
            self.chatbot.train(converTutoriaProfesor)

        p = cursor.execute("""select * from Profesores """)
        for rowP in p.fetchall():

            
            cuatri = ''
            t = cursor.execute("select * from Tutorias Where id_profesor = "+str(rowP[0]))
            for rowT in t.fetchall():
                if(rowT[1] == 1):
                    cuatri = "primer"

                elif(rowT[1] == 2):
                    cuatri = "segundo"

                if(rowT[2] == "no tiene tutorias en este cuatrimestre"):
                        
                     converTutoriaProfesor = [

                        "quiero saber las tutorias del profesor "+ rowP[1] +" " + rowP[2] + " en el "+cuatri+" cuatrimestre " ,
                        "el profesor "+ rowP[1] +" " + rowP[2] +" no tiene tutorias en el " +cuatri+ " cuatrimestre "
                    ]
                
                else:
                    converTutoriaProfesor = [

                        "quiero saber las tutorias del profesor "+ rowP[1] +" " + rowP[2] + " en el "+cuatri+" cuatrimestre " ,
                        "las tutorias del profesor "+ rowP[1] +" " + rowP[2] +" en el " +cuatri+" cuatrimestre son el dia(s) "+ rowT[2]
                    ]

                self.chatbot.set_trainer(ListTrainer)
                self.chatbot.train(converTutoriaProfesor)

    def trainingClases(self):
        
        cursor = self.db.cursor();
        
        p = cursor.execute("""select * from Profesores """)
        
        for rowP in p.fetchall():

            
            c = cursor.execute("select * from Clases Where id_profesor = "+str(rowP[0]))

            cadena1 = ''
            cadena2 = ''
            
            for rowC in c.fetchall():
                
                a = cursor.execute("select * from Asignaturas Where id_asignatura = '"+str(rowC[2])+"'")
                asignatura =''
                for rowAs in a.fetchall():
                    asignatura = rowAs[2]
                
                aulas_h = cursor.execute("select * from Aulas_Horarios Where id_clase = "+str(rowC[0]))    

                cadenaAulas = ''
                for rowAu in aulas_h.fetchall():
                    cadenaAulas = cadenaAulas + rowAu[2] + ": " +rowAu[3]+"\n\t"
                         

                if(rowC[3] == 1):
                    
                    cadena1 = cadena1 + rowC[4] + " " + rowC[5] + " "+ rowC[6] +" con la asignatura: "+ asignatura +"\n\t"+cadenaAulas
                   

                elif(rowC[3] == 2):
                    
                    cadena2 = cadena2 + rowC[4] + " " + rowC[5] + " " + rowC[6] +" con la asignatura: "+ asignatura +"\n\t"+cadenaAulas


            if cadena1 == '':
                cadena1 = 'no tiene clases en este cuatrimestre'
            

            if cadena2 == '':
                cadena2 = 'no tiene clases en este cuatrimestre' 
            
            converClasesProfesor = [

                "quiero saber las clases del profesor "+ rowP[1] +" " + rowP[2],
                "En el primer cuatrimestre  son: \n "+ cadena1 + "En el segundo cuatrimestre  son: \n " + cadena2
            ]
             
            
            self.chatbot.set_trainer(ListTrainer)
            self.chatbot.train(converClasesProfesor)
            
        
        p = cursor.execute("""select * from Profesores """)
        
        for rowP in p.fetchall():

            
            c = cursor.execute("select * from Clases Where id_profesor = "+str(rowP[0]))

            cadena1 = ''
            cadena2 = ''
            
            for rowC in c.fetchall():
                
                a = cursor.execute("select * from Asignaturas Where id_asignatura = '"+str(rowC[2])+"'")
                asignatura =''
                for rowAs in a.fetchall():
                    asignatura = rowAs[2]
                
                aulas_h = cursor.execute("select * from Aulas_Horarios Where id_clase = "+str(rowC[0]))    

                cadenaAulas = ''
                for rowAu in aulas_h.fetchall():
                    cadenaAulas = cadenaAulas + rowAu[2] + ": " +rowAu[3]+"\n\t"
                
                

                if(rowC[3] == 1):
                    
                    cadena1 = cadena1 + rowC[4] + " " + rowC[5] + " "+ rowC[6] +" con la asignatura: "+ asignatura +"\n\t"+cadenaAulas
                   

                elif(rowC[3] == 2):
                    
                    cadena2 = cadena2 + rowC[4] + " " + rowC[5] + " " + rowC[6] +" con la asignatura: "+ asignatura +"\n\t"+cadenaAulas


            if cadena1 == '':
                cadena1 = 'no tiene clases en este cuatrimestre'
            

            if cadena2 == '':
                cadena2 = 'no tiene clases en este cuatrimestre' 
            
            converClasesProfesor = [

                "quiero saber las clases del profesor "+ rowP[1] +" " + rowP[2]+ " en el primer cuatrimestre  ",
                "las clases del profesor "+ rowP[1] +" " + rowP[2] +" en el primer cuatrimestre  son: \n "+ cadena1
            ]
            
            self.chatbot.set_trainer(ListTrainer)
            self.chatbot.train(converClasesProfesor)
            
            converClasesProfesor = [

                "quiero saber las clases del profesor "+ rowP[1] +" " + rowP[2]+ " en el segundo cuatrimestre  ",
                "las clases del profesor "+ rowP[1] +" " + rowP[2] +" en el segundo cuatrimestre  son: \n " + cadena2
            ]
           
            self.chatbot.set_trainer(ListTrainer)
            self.chatbot.train(converClasesProfesor)