# 21

> **Material de referencia**
> - Clases: [`../Clases/clase0929_path_encoding.ipynb`](../Clases/clase0929_path_encoding.ipynb) y [`../Clases/clase1001_encoding_json.ipynb`](../Clases/clase1001_encoding_json.ipynb)
> - Apuntes: [`../Apuntes/pathlib.md`](../Apuntes/pathlib.md), [`../Apuntes/encoding.md`](../Apuntes/encoding.md) y [`../Apuntes/json.md`](../Apuntes/json.md)

1. Recorrer todos los `.txt` de `datos/smn/`.
2. Leer cada uno detectando si está en `utf-8` o `cp1252`.
3. Guardar un único `salida/observaciones.json` con todas las observaciones, legible (`ensure_ascii=False`, `indent=2`) y en UTF-8.
4. Volver a abrir el JSON y mostrar las estaciones sin repetir.

**Verificación:** `Ñorquinco`, `Neuquén` y `Río Gallegos` tienen que aparecer bien escritos.
