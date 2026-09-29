# Organizando un proyecto: sys.path y el módulo os
## Programación 1 — Comisión 2

---

## 1. Agregar carpetas a `sys.path`

Si el proyecto se organiza en subcarpetas, y desde `main.py` necesitamos importar un módulo que está en otra carpeta, Python no la va a encontrar sola, porque esa carpeta no está en `sys.path`.

La solución más simple es agregarla nosotros mismos, en tiempo de ejecución:

```python
import sys
sys.path.append("mi_carpeta")

import algunacosa   # ahora sí la busca también ahí
```

Como `sys.path` es una lista común, se le puede hacer `.append(...)` como a cualquier otra. Esto hay que hacerlo **antes** del `import` que depende de esa carpeta, porque Python arma la búsqueda en el momento en el que se ejecuta el `import`.

Algo para tener en cuenta: la ruta que agregues puede ser relativa (depende desde dónde se ejecute el script) o absoluta. Para no tener sorpresas según desde qué carpeta se llama al script, conviene armar la ruta en base a la ubicación del propio archivo — y para eso usamos `os`.

---

## 2. El módulo `os`: carpetas y archivos

`os` es el módulo que da acceso a funciones del sistema operativo: dónde estamos parados, qué hay en una carpeta, armar rutas, etc.

### ¿Dónde estoy? ¿Dónde está mi script?

```python
import os

print(os.getcwd())            # carpeta desde la que se ejecutó el script
print(os.path.dirname(__file__))   # carpeta donde está el archivo .py
```

`os.getcwd()` depende de desde dónde llamás al script en la terminal; `os.path.dirname(__file__)` no cambia, siempre apunta a la carpeta del archivo. Por eso conviene usar esta segunda forma para armar rutas confiables:

```python
import sys, os

carpeta_actual = os.path.dirname(__file__)
sys.path.append(os.path.join(carpeta_actual, "mi_carpeta"))
```

`os.path.join(...)` arma la ruta uniendo partes con el separador correcto según el sistema operativo (`/` en Linux/Mac, `\` en Windows), así que siempre conviene usarlo en vez de concatenar strings a mano.

### Listar el contenido de una carpeta

```python
import os

archivos = os.listdir("datos")
print(archivos)
# ['clima.csv', 'ventas.csv', 'notas.txt']
```

`os.listdir(ruta)` devuelve una lista de strings con **todo** lo que hay en esa carpeta (archivos y subcarpetas mezclados, sin filtrar por tipo).

### Distinguir archivos de carpetas

```python
import os

for nombre in os.listdir("datos"):
    ruta = os.path.join("datos", nombre)
    if os.path.isfile(ruta):
        print(nombre, "es un archivo")
    elif os.path.isdir(ruta):
        print(nombre, "es una carpeta")
```

- `os.path.isfile(ruta)` → `True` si es un archivo.
- `os.path.isdir(ruta)` → `True` si es una carpeta.
- `os.path.exists(ruta)` → `True` si existe (archivo o carpeta).

### Contar cuántos archivos de datos hay

Como `os.listdir` no filtra por tipo de archivo, si querés quedarte solo con los `.csv`, por ejemplo, hay que filtrar vos mismo con el nombre del archivo:

```python
import os

archivos = os.listdir("datos")
csvs = [nombre for nombre in archivos if nombre.endswith(".csv")]
print(f"Hay {len(csvs)} archivos csv")
```

`str.endswith(".csv")` alcanza para filtrar por extensión en la mayoría de los casos.

### Separar nombre y extensión

```python
import os

nombre, extension = os.path.splitext("ventas.csv")
print(nombre, extension)
# ventas .csv
```

Útil si necesitás comparar o clasificar por extensión sin hacer el `.endswith(...)` a mano.

---

## Para leer más

- [`os` — Documentación oficial](https://docs.python.org/es/3/library/os.html) — referencia completa del módulo `os`.
- [`os.path` — Documentación oficial](https://docs.python.org/es/3/library/os.path.html) — funciones para trabajar con rutas (`join`, `exists`, `isfile`, `isdir`, `splitext`, etc.).
