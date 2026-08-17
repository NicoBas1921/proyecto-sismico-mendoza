# Proyecto Sísmico Mendoza

Repositorio para construir de forma reproducible un catálogo sísmico homogéneo de Mendoza, con **Mw como magnitud de referencia**.

## Estado

Estructura inicial del proyecto. Los datos reales de ISC, USGS e INPRES todavía no están incluidos en este repositorio.

## Flujo previsto

```text
fuentes originales
        ↓
normalización
        ↓
deduplicación
        ↓
homogeneización a Mw
        ↓
controles de calidad
        ↓
catálogo procesado
```

## Estructura

- `src/proyecto_sismico_mendoza/`: código reutilizable.
- `scripts/`: puntos de entrada para ejecutar el procesamiento.
- `config/`: reglas declarativas del catálogo y de magnitudes.
- `data/raw/`: archivos originales locales, excluidos de Git.
- `data/interim/`: resultados intermedios, excluidos de Git.
- `data/processed/`: catálogo final generado, excluido de Git.
- `tests/`: pruebas automatizadas.
- `docs/`: decisiones metodológicas y plan de trabajo.

## Inicio rápido

Requiere Python 3.11 o posterior.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e .
python -m unittest discover -s tests
```

El pipeline todavía es una base mínima. Se completará cuando estén disponibles y documentados los archivos fuente reales.

## Autoría

Proyecto grupal con fines educativos.
