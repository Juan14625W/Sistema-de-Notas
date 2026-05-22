# base_datos.py

Resumen

`BaseDatos` es una clase ligera para interactuar con una base de datos SQLite llamada `notas.db`. Se encarga de crear la tabla `estudiantes` y provee métodos simples para insertar y obtener registros.

Esquema de la tabla `estudiantes`
- `id` (INTEGER, PK, autoincrement)
- `nombre` (TEXT, NOT NULL)
- `codigo` (TEXT, UNIQUE, NOT NULL)
- `correo` (TEXT, UNIQUE, NOT NULL)
- `nota_final` (REAL)
- `aprobado` (TEXT)

API principal

- `BaseDatos()` -> instancia con conexión abierta y tablas creadas.
- `crear_tablas()` -> crea la tabla `estudiantes` si no existe.
- `insertar_estudiante(nombre, codigo, correo, nota_final, aprobado)` -> intenta insertar un estudiante. Devuelve `True` si se guarda, `False` si hubo conflicto de unicidad (código o correo duplicado).
- `obtener_estudiantes()` -> devuelve una lista de tuplas con todos los registros.
- `cerrar()` -> cierra la conexión a la base de datos.

Notas de implementación

- Usa `sqlite3` integrado en Python, sin ORM.
- `insertar_estudiante` captura `sqlite3.IntegrityError` y lo traduce a `False` para que la interfaz pueda mostrar un error amigable.

Sugerencias

- Añadir manejo de excepciones más fino y logging para depuración.
- Agregar métodos para buscar/actualizar/eliminar estudiantes si se requiere.
