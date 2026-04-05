import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ruta = BASE_DIR / "db" / "output"
archivo = BASE_DIR / "db" / "output" / "final_data.csv"
output_folder = "db/analysis"

columnas_excluir_contiene = ["_id",
           "date", 
           "timestamp"]    
columnas_excluir_exactas = ["review_comment_message", 
           "review_comment_title", 
           "review_answer_timestamp", 
           "order_approved_at",
           "geolocation_lat", 
           "geolocation_lng"]

def unique_values(data, log_file):
    for col in data.columns:
        dtype = data[col].dtype
        values = data[col].unique()
        length_values = len(values)

        if length_values < 30:
            line = f"{col} ({dtype}), {length_values} valores únicos: {values}\n"
        else:
            line = f"{col} ({dtype}) tiene {length_values} valores únicos (más de 30).\n"
        log_file.write(line)

        if check_column(col):
            line = line + f"{col} no se le realizara grafico\n"
        else:
            generate_plots(data, col, output_folder)
        print(line)


def value_analysis(data, name, log_file):
    log_file.write(f"\n===== {name.upper()} =====\n")
    log_file.write(f"Shape: {data.shape}\n")

    # % de NaNs
    log_file.write("\n% de NaNs por columna:\n")
    nan_percent = (data.isna().sum() / len(data)) * 100
    log_file.write(str(nan_percent) + "\n\n")

    # valores únicos
    unique_values(data, log_file)

def check_column(col):
    col_lower = col.lower()

    if (
        any(p in col_lower for p in columnas_excluir_contiene) or
        any(col_lower == p for p in columnas_excluir_exactas)
    ):
        print(f"⏭️ Saltando columna (excluida): {col}")
        return 1
    return 0

def generate_plots(df, col, output_folder):        
        if check_column(col):
            print(f"⏭️ Saltando columna : {col}")
        else:
            print(f"📊 Graficando columna: {col}")

            plt.figure(figsize=(10, 5))
            plt.rcParams["font.family"] = "DejaVu Sans"
            sns.countplot(data=df, x=col)
            plt.title(f"Countplot - {col}")
            plt.xticks(rotation=90)  # <- AHORA VERTICAL
            plt.tight_layout()
            img_path = os.path.join(output_folder, f"count_{col}.jpg")
            plt.savefig(img_path)
            plt.close()

            plt.figure(figsize=(10, 5))
            plt.rcParams["font.family"] = "DejaVu Sans"
            sns.countplot(data=df, x=col)
            plt.title(f"Histplot - {col}")
            plt.xticks(rotation=90)  # <- AHORA VERTICAL
            plt.tight_layout()
            img_path = os.path.join(output_folder, f"hist_{col}.jpg")
            plt.savefig(img_path)
            plt.close()


def full_db():
    # BUCLE PRINCIPAL
    for archivo in os.listdir(ruta):
        if archivo.endswith(".csv"):
            path_completo = os.path.join(ruta, archivo)

            print("\n==============================")
            print(f"Abrir: {archivo}")
            print(path_completo)
            print("==============================\n")

            df = pd.read_csv(path_completo)

            # Carpeta análisis
            nombre_tabla = archivo.replace(".csv", "")
            carpeta_analisis = os.path.join("db/analysis", nombre_tabla)
            os.makedirs(carpeta_analisis, exist_ok=True)

            # Ruta texto
            txt_path = os.path.join(carpeta_analisis, f"{nombre_tabla}.txt")
            with open(txt_path, "w", encoding="utf-8") as log:

                log.write(f"===== ANALISIS DE {archivo} =====\n")
                log.write(f"Shape: {df.shape}\n\n")

                # NaNs en %
                log.write("Porcentaje de NaNs por columna:\n")
                log.write(str((df.isna().sum() / len(df)) * 100) + "\n\n")

                # Buscar duplicados
                duplicados = df.duplicated().sum()
                log.write(f"Duplicados encontrados: {duplicados}\n")
                if duplicados > 0:
                    log.write("Ejemplo de duplicado:\n")
                    log.write(str(df[df.duplicated()].head(1)) + "\n\n")
                else:
                    log.write("No se encontraron duplicados.\n\n")

                # valores únicos + tipos
                log.write("Valores únicos por columna:\n\n")
            unique_values(df, log)


def unique_file():
    df = pd.read_csv(archivo)
    # Carpeta análisis
    nombre_tabla = "final_data"
    carpeta_analisis = os.path.join("db/analysis", nombre_tabla)
    os.makedirs(carpeta_analisis, exist_ok=True)
    # Ruta texto
    txt_path = os.path.join(carpeta_analisis, f"{nombre_tabla}.txt")
    with open(txt_path, "w", encoding="utf-8") as log:
        log.write("===== ANALISIS DE Final data =====\n")
        log.write(f"Shape: {df.shape}\n\n")
        # NaNs en %
        log.write("Porcentaje de NaNs por columna:\n")
        log.write(str((df.isna().sum() / len(df)) * 100) + "\n\n")
        # Buscar duplicados
        duplicados = df.duplicated().sum()
        log.write(f"Duplicados encontrados: {duplicados}\n")
        if duplicados > 0:
            log.write("Ejemplo de duplicado:\n")
            log.write(str(df[df.duplicated()].head(1)) + "\n\n")
        else:
            log.write("No se encontraron duplicados.\n\n")
        # valores únicos + tiposS
        log.write("Valores únicos por columna:\n\n")
        unique_values(df, log)

unique_file()