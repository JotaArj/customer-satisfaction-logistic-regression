# Predicción de Satisfacción del Cliente

Proyecto de machine learning enfocado en predecir la satisfacción del cliente utilizando modelos de clasificación y análisis exploratorio de datos.

[Introduccion al Proyecto](olist-project-files\docs\0_Introduccion.docx)

---

## Descripción del Proyecto

Este proyecto tiene como objetivo predecir si un cliente está satisfecho o no en función de diferentes variables relacionadas con el servicio.

El proyecto incluye limpieza de datos, análisis exploratorio (EDA), ingeniería de variables y entrenamiento de un modelo de clasificación basado en **Logistic Regression** así como otros modelos de machine learning con la finalidad de hallar el mejor para nuestro objetivo.

[Descripcion del Proyecto](olist-project-files\docs\0_Introduccion.docx)

---

## Objetivos

- Comprender los factores que influyen en la satisfacción del cliente
- Explorar y limpiar el conjunto de datos
- Evaluar el rendimiento del modelo

---

## Dataset

Fuente: [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
Variable objetivo: `satisfaction`  
Las variables incluyen datos demográficos del cliente, valoraciones del servicio y métricas de interacción.

![Estructura Datasets](olist-project-files\images\estructura_dataframes.png)

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

(olist-project-files\docs\3_Workflow.docx)

1. Limpieza de datos
    [Script ETL](olist-project-files\code\etl\final_data_olist.ipynb)
    [Descripcion de columnas del dataset](olist-project-files\docs\1_Tablas_descripciones.xlsx)

2. Análisis exploratorio de datos (EDA)
    [Script analisiis de columnas](olist-project-files\code\exploration\analisis_descriptor_columns.py)
    [Script analisis datasets](olist-project-files\code\exploration\analysis.py)
    [Script generador de dataset para dashboard](olist-project-files\code\etl\final_data_VISUALIZACION.ipynb)
    [Dashboard Olist](olist-project-files\docs\dashboard_OLIST.pbix)

3. Ingeniería de variables
    [Agrupacion de estados y categorias](olist-project-files\docs\2_Agrupación_ESTADOS_CATEGORÍAS.xlsx)
    [Transformacion de columnas segun modelo (pagina 2 en adelante)](olist-project-files\docs\4_Columnas_transformaciones_modelo.xlsx)
    [Script modelo Regresion logistica (incluye ajuste de dataset)](olist-project-files\code\ml-scripts\logistic-regression\Regresion_Logistica_Olist.ipynb)
    
4. Entrenamiento del modelo (Logistic Regression)
    [Script Regresion logistica](olist-project-files\code\ml-scripts\logistic-regression\Regresion_Logistica_Olist.ipynb)

5. Evaluación del modelo
    [Evaluacion modelos (pagina 1)](olist-project-files\docs\4_Columnas_trasnformaciones_modelo.xlsx)
    [Script modelo Regresion logistica](olist-project-files\code\ml-scripts\logistic-regression\Regresion_Logistica_Olist.ipynb)

---

## Análisis Exploratorio de Datos

- Distribución de la variable objetivo
- Análisis de correlaciones
- Exploración de la importancia de variables
- Detección de valores nulos y outliers

---

## Modelos utilizados

**Logistic Regression**
    [Script Logistic Regression](olist-project-files\code\ml-scripts\logistic-regression\Regresion_Logistica_Olist.ipynb)

**KNN**
    [Script 1 KNN](olist-project-files\code\ml-scripts\KNN\1_KNN_binario.ipynb)
    [Script 2 KNN](olist-project-files\code\ml-scripts\KNN\2_KNN_binario.ipynb)
    [Script 3 KNN](olist-project-files\code\ml-scripts\KNN\3_KNN_binario.ipynb)
    [Script 4 KNN](olist-project-files\code\ml-scripts\KNN\4_KNN_binario.ipynb)
    [Script KNN Binario](olist-project-files\code\ml-scripts\KNN\KNN_1var_Olist.ipynb)
    [Script KNN 3 variables](olist-project-files\code\ml-scripts\KNN\KNN_3var_Olist.ipynb)
    [Script KNN 5 variables](olist-project-files\code\ml-scripts\KNN\KNN_5var_Olist.ipynb)

**Gradient Boosting**
    [Script Gradient Boosting binario](olist-project-files/code/ml-scripts/gradient-boosting/Gradient_Boosting_2var_Olist.ipynb)
    [Script Gradient Boosting 3 variables](olist-project-files/code/ml-scripts/gradient-boosting/Gradient_Boosting_3var_Olist.ipynb)
    [Script XGBoost](olist-project-files\code\ml-scripts\gradient-boosting\XGBoost_Olist.ipynb)

**Decision Tree**
    (Gradient_Boosting_3var_Olist.ipynb)
    [Script Decision Tree](olist-project-files\code\ml-scripts\decision-tree\tree_model.ipynb)

---

## Evaluación del Modelo

Métricas utilizadas:

- Accuracy
- Sensibilidad
- Especificidad (Valor que fue determinante para decidir sobre el modelo)
- F1_score
- ROC-AUC

Como podemos observar, tenemos varios modelos con muy buenos resultados en algunos aspectos, pero el unico que realmente tenia unos valores aceptables en todas las metricas, en particular en especificidad fue en la regresion logistica

![Mapa de calor de evaluación de modelos](olist-project-files\images\heatmap_resultados_modelos.jpg)
![Tabla resultados de evaluación de modelos](olist-project-files\images\tabla_comparacion_modelos.jpeg)

---

## Resultados e Insights

Tanto el resultado como el proceso aparece relatado en [Presentacion Olist](olist-project-files\docs\Presentacion_OLIST.pdf)

Se realizaron dos [dashboards](olist-project-files\docs\dashboard_OLIST.pbix) para poder interpretar y exponer los datos

![Dashboard General](olist-project-files/images/dashboard_global_image.jpg)
![Dashboard Retraso](olist-project-files/images/dashboard_retraso_image.jpg)

Tras analizar detenidamente los resultados, podemos observar que la valoracion habitual es de 5, y las unicas relaciones solidas fueron que el pedido no llego retrasado o que no se entrego, que mostraba una relacion bastante elevada.

Pudimos descartar que estuviera relacionado, o bien con el tamaño del envio, el tipo de producto, numero de productos, precio o localizacion del vendedor.

![pesos variables](olist-project-files\images\pesos_variables.jpg)
![influencia retraso](olist-project-files\images\influencia_retraso.jpg)
![influencia categorias](olist-project-files\images\influencia_categorias.jpg)
![influencia categorias](olist-project-files\images\influencia_entrega.jpg)

Se podría obtener mejores resultados ampliando los datos, principalmente analizando los textos de las reviews en busca de los motivos de las valoraciones, ya sea bien por la adicion de keywords o bien por vectores semanticos para la correcta evaluacion de las razones de los usuarios.
---