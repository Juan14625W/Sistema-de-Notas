"""Módulo de lógica de negocio para el sistema de notas.

Incluye validaciones de correo, validaciones de notas y cálculos de las notas de corte
y la nota definitiva.
"""

class Logica:
    """Formaliza las reglas de validación y cálculo usadas por la interfaz."""

    def validar_correo(self, correo):
        """Valida un correo institucional y detecta patrones suspicaces.

        Args:
            correo (str): Correo a validar.

        Returns:
            tuple[bool, str]: `(valido, mensaje)`.
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
        """Valida que la nota sea un número entre 0.0 y 5.0.

        Args:
            nota (str|int|float): Valor ingresado por el usuario.

        Returns:
            tuple[bool, float|str]: `(True, nota_convertida)` o `(False, mensaje_error)`.
        """
        try:
            nota = float(nota)
            if 0.0 <= nota <= 5.0:
                return True, nota
            return False, "la nota debe estar entre 0.0 y 5.0"
        except ValueError:
            return False, "ingrese un numero valido"

    def calcular_nota_corte(self, trabajos, quices, parcial):
        """Calcula la nota ponderada de un corte.

        Formula:
            trabajos 30%, quices 30%, parcial 40%.
        """
        return (trabajos * 0.30) + (quices * 0.30) + (parcial * 0.40)

    def calcular_definitiva(self, corte1, corte2, final):
        """Calcula la nota definitiva a partir de los tres cortes."""
        return (corte1 * 0.35) + (corte2 * 0.35) + (final * 0.30)

    def verificar_aprobado(self, definitiva):
        """Determina si la nota definitiva es aprobatoria."""
        if definitiva > 3.5:
            return "Aprobado"
        return "Reprovado"
