# Construcción de proyectos en Python
## Programación 1 — Comisión 2

---

## 1. Módulos: la unidad básica de un proyecto

Un **módulo** no es más que un archivo `.py`. Cuando el proyecto crece, se suele separar el código en varios módulos, que se conectan con `import`.

Ejemplo:
```python
# saludos.py
def saludar(nombre):
    print(f"Hola, {nombre}!")
```
```python
# main.py
import saludos

saludos.saludar("Mundo")
```
---
Formas de importar:

```python
import saludos                    # saludos.saludar(...)
from saludos import saludar       # saludar(...)
import saludos as sd              # sd.saludar(...)
```

### ¿Adónde se buscan los módulos?

Al ejecutar `import algunacosa`, Python busca en este orden:

1. Si ya lo importó antes en esta misma ejecución, lo reutiliza (no lo vuelve a leer).
2. Si es un módulo interno (*built-in*) del propio Python (como `sys`), lo usa directo.
3. Si no, recorre la lista `sys.path` — un listado de carpetas — buscando un archivo `algunacosa.py`. Esa lista incluye, **la carpeta donde está el script que estás ejecutando**.

```python
import sys
print(sys.path)
```

`import saludos` funciona porque `saludos.py` está en la misma carpeta que `main.py`. Si no lo encuentra el error que devuelve es  `ModuleNotFoundError`.

---

## 2. El ambiente de ejecución: `__main__`

Todo módulo tiene una variable especial (también llamadas variales *dunder*) llamada `__name__` (es un string). Su valor depende de *cómo* se está usando el archivo `.py`:

- Si se ejecuta directamente (`python saludos.py`), `__name__` vale `"__main__"`.
- Si se importa desde otro archivo, `__name__` es `"saludos"` (el nombre del módulo).

Esto nos permite escribir un archivo que funcione de las dos formas: como módulo reutilizable y script ejecutable, sin que el código de prueba se dispare cuando alguien solo quiere importar tus funciones.

```python
# saludos.py
def saludar(nombre):
    print(f"Hola, {nombre}!")

if __name__ == "__main__":
    # esto SOLO se ejecuta si corrés "python saludos.py" directamente
    saludar("Test")
```

Si otro archivo hace `import saludos`, ese `saludar("Test")` no se ejecuta. Es una forma prolija de separar "la lógica" de "la prueba/ejecución".

---

## 3. Entrada por parámetros: módulo `sys`

Habíamos visto que una manera de pasar parámetros a un programa era con la función `input()`. Otra forma habitual muy usada en la práctica es pasar los datos **al momento de ejecutar el script**, desde la terminal:

```bash
python saludos.py Juan
```

Para leer eso dentro del script, usamos `sys.argv`: una lista con los argumentos que se pasaron.

```python
import sys

print(sys.argv)
# ['saludos.py', 'Juan']
```

- `sys.argv[0]` es siempre el nombre del script.
- `sys.argv[1]`, `sys.argv[2]`, etc. son los argumentos que pasamos nosotros.
- **todos** llegan como objetos `str`, hay que convertirlos (parsear!) con `int()` o `float()` si fuera necesario.

```python
import sys

nombre = sys.argv[1]
print(f"Hola, {nombre}!")
```

Si el script necesita un argumento y no se lo pasamos, `sys.argv[1]` da error `IndexError` — algo a tener en cuenta para validar la entrada.


---

## Para leer más

- [Módulos — Tutorial oficial de Python](https://docs.python.org/es/3/tutorial/modules.html) — el capítulo del tutorial oficial que cubre `import`, `sys.path` y cómo se organiza un módulo.
- [`sys` — Documentación oficial](https://docs.python.org/es/3/library/sys.html) — referencia completa del módulo `sys`, incluye `sys.argv` y `sys.path`.
- [`__main__` — Documentación oficial](https://docs.python.org/es/3/library/__main__.html) — explica en detalle qué es el módulo `__main__` y el patrón `if __name__ == "__main__":`.
- [Línea de comandos y entorno — Documentación oficial](https://docs.python.org/es/3/using/cmdline.html) — cómo Python arma `sys.argv` y `sys.path` al ejecutar un script desde la terminal.
- [Breve recorrido por la Biblioteca Estándar — sys.argv](https://docs.python.org/es/3/tutorial/stdlib.html) — ejemplo corto y directo de `sys.argv` en el tutorial oficial.
