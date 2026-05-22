import sqlite3

class BaseDatos:
    def __init__(self):
        self.conexion = sqlite3.connect("notas.db")
        self.cursor = self.conexion.cursor()
        self.crear_tablas()
    def crear_tablas(self):
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
        self.cursor.execute("SELECT * FROM estudiantes")
        return self.cursor.fetchall()
        
    def cerrar(self):
        self.conexion.close()