# interfaz.py

Resumen

`App` es la clase principal que construye la interfaz gráfica con Tkinter. Orquesta el flujo de la aplicación: login, menú, registro, ingreso de notas y visualización de estudiantes.

Flujo de la aplicación

1. `pantalla_login()` — pide el correo institucional para acceder.
2. `pantalla_menu()` — menú principal con opciones para registrar, ver estudiantes, cerrar sesión o salir.
3. `pantalla_registro()` — formulario inicial para nombre, código y correo del estudiante.
4. `pantalla_notas()` — formulario (scrollable) para ingresar las notas de los tres cortes y calcular la definitiva.
5. `calcular_y_guardar()` — valida las entradas, calcula las notas usando `Logica`, guarda en la base de datos y muestra un resumen.
6. `pantalla_ver_estudiantes()` — lista todos los estudiantes desde la base de datos.

Helpers importantes

- `crear_entry(parent, ancho=30)` — devuelve un `tk.Entry` con estilo consistente.
- `crear_boton(parent, texto, comando, ...)` — botón estilizado.
- `limpiar_ventana()` — destruye widgets para cambiar de pantalla.

Notas de integración

- `App` crea internamente `BaseDatos()` y `Logica()` y los usa para persistencia y validación.
- La imagen `Logo U 1.png` se carga desde la misma carpeta del archivo (`__file__`). Si falta, la app fallará al iniciar.

Sugerencias

- Manejar la ausencia de la imagen con un bloque try/except y usar un placeholder.
- Extraer cadenas (mensajes) a constantes para facilitar cambios y traducción.
- Añadir confirmación al cerrar la app (`salir`) para evitar cierres accidentales.

Atajos para desarrolladores

- Ejecuta `python interfaz.py` desde la carpeta `Sistema de Notas`.
- Si deseas ejecutar la lógica sin UI, se pueden importar `Logica` desde la consola Python.
