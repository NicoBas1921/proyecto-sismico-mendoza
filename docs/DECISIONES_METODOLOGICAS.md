# Decisiones metodológicas

## Magnitud de referencia

La magnitud principal del catálogo será **Mw**.

Cada registro deberá conservar como mínimo:

- magnitud y tipo de magnitud originales;
- Mw final, cuando corresponda;
- método y referencia de conversión;
- fuente e identificador originales;
- indicadores de calidad, exclusión y deduplicación.

Los tipos `Mw`, `mww`, `mwb` y `mwr` se conservarán directamente. Las relaciones declaradas en `config/magnitudes.toml` se aplicarán a los demás tipos admitidos. Un valor no se convertirá si el tipo es desconocido o no existe una relación documentada.

## Trazabilidad

Nunca se reemplazará silenciosamente la magnitud original. El valor homogeneizado será una columna adicional y toda conversión deberá poder reconstruirse.

## Asuntos pendientes antes del catálogo v1.0

1. Incorporar los archivos fuente reales y registrar fecha, consulta y licencia.
2. Completar y verificar las referencias bibliográficas de las conversiones.
3. Definir tolerancias y prioridad de fuentes para la deduplicación.
4. Definir controles geográficos, temporales y de profundidad.
5. Evaluar completitud espacial y temporal del catálogo.

