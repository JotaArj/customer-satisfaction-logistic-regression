# Predicción de Satisfacción del Cliente

Proyecto de machine learning enfocado en predecir la satisfacción del cliente utilizando modelos de clasificación y análisis exploratorio de datos.

---

## Descripción del Proyecto

Este proyecto tiene como objetivo predecir si un cliente está satisfecho o no en función de diferentes variables relacionadas con el servicio.

El proyecto incluye limpieza de datos, análisis exploratorio (EDA), ingeniería de variables y entrenamiento de un modelo de clasificación basado en **Logistic Regression** así como otros modelos de machine learning con la finalidad de hallar el mejor para nuestro objetivo.

---

## Objetivos

- Comprender los factores que influyen en la satisfacción del cliente
- Explorar y limpiar el conjunto de datos
- Evaluar el rendimiento del modelo

---

## Dataset

Fuente: ![Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
Variable objetivo: `satisfaction`  
Las variables incluyen datos demográficos del cliente, valoraciones del servicio y métricas de interacción.

![Estructura Datasets](https://i.imgur.com/HRhd2Y0.png)

---

## Tecnologías Utilizadas

Herramientas y librerías utilizadas en el proyecto.

- PowerBI
- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib / Seaborn
- Jupyter Notebook
- Excel
- Canvas
- Visual Studio Code
- Git


---

## Flujo del Proyecto

olist-project-files\docs\3_Workflow.docx

1. Limpieza de datos
    olist-project-files\code\etl\final_data_olist.ipynb
    olist-project-files\docs\1_Tablas_descripciones.xlsx

2. Análisis exploratorio de datos (EDA)
    olist-project-files\docs\1_Tablas_descripciones.xlsx
    olist-project-files\code\exploration\analisis_descriptor_columns.py
    olist-project-files\code\exploration\analysis.py
    olist-project-files\code\etl\final_data_VISUALIZACION.ipynb

3. Ingeniería de variables
    olist-project-files\docs\2. Agrupación_ESTADOS_CATEGORÍAS.xlsx
    olist-project-files\docs\4_Columnas_trasnformaciones_modelo.xlsx
    olist-project-files\code\ml-scripts\logistic-regression\Regresion_Logistica_Olist.ipynb
    
4. Entrenamiento del modelo (Logistic Regression)
    olist-project-files\code\ml-scripts\logistic-regression\Regresion_Logistica_Olist.ipynb

5. Evaluación del modelo
    olist-project-files\docs\4_Columnas_trasnformaciones_modelo.xlsx
    olist-project-files\code\ml-scripts\logistic-regression\Regresion_Logistica_Olist.ipynb

---

## Análisis Exploratorio de Datos

- Distribución de la variable objetivo
- Análisis de correlaciones
- Exploración de la importancia de variables
- Detección de valores nulos y outliers

---

## Modelo

Modelo utilizado: **Logistic Regression**
    olist-project-files\code\ml-scripts\logistic-regression\Regresion_Logistica_Olist.ipynb


Pasos realizados:

- División de datos en train/test
- Escalado de variables
- Entrenamiento del modelo
- Ajuste de modelo y comparación.
- Predicción

---

## Evaluación del Modelo

Explica cómo se evaluó el modelo.

Métricas utilizadas:

- Accuracy
- Sensibilidad
- Especificidad (Valor que fue determinante para decidir sobre el modelo)
- F1_score
- ROC-AUC

---

## Resultados e Insights

Explica qué conclusiones se obtuvieron del análisis.


---