class Logica:

    def validar_correo(self,correo):
        if correo[2] =="*":
            return False,"Acceso denegado: intruso detectado"

        if correo[1] == "m":
            return False, "Acceso denegado: intruso detectado"
        for simbolo in ["+","=","&"]:
            if simbolo in correo:
                return False, "Acceso denegado: intruso detectado"
        if not correo.endswith("@uniautonoma.edu.co"):
               return False, "El correo debe ser @uniautonoma.edu.co"
        
        return True, "correo valido"
        
    def validar_nota(self,nota):
        try:
            nota = float(nota)
            if 0.0 <= nota <= 5.0:
                return True, nota
            else:
                return False, "la nota debe estar entre 0.0 y 5.0"
        except:
            return False, "ingrese un numero valido "

    def calcular_nota_corte(self,trabajos,quices,parcial):
        return(trabajos*0.30)+(quices*0.30)+(parcial*0.40)
    
    def calcular_definitiva(self,corte1,corte2,final):
        return (corte1*0.35)+(corte2*0.35)+(final*0.30)
    def verificar_aprobado(self,definitiva):
        if definitiva > 3.5:
            return "Aprobado"
        else:
            return "Reprovado"
        