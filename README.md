# Proyecto Sísmico Mendoza

Repositorio para construir y analizar de forma reproducible un catálogo sísmico
homogéneo de Mendoza, con **Mw como magnitud de referencia**.

## Estado

El proyecto incluye el catálogo procesado v1.1 en CSV y Excel, la configuración de
homogeneización de magnitudes y un primer análisis exploratorio reproducible. Los
archivos v1.1 son entradas inmutables del análisis: el notebook los lee, pero no los
modifica.

## Estructura

- `notebooks/01_eda_catalogo.ipynb`: análisis exploratorio del catálogo.
- `src/proyecto_sismico_mendoza/`: código reutilizable.
- `scripts/`: puntos de entrada para el procesamiento.
- `config/`: reglas declarativas del catálogo y de magnitudes.
- `data/raw/`: archivos originales locales.
- `data/interim/`: resultados intermedios.
- `data/processed/`: catálogo final v1.1 usado como entrada del EDA.
- `tests/`: pruebas automatizadas.
- `docs/`: decisiones metodológicas y plan de trabajo.

## Preparar el entorno en Windows

Requiere Python 3.11 o posterior. Desde PowerShell, en la raíz del repositorio:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .
```

Si PowerShell bloquea temporalmente la activación de scripts, puede habilitarla solo
para la sesión actual:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

Registrar el entorno como kernel de Jupyter es opcional, pero facilita identificarlo
en VS Code y JupyterLab:

```powershell
python -m ipykernel install --user --name proyecto-sismico-mendoza --display-name "Python (proyecto-sismico-mendoza)"
```

## Ejecutar el análisis en VS Code

1. Abrir la carpeta del repositorio en VS Code.
2. Abrir `notebooks/01_eda_catalogo.ipynb`.
3. Pulsar **Select Kernel** y elegir `.venv` o **Python (proyecto-sismico-mendoza)**.
4. Ejecutar **Run All** y comprobar que todas las celdas finalicen sin errores.

El notebook localiza automáticamente la raíz del proyecto; no contiene rutas
absolutas de una computadora particular.

## Ejecutar con JupyterLab

Con el entorno activado:

```powershell
python -m jupyter lab
```

En la interfaz, abrir `notebooks/01_eda_catalogo.ipynb`, seleccionar el kernel del
proyecto y ejecutar todas las celdas.

## Pruebas

```powershell
python -m unittest discover -s tests
```

## Alcance del EDA

El análisis documenta controles de calidad sin eliminar registros, compara el
catálogo completo con los subconjuntos QC, Mw y espacial, y produce análisis
temporales, de magnitud, profundidad, fuentes y epicentros. También incluye una
estimación exploratoria de completitud por MAXC; no constituye un análisis de riesgo
ni de peligrosidad sísmica.

## Autoría

Proyecto grupal con fines educativos.
