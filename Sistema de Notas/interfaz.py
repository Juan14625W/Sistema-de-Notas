"""Interfaz gráfica del sistema de notas para Uniautónoma.

Este módulo construye la ventana principal con Tkinter, gestiona el login,
registro de estudiantes, ingreso de notas y visualización de resultados.
"""
import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from base_datos import BaseDatos
from logica import Logica

COLOR_FONDO        = "#1e1e2e"
COLOR_PANEL        = "#2a2a3e"
COLOR_ACENTO       = "#7c3aed"
COLOR_ACENTO2      = "#9d5cf5"
COLOR_TEXTO        = "#e2e8f0"
COLOR_TEXTO_GRIS   = "#94a3b8"
COLOR_EXITO        = "#22c55e"
COLOR_ERROR        = "#ef4444"
COLOR_ENTRY        = "#313145"
COLOR_BORDE        = "#3d3d5c"
FUENTE_TITULO      = ("Segoe UI", 22, "bold")
FUENTE_SUBTITULO   = ("Segoe UI", 13, "bold")
FUENTE_NORMAL      = ("Segoe UI", 11)
FUENTE_PEQUEÑA     = ("Segoe UI", 9)

class App:
    """Clase principal que construye la aplicación y controla la navegación."""

    def __init__(self):
        self.db = BaseDatos()
        self.logica = Logica()
        self.ventana = tk.Tk()
        self.ventana.title("Sistema de Notas - Uniautonoma")
        self.ventana.geometry("800x750")
        self.ventana.resizable(False, False)
        self.ventana.protocol("WM_DELETE_WINDOW", self.salir)
        self.pantalla_login()

    def crear_entry(self, parent, ancho=30):
        """Crea y devuelve un campo de texto estilizado para el formulario."""
        return tk.Entry(
            parent,
            width=ancho,
            font=FUENTE_NORMAL,
            bg=COLOR_ENTRY,
            fg=COLOR_TEXTO,
            insertbackground=COLOR_TEXTO,
            relief="flat",
            bd=8
        )

    def crear_boton(self, parent, texto, comando, ancho=22, color=None):
        """Crea un botón con el estilo de la aplicación y lo devuelve."""
        return tk.Button(
            parent,
            text=texto,
            command=comando,
            width=ancho,
            font=FUENTE_SUBTITULO,
            bg=color or COLOR_ACENTO,
            fg=COLOR_TEXTO,
            activebackground=COLOR_ACENTO2,
            activeforeground=COLOR_TEXTO,
            relief="flat",
            bd=0,
            cursor="hand2",
            pady=8
        )

    def crear_panel(self, parent, pady=20, padx=30):
        """Crea un panel oscuro para agrupar elementos visuales dentro de la ventana."""
        frame = tk.Frame(parent, bg=COLOR_PANEL, bd=0, relief="flat")
        frame.pack(pady=pady, padx=padx, fill="both", expand=True)
        return frame

    def pantalla_login(self):
        """Muestra la pantalla de inicio de sesión donde el usuario ingresa su correo."""
        self.limpiar_ventana()
        self.ventana.configure(bg=COLOR_FONDO)

        tk.Frame(self.ventana, bg=COLOR_ACENTO, height=6).pack(fill="x")

        panel = tk.Frame(self.ventana, bg=COLOR_PANEL, bd=0)
        panel.pack(pady=40, padx=50, fill="both", expand=True)
        imagen_path = os.path.join(os.path.dirname(__file__), "Logo U 1.png")
        imagen = Image.open(imagen_path)
        imagen = imagen.resize((180, 120))
        self.logo_img = ImageTk.PhotoImage(imagen)
        tk.Label(
            panel,
            image=self.logo_img,
            bg=COLOR_PANEL).pack(pady=(30, 10))
        tk.Label(panel, text="🎓",
                 font=("Segoe UI Emoji", 40),
                 bg=COLOR_PANEL, fg=COLOR_ACENTO).pack(pady=(20, 5))

        tk.Label(panel, text="Sistema de Notas",
                 font=FUENTE_TITULO,
                 bg=COLOR_PANEL, fg=COLOR_TEXTO).pack()

        tk.Label(panel, text="Corporación Universitaria Autónoma del Cauca",
                 font=FUENTE_PEQUEÑA,
                 bg=COLOR_PANEL, fg=COLOR_TEXTO_GRIS).pack(pady=(2, 25))

        tk.Frame(panel, bg=COLOR_BORDE, height=1).pack(fill="x", padx=20)

        tk.Label(panel, text="Correo institucional:",
                 font=FUENTE_PEQUEÑA,
                 bg=COLOR_PANEL, fg=COLOR_TEXTO_GRIS).pack(anchor="w", padx=30, pady=(20, 3))

        self.entry_correo = self.crear_entry(panel, ancho=33)
        self.entry_correo.pack(padx=30)
        self.entry_correo.bind("<Return>", lambda e: self.verificar_login())

        self.crear_boton(panel, "  Ingresar →", self.verificar_login).pack(pady=25)

        tk.Label(panel, text="Solo usuarios @uniautonoma.edu.co",
                 font=FUENTE_PEQUEÑA,
                 bg=COLOR_PANEL, fg=COLOR_TEXTO_GRIS).pack(pady=(0, 5))

        tk.Frame(panel, bg=COLOR_BORDE, height=1).pack(fill="x", padx=20)

        footer = tk.Frame(self.ventana, bg=COLOR_FONDO)
        footer.pack(side="bottom", fill="x", pady=8)
        tk.Label(footer,
                 text="© 2026 Estiven Chantre Sánchez y  Marcela Apio Caliz     •  Uniautónoma del Cauca",
                 font=FUENTE_PEQUEÑA,
                 bg=COLOR_FONDO, fg=COLOR_ACENTO).pack()

    def verificar_login(self):
        """Valida el correo ingresado y redirige al menú si es correcto."""
        correo = self.entry_correo.get().strip()
        if correo == "":
            messagebox.showwarning("Aviso", "Ingresa tu correo")
            return
        valido, mensaje = self.logica.validar_correo(correo)
        if not valido:
            messagebox.showerror("Acceso denegado", mensaje)
        else:
            self.correo_actual = correo
            self.pantalla_menu()

    def pantalla_menu(self):
        """Muestra el menú principal con las opciones de registro, consulta y salida."""
        self.limpiar_ventana()
        self.ventana.configure(bg=COLOR_FONDO)

        tk.Frame(self.ventana, bg=COLOR_ACENTO, height=6).pack(fill="x")

        panel = tk.Frame(self.ventana, bg=COLOR_PANEL)
        panel.pack(pady=30, padx=50, fill="both", expand=True)

        tk.Label(panel, text="📋  Menú Principal",
                 font=FUENTE_TITULO,
                 bg=COLOR_PANEL, fg=COLOR_TEXTO).pack(pady=(30, 5))

        tk.Label(panel, text=f"Sesión: {self.correo_actual}",
                 font=FUENTE_PEQUEÑA,
                 bg=COLOR_PANEL, fg=COLOR_TEXTO_GRIS).pack()

        tk.Frame(panel, bg=COLOR_BORDE, height=1).pack(fill="x", padx=20, pady=20)

        self.crear_boton(panel, "📝  Registrar estudiante",
                         self.pantalla_registro).pack(pady=8)

        self.crear_boton(panel, "📊  Ver estudiantes registrados",
                         self.pantalla_ver_estudiantes,
                         color="#0f766e").pack(pady=8)

        tk.Frame(panel, bg=COLOR_BORDE, height=1).pack(fill="x", padx=20, pady=15)

        self.crear_boton(panel, "🚪  Cerrar sesión",
                         self.pantalla_login, color="#374151").pack(pady=5)

        self.crear_boton(panel, "❌  Salir",
                         self.salir, color=COLOR_ERROR).pack(pady=5)

        tk.Label(panel, text="Sistema de Notas v1.0",
                 font=FUENTE_PEQUEÑA,
                 bg=COLOR_PANEL, fg=COLOR_TEXTO_GRIS).pack(pady=(20, 15))

    def pantalla_registro(self):
        """Muestra el formulario para registrar los datos básicos del estudiante."""
        self.limpiar_ventana()
        self.ventana.configure(bg=COLOR_FONDO)

        tk.Frame(self.ventana, bg=COLOR_ACENTO, height=6).pack(fill="x")

        panel = tk.Frame(self.ventana, bg=COLOR_PANEL)
        panel.pack(pady=30, padx=50, fill="both", expand=True)

        tk.Label(panel, text="📝  Registro de Estudiante",
                 font=FUENTE_TITULO,
                 bg=COLOR_PANEL, fg=COLOR_TEXTO).pack(pady=(30, 5))

        tk.Frame(panel, bg=COLOR_BORDE, height=1).pack(fill="x", padx=20, pady=15)

        tk.Label(panel, text="Nombre completo:",
                 font=FUENTE_PEQUEÑA,
                 bg=COLOR_PANEL, fg=COLOR_TEXTO_GRIS).pack(anchor="w", padx=30, pady=(10, 3))
        self.entry_nombre = self.crear_entry(panel, ancho=33)
        self.entry_nombre.pack(padx=30)

        tk.Label(panel, text="Código:",
                 font=FUENTE_PEQUEÑA,
                 bg=COLOR_PANEL, fg=COLOR_TEXTO_GRIS).pack(anchor="w", padx=30, pady=(10, 3))
        self.entry_codigo = self.crear_entry(panel, ancho=33)
        self.entry_codigo.pack(padx=30)

        tk.Label(panel, text="Correo institucional:",
                 font=FUENTE_PEQUEÑA,
                 bg=COLOR_PANEL, fg=COLOR_TEXTO_GRIS).pack(anchor="w", padx=30, pady=(10, 3))
        self.entry_correo2 = self.crear_entry(panel, ancho=33)
        self.entry_correo2.pack(padx=30)

        tk.Frame(panel, bg=COLOR_BORDE, height=1).pack(fill="x", padx=20, pady=20)

        self.crear_boton(panel, "Siguiente → Ingresar Notas",
                         self.pantalla_notas).pack(pady=5)
        self.crear_boton(panel, "← Volver",
                         self.pantalla_menu, color="#374151").pack(pady=5)
        
    def pantalla_notas(self):
        """Muestra la pantalla donde se ingresan las notas del estudiante."""
        self.nombre_actual = self.entry_nombre.get().strip()
        self.codigo_actual = self.entry_codigo.get().strip()
        self.correo_reg    = self.entry_correo2.get().strip()

        if self.nombre_actual == "" or self.codigo_actual == "" or self.correo_reg == "":
            messagebox.showwarning("Aviso", "Todos los campos son obligatorios")
            return

        valido, mensaje = self.logica.validar_correo(self.correo_reg)
        if not valido:
            messagebox.showerror("Correo inválido", mensaje)
            return

        self.limpiar_ventana()
        self.ventana.configure(bg=COLOR_FONDO)

        tk.Frame(self.ventana, bg=COLOR_ACENTO, height=6).pack(fill="x")


        canvas = tk.Canvas(self.ventana, bg=COLOR_FONDO, highlightthickness=0)
        scroll = tk.Scrollbar(self.ventana, orient="vertical", command=canvas.yview)
        self.frame_notas = tk.Frame(canvas, bg=COLOR_PANEL)

        self.frame_notas.bind("<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=self.frame_notas, anchor="nw")
        canvas.configure(yscrollcommand=scroll.set)
        canvas.pack(side="left", fill="both", expand=True, padx=(40, 0), pady=20)
        scroll.pack(side="right", fill="y")

        tk.Label(self.frame_notas, text="📊  Ingreso de Notas",
                 font=FUENTE_TITULO,
                 bg=COLOR_PANEL, fg=COLOR_TEXTO).pack(pady=(20, 5))

        tk.Label(self.frame_notas, text=f"Estudiante: {self.nombre_actual}",
                 font=FUENTE_PEQUEÑA,
                 bg=COLOR_PANEL, fg=COLOR_TEXTO_GRIS).pack()


        def seccion(titulo):
            tk.Frame(self.frame_notas, bg=COLOR_BORDE, height=1).pack(fill="x", padx=20, pady=10)
            tk.Label(self.frame_notas, text=titulo,
                     font=FUENTE_SUBTITULO,
                     bg=COLOR_PANEL, fg=COLOR_ACENTO).pack(pady=(5, 3))

        def campo(label):
            tk.Label(self.frame_notas, text=label,
                     font=FUENTE_PEQUEÑA,
                     bg=COLOR_PANEL, fg=COLOR_TEXTO_GRIS).pack(anchor="w", padx=40, pady=(8, 2))
            e = self.crear_entry(self.frame_notas, ancho=25)
            e.pack(padx=40)
            return e

        seccion("── Corte 1  (35%) ──")
        self.c1_trabajos = campo("Trabajos (30%):")
        self.c1_quices   = campo("Quices   (30%):")
        self.c1_parcial  = campo("Parcial  (40%):")

        seccion("── Corte 2  (35%) ──")
        self.c2_trabajos = campo("Trabajos (30%):")
        self.c2_quices   = campo("Quices   (30%):")
        self.c2_parcial  = campo("Parcial  (40%):")

        seccion("── Final  (30%) ──")
        self.cf_trabajos = campo("Trabajos (30%):")
        self.cf_quices   = campo("Quices   (30%):")
        self.cf_parcial  = campo("Parcial  (40%):")

        tk.Frame(self.frame_notas, bg=COLOR_BORDE, height=1).pack(fill="x", padx=20, pady=15)

        self.crear_boton(self.frame_notas, "💾  Calcular y Guardar",
                         self.calcular_y_guardar).pack(pady=5)
        self.crear_boton(self.frame_notas, "← Volver",
                         self.pantalla_registro, color="#374151").pack(pady=(5, 20))

    def calcular_y_guardar(self):
        """Lee las notas ingresadas, calcula la definitiva y guarda el registro."""
        campos = {
            "C1 Trabajos":    self.c1_trabajos.get(),
            "C1 Quices":      self.c1_quices.get(),
            "C1 Parcial":     self.c1_parcial.get(),
            "C2 Trabajos":    self.c2_trabajos.get(),
            "C2 Quices":      self.c2_quices.get(),
            "C2 Parcial":     self.c2_parcial.get(),
            "Final Trabajos": self.cf_trabajos.get(),
            "Final Quices":   self.cf_quices.get(),
            "Final Parcial":  self.cf_parcial.get(),
        }

        notas = {}
        for nombre, valor in campos.items():
            valido, resultado = self.logica.validar_nota(valor)
            if not valido:
                messagebox.showerror("Nota inválida", f"{nombre}: {resultado}")
                return
            notas[nombre] = resultado

        corte1 = self.logica.calcular_nota_corte(
            notas["C1 Trabajos"], notas["C1 Quices"], notas["C1 Parcial"])
        corte2 = self.logica.calcular_nota_corte(
            notas["C2 Trabajos"], notas["C2 Quices"], notas["C2 Parcial"])
        final  = self.logica.calcular_nota_corte(
            notas["Final Trabajos"], notas["Final Quices"], notas["Final Parcial"])

        definitiva = self.logica.calcular_definitiva(corte1, corte2, final)
        aprobado   = self.logica.verificar_aprobado(definitiva)

        exito = self.db.insertar_estudiante(
            self.nombre_actual, self.codigo_actual,
            self.correo_reg, round(definitiva, 2), aprobado)

        if not exito:
            messagebox.showerror("Error", "El código o correo ya existe")
            return

        messagebox.showinfo("Resultado",
            f"Estudiante:  {self.nombre_actual}\n"
            f"Corte 1:     {round(corte1, 2)}\n"
            f"Corte 2:     {round(corte2, 2)}\n"
            f"Final:       {round(final, 2)}\n"
            f"Definitiva:  {round(definitiva, 2)}\n"
            f"Estado:      {aprobado}")

        self.pantalla_menu()

    def pantalla_ver_estudiantes(self):
        """Muestra una lista de los estudiantes registrados en la base de datos."""
        self.limpiar_ventana()
        self.ventana.configure(bg=COLOR_FONDO)

        tk.Frame(self.ventana, bg=COLOR_ACENTO, height=6).pack(fill="x")

        tk.Label(self.ventana, text="📊  Estudiantes Registrados",
                 font=FUENTE_TITULO,
                 bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=20)

        frame_contenedor = tk.Frame(self.ventana, bg=COLOR_FONDO)
        frame_contenedor.pack(fill="both", expand=True, padx=30)

        canvas = tk.Canvas(frame_contenedor, bg=COLOR_PANEL, highlightthickness=0)
        scroll = tk.Scrollbar(frame_contenedor, orient="vertical", command=canvas.yview)
        frame_lista = tk.Frame(canvas, bg=COLOR_PANEL)

        frame_lista.bind("<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=frame_lista, anchor="nw")
        canvas.configure(yscrollcommand=scroll.set)
        canvas.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        for col, (texto, ancho) in enumerate([
            ("Nombre", 25), ("Código", 15), ("Definitiva", 12), ("Estado", 12)
        ]):
            tk.Label(frame_lista, text=texto,
                     font=FUENTE_SUBTITULO, width=ancho,
                     bg=COLOR_ACENTO, fg=COLOR_TEXTO,
                     anchor="w", padx=5).grid(row=0, column=col, padx=2, pady=2)

        estudiantes = self.db.obtener_estudiantes()

        if not estudiantes:
            tk.Label(frame_lista, text="No hay estudiantes registrados",
                     font=FUENTE_NORMAL,
                     bg=COLOR_PANEL, fg=COLOR_TEXTO_GRIS).grid(
                     row=1, columnspan=4, pady=20)
        else:
            for i, est in enumerate(estudiantes, start=1):
                bg = COLOR_PANEL if i % 2 == 0 else "#252538"
                color = COLOR_EXITO if est[5] == "Aprobado" else COLOR_ERROR
                tk.Label(frame_lista, text=est[1], width=25,
                         bg=bg, fg=COLOR_TEXTO, anchor="w", padx=5).grid(
                         row=i, column=0, padx=2, pady=1)
                tk.Label(frame_lista, text=est[2], width=15,
                         bg=bg, fg=COLOR_TEXTO, anchor="w").grid(
                         row=i, column=1, padx=2, pady=1)
                tk.Label(frame_lista, text=est[4], width=12,
                         bg=bg, fg=COLOR_TEXTO, anchor="w").grid(
                         row=i, column=2, padx=2, pady=1)
                tk.Label(frame_lista, text=est[5], width=12,
                         bg=bg, fg=color, anchor="w",
                         font=("Segoe UI", 11, "bold")).grid(
                         row=i, column=3, padx=2, pady=1)

        self.crear_boton(self.ventana, "← Volver al Menú",
                         self.pantalla_menu, color="#374151").pack(pady=15)

    def limpiar_ventana(self):
        """Limpia todos los widgets actuales de la ventana para cambiar de pantalla."""
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def salir(self):
        """Cierra la base de datos y destruye la ventana principal."""
        self.db.cerrar()
        self.ventana.destroy()

    def ejecutar(self):
        """Inicia el bucle principal de Tkinter para mostrar la aplicación."""
        self.ventana.mainloop()

app = App()
app.ejecutar()    

            

        