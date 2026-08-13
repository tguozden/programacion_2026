# Práctica 1: Introducción a Python

### Ejercicio 1: Sintaxis vs. Semántica
- Escribe una oración que tenga semántica comprensible pero sintaxis incorrecta.
- Escribe otra oración en español que tenga sintaxis correcta pero errores semánticos.

### Ejercicio 2: Experimentando con el intérprete de Python
Usando el intérprete de Python, escribe `1 + 2` y presiona enter. Python evalúa esta expresión, muestra el resultado y luego muestra otro prompt. 

El operador `*` es para multiplicación y `**` es para potencias. Experimenta ingresando diferentes expresiones y registra lo que muestra el intérprete.

### Ejercicio 3: Errores de sintaxis
Escribe `1 2` y presiona enter. Python intenta evaluar la expresión pero no puede porque no es sintácticamente válida. En su lugar, muestra un mensaje de error similar a este:
```python
File "<interactive input>", line 1
    1 2
      ^
SyntaxError: invalid syntax
```

En muchos casos, Python indica dónde ocurrió el error de sintaxis, aunque no siempre es preciso y no da mucha información sobre qué está mal. La responsabilidad recae principalmente en que el usuario aprenda las reglas de sintaxis.

En este caso, Python se queja porque no hay operador entre los números.

### Ejercicio 4: Encuentra más errores

Busca algunos ejemplos adicionales que produzcan mensajes de error cuando los ingreses en el prompt de Python. Anota lo que ingresaste y la última línea del mensaje de error que Python devuelve.

### Ejercicio 5: Explorando strings
Escribe `print("hola")`. Python ejecuta esto, lo que tiene el efecto de imprimir las letras h-o-l-a. Observa que las comillas que usaste para encerrar el string no son parte de la salida.

Ahora escribe `"hola"` y describe el resultado. Toma nota de cuándo ves las comillas y cuándo no.

### Ejercicio 6: Error de nombre
Escribe `queso` sin las comillas. La salida será similar a esto:
```python
Traceback (most recent call last):
  File "<interactive input>", line 1, in ?
NameError: name 'queso' is not defined
```

Este es un error de tiempo de ejecución (*runtime error*): específicamente es un `NameError`. Ws un error porque el nombre `queso` no está definido.

### Ejercicio 7: Expresiones aritméticas
Escribe `6 + 4 * 9` en el prompt de Python y presiona enter. Registra lo que sucede.

### Ejercicio 8: Scripts vs. intérprete
Crea un script de Python con el siguiente contenido:
```python
6 + 4 * 9
```

¿Qué sucede cuando ejecutás este script?

Ahora cambia el contenido del script a:
```python
print(6 + 4 * 9)
```

Y ejecútalo nuevamente. ¿Qué sucedió esta vez?

Cuando se escribe una expresión en el prompt de Python, se evalúa y el resultado se muestra automáticamente en la línea siguiente, como si fuera una calculadora.

Una secuencia de comandos, o *script*, es diferente: las evaluaciones de expresiones no se muestran automáticamente, por lo que es necesario usar la función `print` para que aparezca la respuesta.

Para pensar: ¿qué ocurre en los en los bloques del intérprete interactivo jupyter? ¿Se muestra la salida de cada instrucción?


### Ejercicio 9: Manipulación de variables con strings
Toma la oración: "Todo trabajo y nada de juego hacen de Jack un chico aburrido". Almacena cada palabra en una variable separada y luego imprime la oración en una sola línea usando `print`.

### Ejercicio 10: Precedencia de operadores
Agrega paréntesis a la expresión `6 * 1 - 2` para cambiar su valor de 4 a -6.

### Ejercicio 11: Comentarios en el código
Coloca un comentario antes de una línea de código que funcionaba previamente y registra lo que sucede cuando vuelves a ejecutar el programa.

### Ejercicio 12: Asignación de variables
Inicia el intérprete de Python e ingresa `bruce + 4` en el prompt. Esto te dará un error:
```
NameError: name 'bruce' is not defined
```

Asigna un valor a `bruce` para que `bruce + 4` evalúe a 10.

### Ejercicio 5: Operador módulo
Evalúa las siguientes expresiones numéricas mentalmente y luego usa el intérprete de Python para verificar tus resultados:
```python
>>> 5 % 2
>>> 9 % 5
>>> 15 % 12
>>> 12 % 15
>>> 6 % 6
>>> 0 % 7
>>> 7 % 0
```

¿Qué sucedió con el último ejemplo? ¿Por qué? Si pudiste anticipar correctamente la respuesta de la computadora en todos excepto el último, es momento de continuar. Si no, tómate tiempo ahora para crear tus propios ejemplos. Explora el operador módulo hasta que estés seguro de que entiendes cómo funciona.

### Ejercicio 6: Problema de horas
Mirás el reloj y son exactamente las 2pm. Programas una alarma para que suene en 51 horas. ¿A qué hora sonará la alarma? 

### Ejercicio 7: Problema generalizado de horas
Escribe un programa en Python para resolver la versión general del problema anterior:
   - Pregunta al usuario a hora actual (en horas, formato 0-23), y pregunta el número de horas a esperar para la alarma. El programa debe mostrar a qué hora sonará la alarma.


