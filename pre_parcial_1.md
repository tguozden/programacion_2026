# Parcial piloto
## 1

Escribí un programa que le pida al usuario un número entero `n` e imprima la tabla de multiplicar de ese número del 1 al 10.

Para pedirle un número al usuario usamos:
```python
n = int(input("Ingresá un número: "))
```

Por ejemplo, para `n = 4` la salida debe ser:
```
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
...
4 x 10 = 40
```

## 2

Dada la siguiente lista:
```python
palabras = ["banana", "sol", "computadora", "luz", "elefante", "mar"]
```

Escribí un programa que recorra la lista e imprima solo las palabras que tengan más de 4 letras, en orden inverso al que aparecen.

La salida esperada es:
```
elefante
computadora
banana
```

## 3

Escribí un programa que pida números al usuario (como en el ejercicio 1) y los vaya guardando en una lista, de a uno por vez. Cuando el usuario ingrese el número `0` el programa terminará, deberá mostrar en pantalla:

- La cantidad de números ingresados (sin contar el 0)
- El mayor y el menor
- El promedio

**Atención!** No vale usar las funciones `max()` ni `min()`.