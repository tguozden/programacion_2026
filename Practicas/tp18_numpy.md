# Trabajo Prácticp 10: Numpy

1. Imprime la versión de numpy
2. Cree un vector nulo de tamaño 10
3. ¿Cómo obtener la documentación de la función zeros de numpy desde la línea de comandos?
4. Cree un vector con valores ordenados del 10 al 49
5. Invierte el orden un vector
6. Cree una matriz 3x3 con valores que vayan del 0 al 8
7. Encuentre los índices de los elementos distintos de cero en [1,2,0,0,4,0]
8. Cree una matriz identidad 3x3
9.  Cree un array 10x10 con valores aleatorios y encuentre los valores mínimo y máximo
10. Cree un vector aleatorio de tamaño 30 y encuentre el valor medio
11. Cree un array 2D con 1 en el borde y 0 en el interior
12. ¿Cómo agregar un borde de ceros alrededor de un array existente? (de cualquier dimensión)
13. ¿Cuál es el resultado de las siguientes expresiones? Explique
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
14.  Cree una matriz 8x8 y rellénala con 0s y 1s siguiendo el patrón de blancas y negras de un tablero de ajedrez. Pista: puede usar slicing o for.
15. Cree una matriz de tablero de ajedrez 8x8 usando la función `tile`
16. Observe la diferencia en las salidas del siguiente y explique
    ```python
    print(   sum(range(5),-1))
    print(np.sum(range(5),-1))
    A = np.array([[1, 2],[3, 4]])
    print(   sum(A))
    print(np.sum(A))
    print(np.sum(A, 0))
    print(np.sum(A, 1))

    ```
17. ¿Cuáles son los resultados de las siguientes expresiones?
    ```python
    np.array(0) / np.array(0)
    np.array(0) // np.array(0)
    np.array([np.nan]*4).astype(int)
    np.array([np.nan]*4).astype(float)
    ```
18. ¿Cómo redondear un array de flotantes a N decimales?
23. ¿Cómo encontrar valores comunes entre dos arrays?
24. ¿Cómo obtener las fechas de ayer, hoy y mañana?
25. ¿Cómo obtener todas las fechas correspondientes al mes de julio de 2016?
26. Cree una matriz 5x5 con valores tal que cada fila vaya de 0 a 4
27. Cree un vector aleatorio de tamaño 10 y ordénelo
28. Comprobar si dos arrays son iguales
29. Pegue el texto siguiente en un archivo y luego obtenga el array:
    ```text
    1, 2, 3, 4, 5
    6,  ,  , 7, 8
    ,  , 9,10,11
    ```
30. ¿Cómo saber si un array 2D dado tiene columnas nulas (todos ceros)? ¿Y filas nulas?
31. Encuentre el valor más cercano a un valor dado en un array 2D aleatorio
32. Considere el vector [1, 2, 3, 4, 5], ¿cómo construir un nuevo vector con 3 ceros consecutivos intercalados entre cada valor?
33. ¿Cómo intercambiar dos filas de un array 2D?
34. Considere un array Z = [1,2,3,4,5,6,7,8,9,10,11,12,13,14], ¿cómo generar un array R = [[1,2,3,4], [2,3,4,5], [3,4,5,6], ..., [11,12,13,14]]?
35. ¿Cómo encontrar el valor más frecuente en un array?

Adaptados de https://github.com/rougier/numpy-100