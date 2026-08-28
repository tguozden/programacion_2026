# Recuperatorio — Introducción a la Computación (examen en papel)

## Ejercicio 1 — Interpretación (10 puntos)

Leé el siguiente código con atención y respondé lo que se pide.

```python
texto = "la casa de la vecina es la mas linda"
palabras = texto.split()

conteo = {}
for p in palabras:
    if p in conteo:
        conteo[p] = conteo[p] + 1
    else:
        conteo[p] = 1

repetidas = [palabra for palabra, veces in conteo.items() if veces > 1]
repetidas.sort()

resultado = ""
for i, palabra in enumerate(repetidas):
    if i == 0:
        resultado = palabra
    else:
        resultado = resultado + "-" + palabra

print(conteo)
print(repetidas)
print(resultado)
```

- a) (4 pts) Completá el diccionario `conteo` tal como queda al final del `for`
   (todas las claves y valores).
- b) (2 pts) ¿Qué imprime `print(repetidas)`? Prestá atención al orden.
- c) (2 pts) ¿Qué imprime `print(resultado)`?
- d) (2 pts) Si en la línea `if veces > 1` cambiamos la condición por
   `veces >= 1`, ¿qué cambia en `repetidas`? Explicá sin volver a escribir
   todo el dict.

---

## Ejercicio 2 — Construcción (10 puntos)

Escribí una función `tabla_a_dict(tuplas)` que reciba una lista de tuplas
`(codigo, letra)`, donde `codigo` es un número entero (código ASCII) y
`letra` es el caracter real correspondiente, y devuelva un **diccionario**
que mapee cada caracter (obtenido con `chr(codigo)`) a su `letra`.

Por ejemplo, con:

```python
tuplas = [(83, "a"), (113, "e"), (32, "z")]
```

la función debe devolver:

```python
{"S": "a", "q": "e", " ": "z"}
```

(recordá que `chr(83)` es `"S"`, `chr(113)` es `"q"` y `chr(32)` es el
espacio `" "`).

Escribí el código completo de la función (definición, cuerpo y `return`).
No hace falta que el orden de las claves en el diccionario coincida con el
del ejemplo.

---

## Ejercicio 3 — 5 incisos - 5 puntos

Marcá la opción correcta. Solo una es correcta en cada caso.

**1.** ¿Qué devuelve `"programacion"[3:7]`?

- [ ] `"gram"`
- [ ] `"ogra"`
- [ ] `"grama"`
- [ ] `"progr"`

**2.** Dado `d = {"a": 1, "b": 2}`, ¿qué pasa al ejecutar `d["c"]`?

- [ ] Devuelve `None`
- [ ] Devuelve `0`
- [ ] Lanza un error (`KeyError`)
- [ ] Agrega `"c"` con valor `0` automáticamente

**3.** ¿Cuál de estas expresiones es `True`?

- [ ] `ord('a') < ord('z')`
- [ ] `chr(97) == 'z'`
- [ ] `'A'.lower() == 'A'`
- [ ] `ord('a') == ord('A')`

**4.** ¿Cuál de estas listas y diccionarios son *mutables* (se pueden
modificar después de creados)?

- [ ] Solo las listas
- [ ] Solo los diccionarios
- [ ] Ambos
- [ ] Ninguno de los dos

**5.** ¿Qué imprime este código?

```python
def f(lista):
    lista.append(99)

x = [1, 2, 3]
f(x)
print(x)
```

- [ ] `[1, 2, 3]`
- [ ] `[1, 2, 3, 99]`
- [ ] Error, porque `f` no tiene `return`
- [ ] `None`
