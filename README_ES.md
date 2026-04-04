# Predicción de Satisfacción del Cliente – Olist E-commerce

Proyecto de Machine Learning para predecir la satisfacción del cliente en e-commerce utilizando datos reales de Olist. Permite identificar clientes en riesgo de insatisfacción y generar insights accionables para mejorar la retención.  

---

## 🔹 Resumen Ejecutivo

- **Dataset:** ~100k pedidos reales de Olist  
- **Objetivo:** Clasificar clientes satisfechos vs no satisfechos  
- **Modelos evaluados:** Logistic Regression, KNN, Decision Tree, Gradient Boosting, XGBoost  
- **Mejor modelo:** Logistic Regression  
- **Insight clave:** El retraso en la entrega es el principal predictor de insatisfacción  
- **Valor de negocio:** Identificación temprana de clientes insatisfechos para mejorar la retención  

---

## 🔹 Objetivos del Proyecto

1. Identificar factores que afectan la satisfacción del cliente  
2. Construir y evaluar modelos de clasificación  
3. Comparar diferentes enfoques de Machine Learning  
4. Traducir resultados técnicos en decisiones de negocio  

---

## 🔹 Dataset

- **Fuente:** [Olist Brazilian E-Commerce Dataset (Kaggle)](https://www.kaggle.com/olistbr/brazilian-ecommerce)  
- **Tipo de datos:** Transaccionales reales  
- **Variable objetivo:** `satisfaction` (binaria)  
- **Principales variables:** valoraciones de clientes, tiempo de entrega, características del pedido, información del vendedor  

![Estructura del dataset](04_IMAGES/data_model_structure.png)  

---

## 🔹 Tecnologías Utilizadas

- **Lenguaje y librerías:** Python (Pandas, NumPy, Scikit-learn), Matplotlib, Seaborn  
- **Herramientas de visualización:** Power BI, Excel  
- **Documentación y control de versiones:** Jupyter Notebooks, Git & GitHub  

---

## 🔹 Estructura del Proyecto

- 01_ETL/ # Preparación y limpieza de datos
- 02_EDA/ # Análisis exploratorio (EDA)
- 03_ML_MODELS/ # Modelos de ML
- 04_IMAGES/ # Gráficos e imágenes para README y dashboard
- 05_DOCS/ # Documentación y reportes finales

---


---

## 🔹 Notebooks Clave

[01_data_preparation.ipynb](01_ETL/01_data_preparation.ipynb)
[01_data_for_dashboard.ipynb](01_ETL/01_data_for_dashboard.ipynb)
[02_eda_general_analysis.ipynb](02_EDA/02_eda_general_analysis.ipynb)
[02_eda_feature_distributions.ipynb](02_EDA/02_eda_feature_distributions.ipynb)[03_model_logistic_regression.ipynb](03_ML_MODELS/03_model_logistic_regression.ipynb)
[03_model_knn_baseline.ipynb](03_ML_MODELS/03_model_knn_baseline.ipynb)
[03_model_decision_tree.ipynb](03_ML_MODELS/03_model_decision_tree.ipynb)
[03_model_xgboost.ipynb](03_ML_MODELS/03_model_xgboost.ipynb)
 

---

## 🔹 Preparación de Datos (ETL)

- Limpieza y unión de datasets transaccionales  
- Tratamiento de valores nulos y outliers  
- Generación de dataset final listo para análisis y modelado  

![ETL Overview](04_IMAGES/etl_overview.png)  

---

## 🔹 Análisis Exploratorio (EDA)

- Distribución de la variable objetivo  
- Correlaciones y relaciones entre variables  
- Validación de calidad de datos  

![EDA General](04_IMAGES/eda_overview.png)  
![Distribución de Features](04_IMAGES/eda_feature_distributions.png)  

---

## 🔹 Modelado y Evaluación

### Métricas utilizadas

- Accuracy  
- Recall (Sensibilidad)  
- Specificity (clave para evitar falsos positivos)  
- F1-score  
- ROC-AUC  

### Modelo Final: Logistic Regression

- Mejor equilibrio entre métricas  
- Alta **specificity** → reduce falsos positivos (clientes satisfechos clasificados como insatisfechos)  

![Comparación de Modelos](04_IMAGES/model_comparison_heatmap.jpg)  
![Resultados de Modelos](04_IMAGES/model_results_table.jpg)  

---

## 🔹 Insights Clave

- Retrasos en la entrega → principal driver de insatisfacción  
- Valoraciones muy concentradas en valores altos (dataset desbalanceado)  
- Variables como precio, categoría o tamaño tienen bajo impacto  
- Entregas fallidas correlacionadas con malas valoraciones  

![Importancia de variables](04_IMAGES/feature_importance.jpg)  
![Impacto de retraso en entrega](04_IMAGES/delivery_delay_impact.jpg)  
![Impacto por categoría](04_IMAGES/category_impact.jpg)  
![Impacto del tiempo de entrega](04_IMAGES/delivery_time_impact.jpg)  

---

## 🔹 Visualización en Power BI

- **Dashboard general:** visión global del negocio  
- **Dashboard de retrasos:** análisis detallado de entregas tardías  

![Dashboard General](04_IMAGES/dashboard_overview.jpg)  
![Dashboard Retrasos](04_IMAGES/dashboard_delay_analysis.jpg)  

---

## 🔹 Limitaciones

- Dataset desbalanceado (predominio de valoraciones positivas)  
- No se ha utilizado información textual (reviews)  
- Limitación en la profundidad de variables  
- Posibles mejoras con NLP  

---

## 🔹 Mejoras Futuras

- Incorporar análisis de texto (NLP) y embeddings semánticos  
- Optimización de hiperparámetros  
- Técnicas de balanceo (SMOTE, etc.)  
- Pipeline automatizado de entrenamiento  

---

## 🔹 Cómo ejecutar el proyecto

TODO
REVISAR TODA LA EJECUCION PASO A PASO Y MODIFICAR

download dataset from [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce/data)

```bash
git clone https://github.com/JotaArj/customer-satisfaction-logistic-regression.git
cd customer-satisfaction-logistic-regression
pip install -r requirements.txt
jupyter notebook

```