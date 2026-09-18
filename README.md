# Proyecto Video Games Sales - Inteligencia Artificial (ISPC)

Este repositorio contiene el desarrollo del proyecto para la materia Inteligencia Artificial /
Ciencia de Datos, sobre un dataset de ventas de videojuegos (1980-2016).

---

## Integrantes

* Agustin Gibaut
* Ignacio Matias Cantoni
* Agustin Ceballos
* Miguel Scaccia
* Pablo Peralta
* Rodrigo Rojas

---

## Fase 1 - Comprensión de los Datos

Limpieza de datos y análisis exploratorio (EDA) para identificar y clasificar variables, detectar
patrones y obtener hallazgos preliminares.

### Objetivo

Realizar la limpieza y el análisis exploratorio del dataset con el fin de identificar y clasificar
sus variables (numéricas y categóricas), comprender su estructura, detectar patrones y obtener
hallazgos preliminares a partir de los datos disponibles.

### ✔️ Limpieza de Datos

Se implementó un script (`app.py`) que toma el dataset original y produce una versión limpia,
incluyendo:

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

Los resultados obtenidos permiten comprender mejor la composición del dataset: las variables de
ventas están fuertemente sesgadas hacia pocos títulos exitosos, casi la mitad de los juegos no tiene
puntaje de la crítica, y existe una relación positiva (aunque no estricta) entre buena crítica y
mayores ventas. Estos hallazgos son un punto de partida para etapas posteriores del análisis.

### ✔️ Visualización de Datos

Se desarrollaron gráficos simples para representar visualmente la información obtenida:

* Valores faltantes por columna.
* Evolución de lanzamientos de juegos por año.
* Top 10 plataformas por cantidad de juegos.
* Ventas globales totales por género.
* Ventas promedio según rango de puntaje de la crítica.
* Proporción de juegos con y sin puntaje de la crítica.

### Archivos Entregables (Fase 1)

* `app.py`
* `Video_Games_Sales_clean.csv`
* `analisis_exploratorio.ipynb`

---

## Fase 2 - Modelado y Evaluación (Regresión)

A partir de las conclusiones de la Fase 1, se entrenó y evaluó un modelo de **regresión** que
predice `global_sales` (ventas globales en millones de copias).

### Objetivo

Implementar un modelo alineado con el problema definido en el EDA, dividiendo el dataset en
train/test, entrenando el algoritmo solo con los datos de entrenamiento y evaluando su desempeño
sobre datos no vistos.

### ✔️ Variable objetivo y features

* **Variable objetivo:** `global_sales`, numérica continua → problema de regresión.
* **Features usadas:** `critic_score`, `critic_count`, `user_score`, `user_count`,
  `year_of_release`, `platform`, `genre`, `rating`.
* **Features excluidas:** `na_sales`/`eu_sales`/`jp_sales`/`other_sales` (suman exactamente
  `global_sales`, sería fuga de datos) y `name`/`publisher`/`developer` (identificadores de alta
  cardinalidad).

### ✔️ Entrenamiento

* División train/test 80/20 con `random_state=42` fijo.
* Modelos entrenados solo con datos de entrenamiento: `LinearRegression` (base) y
  `RandomForestRegressor` (alternativa no lineal), ambos con hiperparámetros por defecto.

### ✔️ Evaluación de Desempeño

Métricas calculadas sobre el conjunto de test:

| Modelo | MAE | RMSE | R² |
|---|---|---|---|
| LinearRegression | 0.71 | 1.40 | 0.28 |
| RandomForestRegressor | 0.52 | 1.26 | 0.42 |

`RandomForestRegressor` obtiene mejor desempeño en las tres métricas, lo que sugiere relaciones no
lineales entre las features y las ventas. El R² moderado (~0.42) es esperable: el dataset no incluye
factores clave como marketing o fuerza de la franquicia. La interpretación completa está en el
notebook.

### Archivos Entregables (Fase 2)

* `modelado.ipynb`

---

## Herramientas Utilizadas

* Python
* Pandas
* NumPy
* Matplotlib
* scikit-learn
* Jupyter Notebook

---

## Dataset

El análisis se realizó sobre `Video_Games_Sales_as_at_22_Dec_2016.csv`, un dataset de ventas de
videojuegos por región (Norteamérica, Europa, Japón, otros) junto con puntajes de crítica y de
usuarios, del cual se generó una versión limpia (`Video_Games_Sales_clean.csv`) mediante `app.py`.

---

## Estado del Proyecto

**Fase 1:**
✔️ Limpieza de datos
✔️ Análisis descriptivo
✔️ Detección de patrones
✔️ Visualización de datos
✔️ Primeras conclusiones

**Fase 2:**
✔️ División train/test
✔️ Entrenamiento del modelo
✔️ Evaluación de desempeño (MAE, MSE, RMSE, R²)
✔️ Interpretación de resultados
