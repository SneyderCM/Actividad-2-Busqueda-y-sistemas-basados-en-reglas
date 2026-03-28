from src.base_conocimiento import BaseConocimiento
from src.motor_inferencia import MotorInferencia
from src.busqueda_a_estrella import BusquedaAEstrella

def ejecutar_pruebas():
    """Ejecuta todas las pruebas del sistema"""
    
    bc = BaseConocimiento()
    motor = MotorInferencia(bc)
    a_estrella = BusquedaAEstrella(bc)
    
    print("="*70)
    print("PRUEBAS DEL SISTEMA INTELIGENTE DE RUTAS")
    print("="*70)
    
    # Prueba 1: Ruta básica
    print("\n[PRUEBA 1] Ruta: Las Americas → San Antonio")
    ruta, costo, info = a_estrella.buscar_ruta("Las Americas", "San Antonio")
    print(f"  Ruta: {ruta}")
    print(f"  Costo: {costo} km")
    print(f"  Estado: {'✅ EXITOSA' if ruta else '❌ FALLIDA'}")
    
    # Prueba 2: Ruta larga
    print("\n[PRUEBA 2] Ruta: Fatima → Aguaclara")
    ruta, costo, info = a_estrella.buscar_ruta("Fatima", "Aguaclara")
    print(f"  Ruta: {ruta}")
    print(f"  Costo: {costo} km")
    print(f"  Estado: {'✅ EXITOSA' if ruta else '❌ FALLIDA'}")
    
    # Prueba 3: Misma estación
    print("\n[PRUEBA 3] Ruta: El Jazmin → El Jazmin (mismo barrio)")
    ruta, costo, info = a_estrella.buscar_ruta("El Jazmin", "El Jazmin")
    print(f"  Ruta: {ruta}")
    print(f"  Costo: {costo} km")
    print(f"  Info: {info}")
    print(f"  Estado: {'✅ EXITOSA' if ruta else '❌ FALLIDA'}")
    
    # Prueba 4: Estación inexistente
    print("\n[PRUEBA 4] Ruta: Las Americas → BarrioFalso (inexistente)")
    ruta, costo, info = a_estrella.buscar_ruta("Las Americas", "BarrioFalso")
    print(f"  Ruta: {ruta}")
    print(f"  Info: {info}")
    print(f"  Estado: {'✅ MANEJO CORRECTO' if not ruta else '❌ DEBERÍA FALLAR'}")
    
    # Prueba 5: Reglas en hora pico
    print("\n[PRUEBA 5] Reglas activas: Las Americas → San Antonio (hora pico)")
    reglas = motor.evaluar_contexto("Las Americas", "San Antonio", hora_pico=True)
    print(f"  Reglas activas: {len(reglas)}")
    for r in reglas:
        print(f"    • {r['descripcion']}")
    
    # Prueba 6: Ruta con El Jazmin
    print("\n[PRUEBA 6] Ruta: Las Americas → El Jazmin")
    ruta, costo, info = a_estrella.buscar_ruta("Las Americas", "El Jazmin")
    print(f"  Ruta: {ruta}")
    print(f"  Costo: {costo} km")
    print(f"  Estado: {'✅ EXITOSA' if ruta else '❌ FALLIDA'}")
    
    # Prueba 7: Todos los barrios disponibles
    print("\n[PRUEBA 7] Verificación de barrios disponibles")
    barrios = bc.obtener_estaciones()
    print(f"  Barrios: {barrios}")
    print(f"  Total: {len(barrios)} barrios")
    print(f"  Estado: {'✅ EXITOSA' if len(barrios) == 5 else '❌ FALLIDA'}")
    
    print("\n" + "="*70)
    print("TODAS LAS PRUEBAS COMPLETADAS")
    print("="*70)
    

if __name__ == "__main__":
    ejecutar_pruebas()