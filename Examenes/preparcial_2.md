<!-- #parcial -->

## 1.
¿Qué se imprimirá en pantalla?

```python
# a)
def misterio(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]

a = [4, 2, 7, 1]
misterio(a)
print(a)


# b)
def f(s):
    if len(s) == 0:
        return ''
    return f(s[1:]) + s[0]

print(f('hola'))


# c)
def g(n):
    if n == 1:
        return 1
    return n * g(n - 1)

print(g(4) - g(3))

# d)
lista = [10, 3, 7, 1, 8, 4, 6]
 
resultado = [] 
i = 0
while i < len(lista):
    if lista[i] % 2 == 0:
        resultado.append(lista[i])
    i += 1
 
print(resultado[::-1]) 
```
  
## 2.

Dada la siguiente lista de palabras: `palabras = ["hola", "mundo", "python", "es", "genial", "no", "sé"]`

Construir un diccionario donde las claves sean las palabras los valores sean la cantidad de letras de cada una.

Por ejemplo, si la lista fuera `["hola", "es"]` el resultado sería:
```python
{"hola": 4, "es":2}
```

Si te sirve, se pueden construir diccionarios por comprensión, por ej.:
```python
{clave: valor for elemento in lista if condicion}
```

## 3
Escribí una función `procesar(s)` que reciba un string y devuelva uno nuevo donde:

- las letras minúsculas se conviertan a mayúsculas (sin usar `.upper()`)
- las letras mayúsculas se conviertan a minúsculas (sin usar `.lower()`)
- los dígitos se reemplacen por `'*'`
- el resto de los caracteres se dejen igual

```python
def procesar(s):
    # Tu código acá

print(procesar('Hola, Mundo!'))    # 'hOLA, mUNDO!'
print(procesar('abc123XYZ'))       # 'ABC***xyz'
print(procesar('Python 3'))        # 'pYTHON *'
```

## 4 Nivel ninja


Escribí un programa que tome las palabras de un texto y las guarde en una lista. El programa debe mostrar:


- Un diccionario de frecuencia de tamaño de palabras
- Todas las palabras ordenadas alfabéticamente


```python
texto = '''Un texto es un conjunto coherente de signos y enunciados, orales 
o escritos, que transmiten un mensaje con una intención comunicativa. 
Todo texto efectivo posee un sentido completo dentro de su contexto y 
se organiza respetando tres propiedades básicas: coherencia (unidad temática), 
cohesión (conexión entre sus partes) y adecuación (adaptación al destinatario).'''
