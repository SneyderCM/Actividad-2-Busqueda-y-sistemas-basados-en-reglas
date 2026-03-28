from src.base_conocimiento import BaseConocimiento

class MotorInferencia:
    """
    Motor de inferencia que evalúa reglas contra hechos.
    Implementa encadenamiento hacia adelante (forward chaining).
    """
    
    def __init__(self, base_conocimiento):
        self.bc = base_conocimiento
        self.hechos_activados = []
    
    def evaluar_contexto(self, origen, destino, hora_pico=False):
        """
        Evalúa el contexto actual contra todas las reglas.
        Retorna las reglas que se activan.
        """
        contexto = {
            "origen": origen,
            "destino": destino,
            "hora_pico": hora_pico
        }
        
        reglas_activas = []
        
        for regla in self.bc.reglas:
            if self.bc.evaluar_regla(regla, contexto):
                reglas_activas.append(regla)
                self.hechos_activados.append(regla["THEN"])
        
        return reglas_activas
    
    def recomendar_ruta(self, ruta, contexto):
        """
        Usa las reglas activas para recomendar o modificar la ruta.
        """
        recomendaciones = []
        
        for hecho in self.hechos_activados:
            if hecho == "alerta_trafico":
                recomendaciones.append("⚠️  ADVERTENCIA: La ruta pasa por zona comercial en hora pico")
            elif hecho == "priorizar_ruta":
                recomendaciones.append("✅ Ruta priorizada: pocos transbordos")
            elif hecho == "ruta_optima":
                recomendaciones.append("⭐ Ruta óptima: distancia menor a 15km")
            elif hecho == "misma_estacion":
                recomendaciones.append("ℹ️  Origen y destino son el mismo barrio")
        
        return recomendaciones
    
    def limpiar_hechos(self):
        """Limpia los hechos activados para nueva evaluación"""
        self.hechos_activados = []


# ============================================
# PRUEBA RÁPIDA
# ============================================
if __name__ == "__main__":
    bc = BaseConocimiento()
    motor = MotorInferencia(bc)
    
    print("\n=== MOTOR DE INFERENCIA ===")
    reglas = motor.evaluar_contexto("Las Americas", "San Antonio", hora_pico=False)
    print(f"Reglas activas: {len(reglas)}")
    for r in reglas:
        print(f"  - {r['descripcion']}")