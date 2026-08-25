# Trabajo Prácticp 10: Numpy

1. Imprime la versión de numpy y la configuración
2. Cree un vector nulo de tamaño 10
3. ¿Cómo encontrar el tamaño en memoria de un array?
4. ¿Cómo obtener la documentación de la función add de numpy desde la línea de comandos?
4. Cree un vector con valores ordenados del 10 al 49
5. Invierte el orden un vector
6. Cree una matriz 3x3 con valores que vayan del 0 al 8
7. Encuentre los índices de los elementos distintos de cero en [1,2,0,0,4,0]
8. Cree una matriz identidad 3x3
9. Cree un array 3x3x3 con valores aleatorios
10. Cree un array 10x10 con valores aleatorios y encuentre los valores mínimo y máximo
11. Cree un vector aleatorio de tamaño 30 y encuentre el valor medio
12. Cree un array 2D con 1 en el borde y 0 en el interior
13. ¿Cómo agregar un borde de ceros alrededor de un array existente? (de cualquier dimensión)
14. ¿Cuál es el resultado de las siguientes expresiones? Explique
```python
0 * np.nan
np.nan == np.nan
np.inf > np.nan
np.nan - np.nan
np.inf * np.inf
(-1) * np.inf
np.inf - np.inf
np.inf + np.inf
np.nan in np.array([np.nan]*4)
np.nan in      set([np.nan]*4)
np.nan in list([[np.nan, 2], [3, 4]])
np.nan in list([np.nan, 2, 3, 4])
0.3 == 3 * 0.1
0.1 == 10 * 0.01

```
15. Cree una matriz 5x5 con los valores 1,2,3,4 debajo de la diagonal
16. Cree una matriz 8x8 y rellénala con 0s y 1s siguiendo el patrón de blancas y negras de un tablero de ajedrez
17. Considere un array con forma (shape) (6,7,8): ¿cuál es el índice (x,y,z) del elemento número 100?
18. Cree una matriz de tablero de ajedrez 8x8 usando la función `tile`
19. Dado un array 1D, niegue todos los elementos que estén entre los índices 3 y 8 incluídos, in place (en el mismo sitio)
20. Observe la diferencia en las salidas del siguiente y explique
```python
print(   sum(range(5),-1))
print(np.sum(range(5),-1))
A = np.array([[1, 2],[3, 4]])
print(   sum(A))
print(np.sum(A))
print(np.sum(A, 0))
print(np.sum(A, 1))

```
21. ¿Cuáles son los resultados de las siguientes expresiones?
```python
np.array(0) / np.array(0)
np.array(0) // np.array(0)
np.array([np.nan]*4).astype(int)
np.array([np.nan]*4).astype(float)
```

22. ¿Cómo redondear un array de flotantes a N decimales?
23. ¿Cómo encontrar valores comunes entre dos arrays?
24. ¿Cómo obtener las fechas de ayer, hoy y mañana?
25. ¿Cómo obtener todas las fechas correspondientes al mes de julio de 2016?
26. Cree una matriz 5x5 con valores tal que cada fila vaya de 0 a 4
27. Cree un vector aleatorio de tamaño 10 y ordénelo
28. Comprobar si dos arrays son iguales
29. Cree un vector aleatorio de tamaño 10 y reemplace el valor máximo por 0
30. Obtenga el array del siguiente archivo:
```text
1, 2, 3, 4, 5
6,  ,  , 7, 8
 ,  , 9,10,11
```
31. ¿Cuál es el equivalente a enumerate para arrays de numpy?
32. ¿Cómo colocar aleatoriamente `p` elementos en un array 2D de `N` elementos?
33. Reste el valor medio de cada fila de una matriz
34. ¿Cómo saber si un array 2D dado tiene columnas nulas (todos ceros)? ¿Y filas nulas?
35. Encuentre el valor más cercano a un valor dado en un array 2D aleatorio
36. Considere el vector [1, 2, 3, 4, 5], ¿cómo construir un nuevo vector con 3 ceros consecutivos intercalados entre cada valor?
37. ¿Cómo intercambiar dos filas de un array 2D?
38. Considere un array Z = [1,2,3,4,5,6,7,8,9,10,11,12,13,14], ¿cómo generar un array R = [[1,2,3,4], [2,3,4,5], [3,4,5,6], ..., [11,12,13,14]]?
39. ¿Cómo encontrar el valor más frecuente en un array?

Adaptados de https://github.com/rougier/numpy-100