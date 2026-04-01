import pandas as pd
import os
import matplotlib.pyplot as plt

# ==============================
# CONFIGURACIONES
# ==============================

ruta = "db"
output_folder = "analisis"
os.makedirs(output_folder, exist_ok=True)

log_global_path = os.path.join(output_folder, "analisis_global.txt")

columnas_excluir_contiene = [
    "_id",
    "date",
    "timestamp"
]

columnas_excluir_exactas = [
    "review_comment_message",
    "review_comment_title",
    "review_answer_timestamp",
    "order_approved_at",
    "geolocation_lat",
    "geolocation_lng"
]

# ==============================
# FUNCIONES
# ==============================

def check_column(col):
    col_lower = col.lower()

    if (
        any(p in col_lower for p in columnas_excluir_contiene) or
        any(col_lower == p for p in columnas_excluir_exactas)
    ):
        return True
    return False


def unique_values(df, log_file, output_folder):
    """Analiza valores únicos por columna y genera gráficos si corresponde."""
    for col in df.columns:
        dtype = df[col].dtype
        values = df[col].unique()
        n = len(values)

        if n < 30:
            log_file.write(f"{col} ({dtype}), {n} valores únicos: {values}\n")
        else:
            log_file.write(f"{col} ({dtype}) tiene {n} valores únicos (más de 30).\n")



def analizar_tabla(df, nombre_tabla, log_file):
    """Ejecución del análisis general de una tabla."""
    log_file.write(f"\n\n===== TABLA: {nombre_tabla.upper()} =====\n")
    log_file.write(f"Shape: {df.shape}\n\n")

    # NaNs por columna
    log_file.write("Porcentaje de NaNs por columna:\n")
    log_file.write(str((df.isna().sum() / len(df)) * 100) + "\n\n")

    # Duplicados
    duplicados = df.duplicated().sum()
    log_file.write(f"Duplicados encontrados: {duplicados}\n")
    if duplicados > 0:
        log_file.write("Ejemplo de duplicado:\n")
        log_file.write(str(df[df.duplicated()].head(1)) + "\n\n")
    else:
        log_file.write("No se encontraron duplicados.\n\n")

    # Valores únicos
    log_file.write("Valores únicos por columna:\n\n")
    unique_values(df, log_file, output_folder)


# ==============================
# BUCLE PRINCIPAL
# ==============================

with open(log_global_path, "w", encoding="utf-8") as log:

    log.write("======= ANALISIS GLOBAL DE TODAS LAS TABLAS =======\n\n")

    for archivo in os.listdir(ruta):
        if archivo.endswith(".csv"):
            path_completo = os.path.join(ruta, archivo)

            print(f"\n📂 Analizando archivo: {archivo}")

            df = pd.read_csv(path_completo)
            nombre_tabla = archivo.replace(".csv", "")

            analizar_tabla(df, nombre_tabla, log)

print("\n✔️ Análisis completado. Archivo generado:")
print(log_global_path)
