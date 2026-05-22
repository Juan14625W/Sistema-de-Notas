"""Módulo para manejar la base de datos local de estudiantes.

Este módulo crea la tabla de estudiantes, inserta registros y
recupera los datos guardados en un archivo SQLite llamado notas.db.
"""
import sqlite3

class BaseDatos:
    """Clase que encapsula el acceso a la base de datos SQLite.

    Su responsabilidad es crear la tabla si no existe, insertar registros
    de estudiantes y devolver los estudiantes guardados.
    """
    def __init__(self):
        self.conexion = sqlite3.connect("notas.db")
        self.cursor = self.conexion.cursor()
        self.crear_tablas()
    def crear_tablas(self):
        """Crea la tabla de estudiantes si aún no existe."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS estudiantes (
                id           INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre       TEXT    NOT NULL,
                codigo       TEXT    UNIQUE NOT NULL,
                correo       TEXT    UNIQUE NOT NULL,
                nota_final   REAL,
                aprobado     TEXT
            )
        """)
        self.conexion.commit()
    def insertar_estudiante(self, nombre, codigo, correo, nota_final, aprobado):
        """Inserta un nuevo estudiante en la base de datos.

        Devuelve True si el registro se guarda correctamente. Si el código o el correo
        ya existen, devuelve False para que la interfaz pueda mostrar un error.
        """
        try:
            self.cursor.execute("""
                INSERT INTO estudiantes (nombre, codigo, correo, nota_final, aprobado)
                VALUES (?, ?, ?, ?, ?)
            """, (nombre, codigo, correo, nota_final, aprobado))
            self.conexion.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        
    def obtener_estudiantes(self):
        """Recupera todos los estudiantes registrados."""
        self.cursor.execute("SELECT * FROM estudiantes")
        return self.cursor.fetchall()
        
    def cerrar(self):
        """Cierra la conexión con la base de datos."""
        self.conexion.close()