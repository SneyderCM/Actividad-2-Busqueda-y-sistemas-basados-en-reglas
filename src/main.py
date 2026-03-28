from src.base_conocimiento import BaseConocimiento
from src.motor_inferencia import MotorInferencia
from src.busqueda_a_estrella import BusquedaAEstrella

def mostrar_menu():
    """Muestra el menú de opciones al usuario"""
    print("\n" + "="*60)
    print("🚌 SISTEMA INTELIGENTE DE RUTAS - TRANSPORTE MASIVO")
    print("="*60)
    print("Basado en Benítez (2014) - Capítulos 2, 3, 9")
    print("="*60)

def main():
    """Función principal del sistema"""
    mostrar_menu()
    
    # Inicializar componentes del sistema inteligente
    print("\n🔧 Inicializando sistema...")
    bc = BaseConocimiento()
    motor = MotorInferencia(bc)
    a_estrella = BusquedaAEstrella(bc)
    print("✅ Sistema listo!")
    
    # Mostrar barrios disponibles
    print(f"\n📍 Barrios disponibles: {', '.join(bc.obtener_estaciones())}")
    
    # Solicitar origen y destino
    print("\n--- PLANIFICAR RUTA ---")
    origen = input("Barrio de ORIGEN: ").strip().title()
    destino = input("Barrio de DESTINO: ").strip().title()
    
    # Preguntar si es hora pico
    hora_pico_input = input("¿Es hora pico? (s/n): ").strip().lower()
    hora_pico = hora_pico_input == 's' or hora_pico_input == 'si'
    
    # Evaluar reglas con motor de inferencia
    print("\n🧠 Evaluando reglas de conocimiento...")
    contexto = {
        "origen": origen,
        "destino": destino,
        "hora_pico": hora_pico
    }
    reglas_activas = motor.evaluar_contexto(origen, destino, hora_pico)
    
    if reglas_activas:
        print(f"✅ {len(reglas_activas)} regla(s) activada(s):")
        for regla in reglas_activas:
            print(f"   • {regla['descripcion']}")
    else:
        print("ℹ️  No hay reglas especiales aplicables")
    
    # Buscar ruta óptima con A*
    print("\n🔍 Buscando ruta óptima con A*...")
    ruta, costo, info = a_estrella.buscar_ruta(origen, destino)
    
    # Mostrar resultados
    print("\n" + "="*60)
    print("📊 RESULTADOS")
    print("="*60)
    
    if ruta:
        print(f"✅ Ruta encontrada: {' → '.join(ruta)}")
        print(f"📏 Distancia total: {costo} km")
        print(f"🔢 Nodos expandidos: {info}")
        
        # Recomendaciones del motor de inferencia
        recomendaciones = motor.recomendar_ruta(ruta, contexto)
        if recomendaciones:
            print("\n💡 Recomendaciones:")
            for rec in recomendaciones:
                print(f"   {rec}")
    else:
        print(f"❌ Error: {info}")
    
    print("="*60)
    print("\n🎓 Este sistema implementa:")
    print("   • Base de conocimiento con reglas")
    print("   • Motor de inferencia")
    print("   • Búsqueda heurística A*")
    print("="*60)


# ============================================
# PUNTO DE ENTRADA
# ============================================
if __name__ == "__main__":
    main()