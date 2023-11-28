from sqlite3 import *

def crearConexion():
    conn=connect("./base_datos/tecnologico.db")
    conn.commit()
    conn.close()

def crearTablaAlumno():
    conn=connect("./base_datos/tecnologico.db")
    cursor=conn.cursor()
    sentencia="""
      CREATE TABLE IF NOT EXISTS Alumnos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT(250),
        edad INTEGER
    )
"""
    cursor.execute(sentencia)
    conn.commit()
    conn.close()
    
def crearTablaCurso():
    conn=connect("./base_datos/tecnologico.db")
    cursor=conn.cursor()
    sentencia="""
      CREATE TABLE IF NOT EXISTS Cursos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT(250),
        id_alumno INTEGER,
        FOREIGN KEY(id_alumno) REFERENCES Alumnos_id
    )
"""
    cursor.execute(sentencia)
    conn.commit()
    conn.close()

def insertAlumno(nombre,edad):
    conn=connect("./base_datos/tecnologico.db")
    cursor=conn.cursor()
    sentencia=f"INSERT INTO Alumnos(nombre,edad) VALUES('{nombre}',{edad})"
    cursor.execute(sentencia)
    conn.commit()
    conn.close()

def insertAlumnos(lista):
    conn=connect("./base_datos/tecnologico.db")
    cursor=conn.cursor()
    sentencia=f"INSERT INTO Alumnos(nombre,edad) VALUES(?,?)"
    cursor.executemany(sentencia,lista)
    conn.commit()
    conn.close()

if __name__=="__main__":
    #crearConexion()
    # crearTablaAlumno()
    # crearTablaCurso()
    # insertAlumno('Yerson',19)
    # insertAlumno('Emerson',18)
    alum=[
        ('rony',26),
        ('yony',19),
        ('monchi',21),
        ('yerson',18),
        ('denis',18)
    ]
    insertAlumnos(alum)

    #tarea
    #eliminar y actualizar la lista alumno