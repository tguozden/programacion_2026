  # PROGRAMA DE ESTUDIO - PROGRAMACIÓN 1

Basado en los apuntes de la comisión 2, https://github.com/tguozden/programacion

## RECURSOS Y HERRAMIENTAS

- Documentación oficial de Python
- Pensando como un científico: https://openbookproject.net/thinkcs/python/english3e/
- Recursos complementarios recomendados:
  - W3Schools para ejercicios prácticos
  - Datacamp
  - geeksforgeeks

**Metodología:** Clases prácticas con ejemplos en vivo, ejercicios progresivos, enfoque en la resolución de problemas concretos. Jupyter Notebooks como entorno de desarrollo

## UNIDAD 1: INTRODUCCIÓN A PYTHON Y CONCEPTOS BÁSICOS

- Salida por pantalla `print()`
- Tipos de variables fundamentales: `int`, `float`, `str`, `list`
- Identificar tipos de datos
- Variables iterables e Indexación

## UNIDAD 2: OPERACIONES CON LISTAS

- Funciones sobre iterables: `min()`, `max()`, `sum()`, `sorted()`
- Range: `range(inicio, stop, paso)`
- Slicing: `lista[inicio:fin]`
- Métodos de listas `append()`, `pop()`, `insert()`, `copy()`, `index()`, `remove()`, `reverse()`, `sort()`
- Listas por comprensión
- Arreglos en Python Listas Tuplas Strings
- Mutabilidad de los arreglos: nociones de hash, ubicación en memoria

## UNIDAD 3: ESTRUCTURAS DE CONTROL

- Estructuras repetitivas: `while`, `break` y `continue`
- Asignación en expresiones (operador walrus `:=`)
- Operador para verificar pertenencia (`in`)

## UNIDAD 4: MANIPULACIÓN DE DATOS

- Métodos de strings avanzados `isalpha()`, `isdecimal()`, `islower()`, `isupper()`, `upper()`, `lower()`, `split()`, `join()`
- Función `isinstance()` para verificar tipos
- Ejercicios:
  - Validación de contraseñas (ejercicio integrador)
  - Procesamiento de texto: conteo de palabras y caracteres
  - Patrones con bucles anidados: pirámide de asteriscos

## UNIDAD 5: ESTRUCTURAS DE DATOS AVANZADAS

- Matrices como listas de listas
- Tuplas: creación, métodos, inmutabilidad
- Sets: Creación y operaciones básicas: `add()`, `intersection()`
- Diccionarios:
  - Creación y acceso `dict[clave]`
  - Métodos: `items()`, `keys()`, `values()`
  - Conteo de frecuencias con diccionarios
- Desempaquetado de tuplas

## UNIDAD 6: FUNCIONES

- Definición de funciones
- Parámetros y argumentos
- Variables globales vs locales
- Alcance de variables
- Tipos de argumentos:
  - Posicionales vs nombrados
  - Argumentos arbitrarios: `*args` (tupla) y `**kwargs` (diccionario)
  - Argumentos por defecto
- Notación de tipos de datos esperados (type hints)
- Forzar argumentos posicionales: `def funcion(x, y, /)`
- Documentación de funciones: docstrings y `help()`
- Desempaquetado: `*lista`, `**diccionario`
- Funciones `zip` y `enumerate`

### Ejercicios

- Sistema de cálculo de temperatura promedio
- Validador de contraseñas con múltiples criterios
- Clasificación de elementos por tipo de dato
- Contador de frecuencia de caracteres
- Identificación de mesetas en listas numéricas
- Procesamiento y análisis de texto

## UNIDAD 7: MANEJO DE ARCHIVOS Y MÓDULOS

- Importación de módulos:
  - `import modulo`
  - `from modulo import function`
  - `import modulo as alias`
- Manejo de archivos:
  - Apertura: `open(archivo, 'r'/'w')`
  - Lectura: `read()`, iteración por líneas
  - Escritura: `write()`
  - Cierre: `close()`
  - bloque `with`
- Procesamiento de texto:
  - Búsqueda de subcadenas
  - Función `find()`
  - Algoritmos de string matching

## UNIDAD 8: PROGRAMACIÓN CON MÚLTIPLES ESTRUCTURAS

- Manipulación de caracteres: funciones `ord()` y `chr()`
- Comprensiones avanzadas listas tuplas conjuntos y diccionarios
- Manejo de errores y validación
- Función `zip()` avanzada con parámetro `strict`

### EJERCICIOS INTEGRADORES

- Procesador de texto con conversión mayúsculas/minúsculas
- Sistema de validación de contraseñas con múltiples criterios
- Encriptación de textos
- Calculadora de promedios ponderados
- Sistema de búsqueda de patrones en textos
- Librería personalizada con funciones de utilidad

## UNIDAD 9: RECURSIÓN Y ALGORITMOS DE ORDENAMIENTO

- Intercambio (swap) de elementos en arreglos
- Ordenamiento por el método de burbuja, variantes
- Otros métodos de ordenamiento
- Complejidad temporal y espacial de un algoritmo: noción de orden
- Búsqueda binaria en listas ordenadas
- Recursión, definición y ejemplos (cuenta regresiva, factorial, fibonacci)
- Recursión en algoritmos de ordenamiento

## UNIDAD 10: EXCEPCIONES EN PYTHON

- Manejo básico de `try - except`
- Bloques `else` y `finally`
- Excepciones específicas
- Excepciones incorporadas (ej `FileNotFoundError`, `IndexError`, `Exception`)
- Lanzamiento de excepciones con `raise`

## UNIDAD 11: MANEJO DE FECHAS EN PYTHON

- `Date` y `datetime`
- Métodos y atributos útiles
- Incrementos temporales: `timedelta`
- Conversión a strings y viceversa: `strptime` y `strftime`
- Lectura de archivos csv

## UNIDAD 12: NUMPY: ARRAYS

- Listas y arrays: diferencias
- Data type en arrays
- Dimensiones
- Indexing y slicing
- Métodos y atributos en numpy arrays
- Operaciones vectorizadas
- Casos simples de difusión (broadcasting)
- Datetime en numpy

## UNIDAD 13: MATPLOTLIB

- Gráficos básicos con líneas
- Gráficos de puntos (Scatter plots)
- Histogramas
- Subplots y manejo de axes
- Guardar gráficas

## UNIDAD 14: ANÁLISIS DE DATOS CON PANDAS

- Arrays con índice: series
- Dataframes
- Métodos y atributos útiles en dataframes
- Manejo de fechas en pandas, datetimeindex
- Selección de datos, filtrado
- Agrupación

## UNIDAD 15: ANÁLISIS DE DATOS CON PANDAS

- Arrays con índice: series
- Dataframes
- Métodos y atributos útiles en dataframes
- Manejo de fechas en pandas, datetimeindex
- Selección de datos, filtrado
- Agrupación

## UNIDAD 16: TOPICOS AVANZADOS (tres clases aprox)

- Funciones lambda
- Map y filter
- Ámbito de variables en distintos scopes
- Funciones como argumentos
- Funciones que devuelven funciones
- Nociones de decoración
- Conceptos básicos de clases
- Clases: definición, inicialización, atributos, métodos
- Herencia en clases

## UNIDAD 17: Manejo de repositorios con git

- Repositorios locales y virtuales
- Inicialización, configuración de usuario
- Commit, push, fetch, pull
- branching
- Solución de conflictos, merge