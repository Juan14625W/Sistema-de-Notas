# Sistema de Notas

Aplicación de escritorio (Tkinter) para calcular y registrar notas de estudiantes.

Descripción
- Interfaz gráfica para ingresar notas por cortes y calcular la nota definitiva.
- Almacena estudiantes en una base de datos SQLite (`notas.db`).
- Validaciones básicas de correo y valores de nota.

Características
- Login por correo institucional (@uniautonoma.edu.co).
- Registro de estudiantes con cálculo de notas por corte y estado (Aprobado/Reprovado).
- Visualización de estudiantes registrados.

Requisitos
- Python 3.8+
- Tkinter (incluido en la mayoría de instalaciones de Python)
- Pillow (para manejo de la imagen del logo)

Instalación rápida

```bash
python -m pip install --upgrade pip
python -m pip install pillow
```

Cómo ejecutar

```bash
cd "Sistema de Notas"
python interfaz.py
```

Archivos principales
- `Sistema de Notas/base_datos.py`: acceso a SQLite y funciones CRUD mínimas.
- `Sistema de Notas/logica.py`: reglas de validación y cálculo de notas.
- `Sistema de Notas/interfaz.py`: aplicación Tkinter que orquesta la experiencia de usuario.

Notas importantes
- La primera ejecución crea `notas.db` en la carpeta de trabajo.
- Asegúrate de tener el archivo de imagen `Logo U 1.png` en la misma carpeta que `interfaz.py`.

Documentación por módulo
- docs/base_datos.md
- docs/logica.md
- docs/interfaz.md

Si quieres, puedo:
- Insertar docstrings directamente en los archivos Python.
- Añadir un pequeño script de pruebas o ejemplos automatizados.
- Preparar un paquete instalable (`requirements.txt`, `setup.py`).
