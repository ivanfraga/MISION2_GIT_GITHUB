# Proyecto IA — Clasificador de flores
Prototipo de clasificación con el dataset Iris integrado en scikit-learn. Se utiliza para practicar Git/GitHub, no para evaluar calidad predictiva.

## Requisitos
- Python 3.10 o superior
- Git

## Instalación
```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Ejecución
Ejecuta siempre los comandos desde la raíz del proyecto (donde está `requirements.txt`).

```bash
python -m src.predictor
```
Salida esperada: `Predicción: 0 | Clase real: 0`

```bash
python -m unittest discover -s tests -v
```
Salida esperada: `Ran 2 tests ... OK`

## Estructura
- `src/predictor.py`: entrenamiento mínimo y predicción.
- `src/metricas.py`: funciones auxiliares para ampliar.
- `tests/`: pruebas de partida.

## Colaboración
Usad ramas `feature/*`, Pull Requests y revisiones de compañeros.
