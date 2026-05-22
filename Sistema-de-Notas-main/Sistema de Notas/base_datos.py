"""Módulo de persistencia para el sistema de notas.

Este módulo define la clase `BaseDatos`, que gestiona una base de datos SQLite
local llamada `notas.db` donde se guardan los registros de estudiantes.
"""

import sqlite3

class BaseDatos:
    """Administra la conexión y las operaciones sobre la tabla `estudiantes`."""

    def __init__(self):
        """Crea la conexión SQLite y asegura que la tabla exista."""
        self.conexion = sqlite3.connect("notas.db")
        self.cursor = self.conexion.cursor()
        self.crear_tablas()

    def crear_tablas(self):
        """Crea la tabla `estudiantes` si aún no existe."""
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
        """Inserta un estudiante en la base de datos.

        Args:
            nombre (str): Nombre completo del estudiante.
            codigo (str): Código único del estudiante.
            correo (str): Correo institucional del estudiante.
            nota_final (float): Nota definitiva calculada.
            aprobado (str): Estado de aprobación ('Aprobado' o 'Reprovado').

        Returns:
            bool: True si se guardó el registro. False si ocurrió un conflicto de unicidad.
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
        """Devuelve todos los estudiantes registrados.

        Returns:
            list[tuple]: Lista de tuplas con el contenido de cada fila.
        """
        self.cursor.execute("SELECT * FROM estudiantes")
        return self.cursor.fetchall()

    def cerrar(self):
        """Cierra la conexión SQLite abierta."""
        self.conexion.close()