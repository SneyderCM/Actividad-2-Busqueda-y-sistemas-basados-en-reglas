import json
import os

class BaseConocimiento:
    """
    Representa el conocimiento del sistema de transporte masivo.
    Contiene HECHOS (estaciones/barrios, conexiones) y REGLAS (IF-THEN).
    """
    
    def __init__(self):
        self.estaciones = self._cargar_estaciones()
        self.conexiones = self._cargar_conexiones()
        self.reglas = self._definir_reglas()
    
    def _cargar_estaciones(self):
        """Carga los hechos: estaciones/barrios del sistema"""
        ruta = os.path.join(os.path.dirname(__file__), '..', 'data', 'estaciones.json')
        with open(ruta, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _cargar_conexiones(self):
        """Carga los hechos: conexiones entre barrios"""
        ruta = os.path.join(os.path.dirname(__file__), '..', 'data', 'conexiones.json')
        with open(ruta, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _definir_reglas(self):
        """
        Define las reglas lógicas IF-THEN para el sistema.
        Basado en encadenamiento hacia adelante (forward chaining).
        """
        return [
            {
                "id": 1,
                "IF": "hora_pico == True AND estacion_destino.zona == 'comercial'",
                "THEN": "alerta_trafico",
                "descripcion": "Alerta: Zona comercial en hora pico puede tener tráfico"
            },
            {
                "id": 2,
                "IF": "numero_transbordos < 2",
                "THEN": "priorizar_ruta",
                "descripcion": "Priorizar rutas con menos transbordos"
            },
            {
                "id": 3,
                "IF": "distancia_total < 15",
                "THEN": "ruta_optima",
                "descripcion": "Ruta menor a 15km es óptima"
            },
            {
                "id": 4,
                "IF": "estacion_origen == estacion_destino",
                "THEN": "misma_estacion",
                "descripcion": "Origen y destino son el mismo barrio"
            }
        ]
    
    def obtener_estaciones(self):
        """Retorna lista de nombres de estaciones/barrios"""
        return list(self.estaciones.keys())
    
    def obtener_conexiones_desde(self, estacion):
        """Retorna todas las conexiones desde una estación"""
        conexiones = []
        for conn in self.conexiones:
            if conn["origen"] == estacion:
                conexiones.append({
                    "destino": conn["destino"],
                    "distancia": conn["distancia"]
                })
            elif conn["destino"] == estacion:
                conexiones.append({
                    "destino": conn["origen"],
                    "distancia": conn["distancia"]
                })
        return conexiones
    
    def obtener_coordenadas(self, estacion):
        """Retorna coordenadas (x, y) de una estación para heurística"""
        if estacion in self.estaciones:
            datos = self.estaciones[estacion]
            return datos.get("x", 0), datos.get("y", 0)
        return 0, 0
    
    def obtener_zona(self, estacion):
        """Retorna la zona de una estación (residencial, comercial, etc.)"""
        if estacion in self.estaciones:
            return self.estaciones[estacion].get("zona", "desconocida")
        return "desconocida"
    
    def evaluar_regla(self, regla, contexto):
        """
        Evalúa una regla contra el contexto actual.
        Implementa motor de inferencia simple.
        """
        condicion = regla["IF"]
        
        # Evaluación simple de condiciones
        if "hora_pico == True" in condicion and contexto.get("hora_pico"):
            if "zona == 'comercial'" in condicion:
                destino = contexto.get("destino", "")
                zona = self.obtener_zona(destino)
                return zona == "comercial"
        
        if "estacion_origen == estacion_destino" in condicion:
            return contexto.get("origen") == contexto.get("destino")
        
        return False


# ============================================
# PRUEBA RÁPIDA
# ============================================
if __name__ == "__main__":
    bc = BaseConocimiento()
    print("=== BASE DE CONOCIMIENTO ===")
    print(f"Barrios: {bc.obtener_estaciones()}")
    print(f"Conexiones desde Las Americas: {bc.obtener_conexiones_desde('Las Americas')}")
    print(f"Reglas definidas: {len(bc.reglas)}")