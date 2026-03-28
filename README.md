# Actividad 2 - Sistema Inteligente de Rutas en Transporte Masivo

## 📋 Descripción
Sistema basado en reglas y búsqueda heurística que encuentra la mejor ruta entre dos barrios del transporte masivo local.

##  Integrante
- **Sneyder Cardona** - [ID BANNER: 100103874]

## Marco Teórico (Benítez, 2014)
Este proyecto implementa los conceptos de:
- **Capítulo 2:** Lógica y representación del conocimiento
- **Capítulo 3:** Sistemas basados en reglas (motor de inferencia)
- **Capítulo 9:** Técnicas basadas en búsquedas heurísticas (A*)

## Barrios del Sistema
| Barrio | Zona | Coordenadas (x, y) |
|--------|------|-------------------|
| Las Americas | Residencial | (0, 10) |
| El Jazmin | Residencial | (5, 8) |
| Aguaclara | Comercial | (10, 10) |
| Fatima | Residencial | (0, 5) |
| San Antonio | Comercial | (10, 0) |

## Requisitos
- Python 3.8+
- No se requieren librerías externas (solo Python estándar)

## Instalación
```bash
git clone https://github.com/tu-usuario/actividad2-transporte-masivo.git
cd actividad2-transporte-masivo

## Ejecutar Codigo
# Ejecutar el sistema principal
py -m src.main

# Ejecutar pruebas automatizadas
py -m tests.pruebas_sistema