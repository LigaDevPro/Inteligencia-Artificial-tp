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
