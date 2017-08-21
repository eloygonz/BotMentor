import sqlite3 as dbapi 

db = dbapi.connect("db.dat")

cursor = db.cursor();

#cursor.execute(" TRUNCATE TABLE horarios; ")
'''
cursor.execute("""DELETE FROM "horarios" """)

db.commit()
'''
#(id, curso, cuatrimestre, asignatura, aulas_labs, dia, hora)
'''
cursor.execute(""" create table horarios (id INTEGER PRIMARY KEY, curso VARCHAR(50), 
	cuatrimestre VARCHAR(50), asignatura VARCHAR(50), aulas_labs VARCHAR(150), dia INT(9), hora INT(9)) """)


cursor.execute(""" create table asignaturas (id INTEGER PRIMARY KEY, grado VARCHAR(50), 
	abreviatura VARCHAR(50), nombre VARCHAR(50), codigo INT(9)) """)
'''



cursor.execute("""CREATE TABLE IF NOT EXISTS Clases (id_clase integer not null unique, id_profesor INTEGER REFERENCES profesores(id_profesor) ON DELETE CASCADE NOT NULL, 
		id_asignatura VARCHAR NOT NULL REFERENCES asignaturas(id_asignatura), cuatrimestre INTEGER NOT NULL, grado VARCHAR NOT NULL, curso VARCHAR NOT NULL, grupo VARCHAR NOT NULL, 
		PRIMARY KEY (id_clase))""")

#cursor.execute("""CREATE TABLE IF NOT EXISTS Clases (id_clase integer not null unique, id_profesor INTEGER REFERENCES profesores(id_profesor) ON DELETE CASCADE NOT NULL, 
#		id_asignatura VARCHAR NOT NULL REFERENCES asignaturas(id_asignatura), cuatrimestre INTEGER NOT NULL,  curso VARCHAR NOT NULL, grupo VARCHAR NOT NULL, aula_lab VARCHAR, hora VARCHAR, 
#		PRIMARY KEY (id_clase))""")

#cursor.execute("""CREATE TABLE IF NOT EXISTS Clases (id_clase integer not null unique, id_profesor INTEGER REFERENCES profesores(id_profesor) ON DELETE CASCADE NOT NULL, 
		#id_asignatura VARCHAR NOT NULL REFERENCES asignaturas(id_asignatura), cuatrimestre INTEGER NOT NULL,  curso VARCHAR NOT NULL, grupo VARCHAR NOT NULL, aula_lab VARCHAR, hora VARCHAR, 
		#PRIMARY KEY (id_profesor, id_asignatura,  cuatrimestre, curso, grupo, aula_lab, hora))""")

# PRIMARY KEY (id_profesor, id_asignatura,  cuatrimestre, curso))  no se puede ya que en las tablas se repite la asignatura varias veces, lo cual nos jode por completo
#cursor.execute(""" CREATE UNIQUE INDEX id_clase on Clases(id_clase) """)

cursor.execute("""CREATE TABLE IF NOT EXISTS Asignaturas  (id_asignatura integer NOT NULL, grado VARCHAR NOT NULL, siglas VARCHAR, nombre VARCHAR,  PRIMARY KEY (id_asignatura, grado)) """)

cursor.execute("""CREATE TABLE IF NOT EXISTS Profesores (id_profesor integer, nombre VARCHAR, apellidos VARCHAR, correo VARCHAR, telefono VARCHAR, despacho VARCHAR, PRIMARY KEY (id_profesor DESC))""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Aulas_Horarios (id_aulas integer, id_clase integer REFERENCES clases(id_clase), aula_lab VARCHAR, hora VARCHAR, PRIMARY KEY (id_aulas)) """)

#cursor.execute("""CREATE TABLE IF NOT EXISTS Aulas (id_aulas integer, id_clase integer REFERENCES clases(id_clase), aula_lab VARCHAR, PRIMARY KEY (id_aulas)) """)

#cursor.execute("""CREATE TABLE IF NOT EXISTS Horarios (id_aulas integer REFERENCES aulas_clases(id), hora VARCHAR) """)

cursor.execute("""CREATE TABLE IF NOT EXISTS Tutorias (id_profesor integer REFERENCES Profesores(id_profesor), cuatrimestre INTEGER NOT NULL, hora VARCHAR)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Cursos (id_cursos integer not null unique, grado VARCHAR, curso INTEGER NOT NULL, grupo VARCHAR, PRIMARY KEY (id_cursos))""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Fichas (id_fichas integer not null unique, grado VARCHAR, curso VARCHAR , id_asignatura VARCHAR NOT NULL REFERENCES asignaturas(id_asignatura), asignatura VARCHAR, documento VARCHAR, PRIMARY KEY (id_fichas))""")

#cursor.execute("""CREATE VIEW DATOS_CLASE AS SELECT CLASE.ID AS ID_CLASE, CLASE.IDA AS ID_A, CLASE.IDP AS ID_P, CLASE.CUATRI AS CUATRIMESTRE, CLASE.GRADO, CLASE.CURSO, CLASE.GRUPO, ASIGNATURA.NOMBRE AS NOMBRE_A, ASIGNATURA.SIGLAS, PROFESOR.NOMBRE AS NOMBRE_P FROM  CLASE, ASIGNATURA, PROFESOR WHERE CLASE.IDA = ASIGNATURA.ID AND CLASE.IDP = PROFESOR.ID """)