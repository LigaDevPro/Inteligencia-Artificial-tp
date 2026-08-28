import pandas as pd
import numpy as np

ARCHIVO_ENTRADA = "Video_Games_Sales_as_at_22_Dec_2016.csv"
ARCHIVO_SALIDA = "Video_Games_Sales_clean.csv"

ANIO_MINIMO_VALIDO = 1970
ANIO_MAXIMO_VALIDO = 2016  # el dataset se recolecto a fines de 2016

print("\n================ CARGANDO DATASET ================\n")

df = pd.read_csv(
    ARCHIVO_ENTRADA,
    sep=","
)

filas_originales = df.shape[0]
columnas_originales = df.shape[1]

print("=============== DATASET ORIGINAL ===============")
print(f"Filas originales: {filas_originales}")
print(f"Columnas originales: {columnas_originales}")

df = df.loc[:, ~df.columns.duplicated()]

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace(r"[^a-zA-Z0-9_]", "", regex=True)
)

print("\nColumnas estandarizadas correctamente.")

filas_antes = len(df)

df.drop_duplicates(inplace=True)
df.dropna(how="all", inplace=True)

filas_eliminadas = filas_antes - len(df)

print("\nFilas duplicadas y vacías eliminadas.")
print(f"Filas eliminadas: {filas_eliminadas}")

columnas_texto = df.select_dtypes(exclude="number").columns

for col in columnas_texto:

    df[col] = df[col].astype(str)

    df[col] = df[col].str.strip()

    df[col] = df[col].replace(
        ["", " ", "nan", "none", "null"],
        np.nan
    )

print("\nTexto normalizado correctamente.")

print("\n================ CASOS ESPECIALES DEL DATASET ================\n")

filas_antes_criticas = len(df)

df.dropna(subset=["name", "genre"], inplace=True)

filas_sin_identificacion = filas_antes_criticas - len(df)

print(f"Filas sin name/genre eliminadas: {filas_sin_identificacion}")

df["user_score"] = df["user_score"].replace("tbd", np.nan)
df["user_score"] = pd.to_numeric(df["user_score"], errors="coerce")

print("\nColumna 'user_score' convertida a numérica (los 'tbd' pasaron a NaN).")

print("\n================ VALIDACIÓN DE RANGOS ================\n")

columnas_ventas = ["na_sales", "eu_sales", "jp_sales", "other_sales", "global_sales"]
ventas_invalidas = {}

for col in columnas_ventas:
    invalidos = df[col] < 0
    ventas_invalidas[col] = int(invalidos.sum())
    df.loc[invalidos, col] = np.nan
    print(f"{col}: {ventas_invalidas[col]} valores negativos corregidos")

critic_invalidos = ((df["critic_score"] < 0) | (df["critic_score"] > 100)).sum()
df.loc[(df["critic_score"] < 0) | (df["critic_score"] > 100), "critic_score"] = np.nan
print(f"\ncritic_score fuera de rango (0-100): {critic_invalidos}")

user_invalidos = ((df["user_score"] < 0) | (df["user_score"] > 10)).sum()
df.loc[(df["user_score"] < 0) | (df["user_score"] > 10), "user_score"] = np.nan
print(f"user_score fuera de rango (0-10): {user_invalidos}")

anio_invalido = (df["year_of_release"] < ANIO_MINIMO_VALIDO) | (df["year_of_release"] > ANIO_MAXIMO_VALIDO)
anios_invalidos = int(anio_invalido.sum())
df.loc[anio_invalido, "year_of_release"] = np.nan
print(f"year_of_release fuera de rango ({ANIO_MINIMO_VALIDO}-{ANIO_MAXIMO_VALIDO}): {anios_invalidos}")

df["year_of_release"] = df["year_of_release"].astype("Int64")

print("\nColumna 'year_of_release' convertida a entero (Int64, admite nulos).")

columnas_antes = len(df.columns)

df.dropna(axis=1, how="all", inplace=True)

columnas_vacias_eliminadas = columnas_antes - len(df.columns)

print(f"\nColumnas vacías eliminadas: {columnas_vacias_eliminadas}")

columnas_eliminadas = []

for col in df.columns:

    if df[col].nunique(dropna=True) <= 1:

        columnas_eliminadas.append(col)

if columnas_eliminadas:

    df.drop(columns=columnas_eliminadas, inplace=True)

    print("\nColumnas eliminadas por poca utilidad:")

    for col in columnas_eliminadas:
        print(f"- {col}")

print("\n================ VALORES NULOS ================\n")

print(df.isnull().sum())

limite_nulos = len(df) * 0.70

columnas_antes_nulos = len(df.columns)

df = df.loc[:, df.isnull().sum() < limite_nulos]

columnas_nulos_eliminadas = columnas_antes_nulos - len(df.columns)

print("\nTratamiento de nulos finalizado.")
print(f"Columnas eliminadas por exceso de nulos: {columnas_nulos_eliminadas}")

df = df.reindex(
    sorted(df.columns),
    axis=1
)

df.reset_index(
    drop=True,
    inplace=True
)

print("\n================ DATASET LIMPIO ================")

print("\nDimensiones finales:")
print(df.shape)

print("\nTipos de datos:")
print(df.dtypes)

print("\nPrimeras filas:")
print(df.head())

print("\nÚltimas filas:")
print(df.tail())

print("\nInformación general:")
print(df.info())

df.to_csv(
    ARCHIVO_SALIDA,
    index=False
)

print("\nDataset limpio exportado correctamente.")
