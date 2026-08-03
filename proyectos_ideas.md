# Ideas para el proyecto final
Combinando las propuestas originales de la cátedra ([proyectos.md](https://github.com/tguozden/programacion_2025/blob/main/Practicas/proyectos.md)) con ideas adicionales.

---

## Análisis y visualización de datos

### Datos personales (Spotify, YouTube, uso del teléfono)
- Explorar fuentes de datos (CSV/JSON), volumen y formato.
- Cargar y limpiar con Pandas: ordenar índices/columnas, multi-índices si hace falta, formatear fechas.
- Preguntas: artistas/temas más escuchados, horarios de mayor uso, hábitos semanales.
- Gráficos: barras, líneas, torta (distribución de géneros).

### Datos públicos (clima, finanzas, deportes)
- Ejemplo: [dataset de boyas oceánicas](https://www.kaggle.com/datasets/samoilovmikhail/ocean-buoys-data-1980-2025) en Kaggle.
- Cargar y limpiar con Pandas.
- Visualizaciones: evolución temporal, mapas (`cartopy`), gráficos burbuja.

### Datos meteorológicos
- Fuente: [datos de la UNRN](https://unrnmeteo.github.io/meteo/historial.html).
- Ideas: temperatura vs. altura, rosas de viento, websocket en JS conectado a un broker MQTT para datos en vivo.

### Datos de WhatsApp
- Exportar chat sin multimedia (Configuración del chat → Exportar chat).
- Parsear el `.txt` (regex/Pandas): fecha, hora, remitente, mensaje; limpiar mensajes multilínea y multimedia omitida.
- Análisis: mensajes por persona/hora/día, longitud promedio, tiempo de respuesta entre participantes.
- Texto: palabras más frecuentes (sin stopwords), nube de palabras, emojis más usados.
- Gráficos: heatmap de actividad (hora × día), líneas en el tiempo, comparación entre participantes.

### Datos de bienestar digital (uso del teléfono)
- Fuente: "Bienestar digital" (Android) o "Tiempo de uso" (iPhone); se pueden bajar los datos?
- Preguntas: apps que más tiempo consumen, patrón semanal (¿más uso el finde?), evolución en el tiempo.
- Comparar tiempo de pantalla vs. cantidad de desbloqueos.
- Gráficos: barras apiladas por app y día, líneas de tendencia, torta por categoría de app.

## Juegos (mayor dificultad, interfaz gráfica tipo PyQt, más POO PyGame)

### Tetris simplificado
- Solo bloques cuadrados; el usuario elige dónde ubicarlos.

### Snake simplificado
- Tamaño constante, bordes periódicos, sin comida ni agregados.

### Buscaminas
- Juego estático, espera acción del jugador. Dificultad media/alta.
- Pasos sugeridos: graficar una "pared de cerámicos", clickear y cambiar de color.

### Juego de la vida de Conway (autómata celular)
- Grilla como matriz de `numpy` (0 = muerta, 1 = viva).
- Reglas: celda viva con 2-3 vecinas vivas sobrevive; celda muerta con exactamente 3 vecinas vivas nace; el resto muere.
- Condiciones de borde: fijas o periódicas (toroidal).
- Animación con `matplotlib.animation`, o interfaz interactiva para definir el estado inicial clickeando.
- Extra: patrones clásicos (planeador, "glider gun"), o generalizar a autómatas 1D de Wolfram.

### Generador/resolvedor de sudokus
- Backtracking simple, interfaz para ingresar y resolver.

---

## Simulaciones de física

### Tiro oblicuo / caída de proyectiles
- Ecuaciones de cinemática, con o sin rozamiento del aire.
- Interfaz para elegir ángulo y velocidad inicial, graficar trayectoria.
- Animación con `matplotlib.animation`.

### Sistema de N cuerpos (gravedad)
- 2-3 cuerpos con ley de gravitación universal.
- Ecuaciones diferenciales con `scipy.integrate`.
- Animación de las órbitas.

### Péndulo simple o doble
- El doble péndulo es visualmente espectacular (caos determinista).
- Ecuaciones diferenciales con `scipy.integrate`.
- *Más desafiante, muy vistoso.*

### Colisiones elásticas en 2D
- Partículas rebotando en una caja, chocando entre sí.
- Practica vectores y detección de colisiones.

**Herramientas comunes:** `numpy` para el cálculo, `matplotlib.animation` o `plotly` para animar; si se quiere interactivo en la web, se puede pasar a JavaScript con canvas.

---

## Otras

### atos de objetos espaciales
- APIs (ej. NASA) para posición en tiempo real de la ISS.
- Combinar con datos astronómicos de `pyephem`.

---

## Notas generales
- Trabajo en lo posible grupos de máximo dos alumnos, con repositorio propio y `README.md` documentando el proceso.
- Los juegos y simulaciones con interfaz gráfica suelen requerir POO (no visto en profundidad en la materia, pero se puede encarar en versión simplificada).
