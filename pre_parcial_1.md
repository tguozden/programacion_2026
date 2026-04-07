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

## 4


Interpretar el siguiente código:  ¿qué se imprimirá en pantalla?

```python
lista = [10, 3, 7, 1, 8, 4, 6]

resultado = []
i = 0
while i < len(lista):
    if lista[i] % 2 == 0:
        resultado.append(lista[i])
    i += 1

print(resultado[::-1])
```
## 5

Interpretar el siguiente código:  ¿qué se imprimirá en pantalla?


```python
frase = "El caballo blanco de San Martín"

x = frase.split(" ")
y = []
for i in x:
    if len(i) > 3:
        y = y + [i]
        
print("-".join(y))
```

