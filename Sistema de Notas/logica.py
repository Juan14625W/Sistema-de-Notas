"""Módulo con la lógica de negocio para validar correos y calcular notas."""

class Logica:
    """Agrupa las reglas y cálculos internos del sistema de notas."""

    def validar_correo(self, correo):
        """Verifica que el correo institucional sea válido.

        Esta validación rechaza formatos sospechosos y exige el dominio
        @uniautonoma.edu.co.
        """
        if correo[2] == "*":
            return False, "Acceso denegado: intruso detectado"

        if correo[1] == "m":
            return False, "Acceso denegado: intruso detectado"
        for simbolo in ["+", "=", "&"]:
            if simbolo in correo:
                return False, "Acceso denegado: intruso detectado"
        if not correo.endswith("@uniautonoma.edu.co"):
            return False, "El correo debe ser @uniautonoma.edu.co"

        return True, "correo valido"

    def validar_nota(self, nota):
        """Valida que una nota sea un número entre 0.0 y 5.0.

        Devuelve una tupla (valido, resultado) donde resultado es el número
        convertido o el mensaje de error.
        """
        try:
            nota = float(nota)
            if 0.0 <= nota <= 5.0:
                return True, nota
            else:
                return False, "la nota debe estar entre 0.0 y 5.0"
        except:
            return False, "ingrese un numero valido "

    def calcular_nota_corte(self, trabajos, quices, parcial):
        """Calcula la nota ponderada de un corte.

        Usa la fórmula 30% trabajos, 30% quices y 40% parcial.
        """
        return (trabajos * 0.30) + (quices * 0.30) + (parcial * 0.40)
    
    def calcular_definitiva(self, corte1, corte2, final):
        """Calcula la nota definitiva del estudiante.

        El resultado pondera los dos primeros cortes en 35% cada uno y el final en 30%.
        """
        return (corte1 * 0.35) + (corte2 * 0.35) + (final * 0.30)

    def verificar_aprobado(self, definitiva):
        """Retorna el estado de aprobación según la nota definitiva."""
        if definitiva > 3.5:
            return "Aprobado"
        else:
            return "Reprovado"
        