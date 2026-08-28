# Fase 1 - Comprensión de los Datos

Este repositorio contiene el desarrollo y análisis realizado para la **Fase 1 (Comprensión de los Datos)** de la materia Desarrollo de Inteligencia Artificial.

El trabajo se basa en el estudio de un dataset de ventas de videojuegos (1980-2016), aplicando limpieza de datos y análisis exploratorio (EDA) para identificar y clasificar variables, detectar patrones y obtener hallazgos preliminares.

---

## Integrantes

* Agustin Gibaut
* Ignacio Matias Cantoni
* Agustin Ceballos
* Miguel Scaccia
* Pablo Peralta
* Rodrigo Rojas

---

## Objetivo

Realizar la limpieza y el análisis exploratorio de un dataset de ventas de videojuegos con el fin de identificar y clasificar sus variables (numéricas y categóricas), comprender su estructura, detectar patrones y obtener hallazgos preliminares a partir de los datos disponibles.

---

## Contenido del Informe

### ✔️ Limpieza de Datos

Se implementó un script (`app.py`) que toma el dataset original y produce una versión limpia, incluyendo:

* Estandarización de nombres de columnas (snake_case).
* Eliminación de filas duplicadas, vacías o sin identificación (`name`/`genre`).
* Conversión de `user_score` de texto (valor `"tbd"`) a numérico.
* Conversión de `year_of_release` a entero.
* Validación de rangos: ventas negativas, puntajes fuera de escala y años fuera del período válido.

### ✔️ Análisis Descriptivo

Se realizó una exploración general del dataset limpio incluyendo:

* Cantidad de registros y variables.
* Identificación y clasificación de variables numéricas y categóricas.
* Identificación de valores faltantes por columna.
* Estadísticas descriptivas (`describe()`) de las variables numéricas.
* Cardinalidad de las variables categóricas (plataforma, género, publisher, developer, rating).

### ✔️ Detección de Patrones

Se identificaron tendencias y relaciones relevantes dentro de los datos:

* Evolución de la cantidad de juegos lanzados por año.
* Plataformas y géneros con más juegos y más ventas acumuladas.
* Relación entre el puntaje de la crítica y las ventas globales.
* Concentración de las ventas en un puñado de títulos ("blockbusters").

### ✔️ Primeras Conclusiones

Los resultados obtenidos permiten comprender mejor la composición del dataset: las variables de ventas están fuertemente sesgadas hacia pocos títulos exitosos, casi la mitad de los juegos no tiene puntaje de la crítica, y existe una relación positiva (aunque no estricta) entre buena crítica y mayores ventas. Estos hallazgos son un punto de partida para etapas posteriores del análisis.

### ✔️ Visualización de Datos

Se desarrollaron gráficos simples para representar visualmente la información obtenida:

* Valores faltantes por columna.
* Evolución de lanzamientos de juegos por año.
* Top 10 plataformas por cantidad de juegos.
* Ventas globales totales por género.
* Ventas promedio según rango de puntaje de la crítica.
* Proporción de juegos con y sin puntaje de la crítica.

---

## Archivos Entregables

* `app.py`
* `Video_Games_Sales_clean.csv`
* `analisis_exploratorio.ipynb`
* `README.md`

---

## Herramientas Utilizadas

* Python
* Pandas
* NumPy
* Matplotlib
* Jupyter Notebook

---

## Dataset

El análisis se realizó sobre `Video_Games_Sales_as_at_22_Dec_2016.csv`, un dataset de ventas de videojuegos por región (Norteamérica, Europa, Japón, otros) junto con puntajes de crítica y de usuarios, del cual se generó una versión limpia (`Video_Games_Sales_clean.csv`) mediante `app.py`.

---

## Estado del Proyecto

✔️ Limpieza de datos
✔️ Análisis descriptivo
✔️ Detección de patrones
✔️ Visualización de datos
✔️ Primeras conclusiones
