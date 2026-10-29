# Trabajo Práctico — Etapa 2
## Gráficos y estadísticas

En esta etapa se agregan gráficos y nuevas secciones al notebook `informe.ipynb`.



## Requerimientos

### 1. Lanzamientos en el tiempo

- gráfico de barras con lo que devuelve `lanzamientos_por_anio` (eje X año, eje Y cantidad de satélites lanzados).
- recibe dos diccionarios `{año: cantidad}` y dibuja barras apiladas, con leyenda. Los años que falten en uno de los diccionarios cuentan como 0. Sirve, por ejemplo, para comparar Starlink con el resto.

### 2. Grupos

   gráfico de barras con la altitud media de cada grupo, a partir de lo que devuelve `resumen_por_grupo`.

### 3. Altitudes

-  histograma de las altitudes entre 200 y 2.000 km, con bins de `ancho_bin` km. Pista: `bins=np.arange(200, 2000 + ancho_bin, ancho_bin)`. 
-  histograma de todas las altitudes con el eje X en escala logarítmica y bins de ancho logarítmico. Pista: `np.logspace` y `plt.xscale("log")`.

### 4. Inclinaciones

- histograma de `"INCLINATION"` de 0° a 180°, con bins de 1°.

---

## El notebook

Agregar estas secciones, cada una con el gráfico y una o dos oraciones que respondan las preguntas:

1. **Lanzamientos por año**: barras por año y barras apiladas Starlink vs. resto, de 1990 a 2026. ¿Desde qué año cambia la escala? ¿Qué parte de ese cambio explica Starlink?
2. **Altura media por grupo**: ¿qué grupos están en órbita baja y cuáles más arriba?
3. **Altitudes en órbita baja**: con `ancho_bin=10` y con `ancho_bin=50`. ¿Qué se ve con uno que no se ve con el otro? ¿A qué alturas se concentran los satélites?
4. **Todas las altitudes**: histograma logarítmico. Identifiquen los picos y relaciónenlos con los tipos de órbita (LEO, MEO, GEO).
5. **Inclinaciones**: ¿qué inclinaciones se repiten más? Filtren por grupo (por ejemplo Starlink y GPS) y vean a qué grupo corresponde cada pico.

---

## Tema libre

Cada grupo propone **un gráfico propio** sobre los datos, que responda una pregunta que les interese.

Antes de programarlo, envíen al docente:

- la pregunta que quieren responder;
- qué tipo de gráfico van a hacer y con qué datos.


---

## Tópico avanzado (opcional): pandas

Rehacer algunos resultados con pandas, en un módulo aparte `analisis_pandas.py`:

- `a_dataframe(registros, satelites)`: devuelve un `DataFrame` con una fila por satélite y columnas `nombre`, `anio`, `grupo`, `inclinacion`, `altitud_km`, `tipo_orbita`. Pista: `pd.DataFrame(lista_de_diccionarios)`.
- `resumen_por_grupo_pd(df)`: el mismo resultado que `resumen_por_grupo`, usando `df.groupby("grupo")["altitud_km"].agg(...)`.
- `lanzamientos_por_grupo_pd(df)`: tabla con un año por fila y un grupo por columna, usando `groupby(["anio", "grupo"]).size().unstack(fill_value=0)`.
- repetir el análisis de altura de satélites por grupo usando boxplots

---
