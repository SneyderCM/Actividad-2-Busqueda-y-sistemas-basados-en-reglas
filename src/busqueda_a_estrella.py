import heapq
from src.base_conocimiento import BaseConocimiento

class BusquedaAEstrella:
    """
    Implementación del algoritmo A* para búsqueda de ruta óptima.
    Fórmula: f(n) = g(n) + h(n)
    - g(n): Costo real desde inicio hasta nodo actual
    - h(n): Heurística (distancia euclidiana estimada a la meta)
    """
    
    def __init__(self, base_conocimiento):
        self.bc = base_conocimiento
    
    def heuristica_distancia(self, estacion_actual, estacion_meta):
        """
        Calcula distancia euclidiana como heurística.
        Es admisible porque nunca sobreestima el costo real.
        """
        x1, y1 = self.bc.obtener_coordenadas(estacion_actual)
        x2, y2 = self.bc.obtener_coordenadas(estacion_meta)
        return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
    
    def buscar_ruta(self, origen, destino):
        """
        Encuentra la ruta óptima usando A*.
        Retorna: (ruta, costo_total, nodos_expandidos)
        """
        # Validar que las estaciones existen
        if origen not in self.bc.obtener_estaciones():
            return None, 0, f"Estación '{origen}' no existe"
        if destino not in self.bc.obtener_estaciones():
            return None, 0, f"Estación '{destino}' no existe"
        
        # Caso especial: misma estación
        if origen == destino:
            return [origen], 0, "Origen y destino son iguales"
        
        # Cola de prioridad: (f_score, contador, estacion, ruta, g_score)
        contador = 0
        cola = [(0, contador, origen, [origen], 0)]
        visitados = set()
        nodos_expandidos = 0
        
        while cola:
            f_score, _, estacion_actual, ruta, g_score = heapq.heappop(cola)
            
            if estacion_actual in visitados:
                continue
            
            visitados.add(estacion_actual)
            nodos_expandidos += 1
            
            # ¿Llegamos al destino?
            if estacion_actual == destino:
                return ruta, g_score, nodos_expandidos
            
            # Explorar vecinos
            conexiones = self.bc.obtener_conexiones_desde(estacion_actual)
            for conexion in conexiones:
                vecino = conexion["destino"]
                costo_arista = conexion["distancia"]
                
                if vecino in visitados:
                    continue
                
                # Calcular nuevos scores
                nuevo_g = g_score + costo_arista
                h = self.heuristica_distancia(vecino, destino)
                nuevo_f = nuevo_g + h
                
                nueva_ruta = ruta + [vecino]
                contador += 1
                heapq.heappush(cola, (nuevo_f, contador, vecino, nueva_ruta, nuevo_g))
        
        # No se encontró ruta
        return None, 0, "No existe ruta entre las estaciones"


# ============================================
# PRUEBA RÁPIDA
# ============================================
if __name__ == "__main__":
    from src.base_conocimiento import BaseConocimiento
    
    bc = BaseConocimiento()
    a_estrella = BusquedaAEstrella(bc)
    
    print("\n=== BÚSQUEDA A* ===")
    ruta, costo, info = a_estrella.buscar_ruta("Las Americas", "San Antonio")
    print(f"Ruta: {ruta}")
    print(f"Costo: {costo} km")
    print(f"Info: {info}")