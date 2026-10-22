# Proyecto IA — Clasificador de flores Iris
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
```text
proyecto_ia/
├── .gitignore          # excluye .venv/, __pycache__/, .env y datos privados
├── README.md           # esta documentación
├── requirements.txt    # dependencias (scikit-learn)
├── src/
│   ├── __init__.py
│   ├── predictor.py    # entrenamiento mínimo (árbol de decisión) y predicción
│   └── metricas.py     # funciones de evaluación
└── tests/
    └── test_metricas.py  # pruebas de contar_aciertos
```

## Colaboración
Usad ramas `feature/*`, Pull Requests y revisiones de compañeros.

## Flujo de trabajo con Git
1. Partir de `main` actualizado: `git switch main && git pull --ff-only origin main`.
2. Crear una rama por tarea: `git switch -c feature/nombre-tarea`.
3. Hacer commits pequeños con mensajes descriptivos (`feat:`, `docs:`, `test:`).
4. Subir la rama: `git push -u origin feature/nombre-tarea`.
5. Abrir un Pull Request con descripción y evidencia de pruebas.
6. Integrar en `main` solo tras la revisión de otra persona.

## Comandos útiles
| Tarea | Comando |
|---|---|
| Ver estado | `git status` |
| Ver historial | `git log --oneline --graph --all` |
| Ver cambios | `git diff` |
| Ejecutar el proyecto | `python -m src.predictor` |
| Ejecutar tests | `python -m unittest discover -s tests -v` |
