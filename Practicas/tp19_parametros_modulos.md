# tp 19
## Proyectos en Python


En todos los ejercicios escribir un archivo `.py` y ejecutar desde la terminal pasando los argumentos correspondientes, por ejemplo:

```bash
python ejercicio1.py 10 hola 3.5 chau
```

---

# 1. Contar e imprimir argumentos

Escribir un script que:
- Muestre en pantalla **cuántos** argumentos se ingresaron (sin contar el nombre del script).
- Imprima cada argumento, uno por línea.

```bash
python ejercicio1.py rojo verde azul
```

```
Cantidad de argumentos: 3
rojo
verde
azul
```

---

# 2. Contar cuántos son enteros

Escribir un script que reciba varios argumentos por `sys.argv` y muestre **cuántos de ellos** representan un número entero.

```bash
python ejercicio2.py 10 hola 3.5 -7 chau 20
```

```
Cantidad de enteros: 2
```

Pistas:
- Todos los argumentos llegan como `str`, aunque "parezcan" números.
- `"10".isdigit()` te sirve para positivos, pero no contempla el signo `-`. Pensá cómo resolverlo (por ejemplo, con `try`/`except` al convertir con `int()`).

---

# 3. Invocar funciones ya definidas

Definir (arriba del todo del archivo) al menos dos funciones, por ejemplo:

```python
def saludar(nombre):
    print(f"Hola, {nombre}!")

def despedir(nombre):
    print(f"Chau, {nombre}!")
```

Usá `sys.argv` para que el primer argumento indique **qué función llamar** y el segundo sea el dato que esa función necesita.

```bash
python ejercicio3.py saludar Ana
python ejercicio3.py despedir Ana
```

Pista: se puede resolver con una cadena de `if`/`elif`, comparando `sys.argv[1]` contra el nombre de la acción.

---

## 4. Un archivo, dos usos

Tomar las funciones del ejercicio 3 y organizalas en un archivo `saludos.py`, agregando un bloque `if __name__ == "__main__":` que las pruebe con algún valor fijo (sin usar `sys.argv` todavía).

Después, crear un segundo archivo `main.py` que:
- Importe `saludos.py`.
- Llame a `saludar` y `despedir` con un nombre que reciba por `sys.argv`.

Verificar que al ejecutar `python saludos.py` se dispare la prueba, pero que al ejecutar `python main.py Ana` **no** se dispare esa prueba — solo lo que definiste en `main.py`.

---

# 5. Integrador: calculadora por línea de comandos

Escribir un script `calculadora.py` que reciba **tres argumentos**: dos números y una operación (`suma`, `resta`, `multiplicacion`).

```bash
python calculadora.py 8 3 suma
```

```
8 + 3 = 11
```

Requisitos:
- Definir una función por operación (`sumar`, `restar`, `multiplicar`) y usá `sys.argv[3]` para decidir cuál invocar.
- Convertir los dos primeros argumentos a número antes de operar.
- Usar `if __name__ == "__main__":`, de forma que el archivo también pueda importarse desde otro script sin que la calculadora se dispare sola.
- Adicional: si no se pasan exactamente 3 argumentos, mostrar un mensaje de error en vez de que el programa explote con `IndexError`.