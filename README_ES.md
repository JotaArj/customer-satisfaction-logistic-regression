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

## 🔹 Problema de Negocio

En entornos de e-commerce, la satisfacción del cliente impacta directamente en:

- Retención
- Reputación de marca
- Costes operativos (devoluciones, soporte)

Este proyecto busca anticipar clientes insatisfechos antes de que dejen una mala valoración, permitiendo acciones proactivas como:

- Seguimiento de pedidos críticos
- Priorización logística
- Intervención del equipo de atención al cliente

---

## 🔹 Contribución

Este proyecto fue desarrollado en colaboración.  

**Mi contribución principal incluye:**

- Desarrollo del pipeline de preparación de datos (ETL)
- Análisis exploratorio (EDA) y validación de calidad de datos
- Implementación y evaluación de modelos de Machine Learning (GradientBoosting, XGBoost, KNN multiples variables)
- Selección y ajuste del modelo final (Logistic Regression)
- Generación de insights orientados a negocio (consensuada por todos los participantes)

### Autores

- Jacinto Arjona
- Giada Ceresa
- Carla López
- Natalia Martinez

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

## 🔹 Notebooks Clave

- [01_data_preparation.ipynb](01_ETL/01_data_preparation.ipynb)
- [01_data_for_dashboard.ipynb](01_ETL/01_data_for_dashboard.ipynb)
- [02_eda_general_analysis.ipynb](02_EDA/02_eda_general_analysis.ipynb)
- [02_eda_feature_distributions.ipynb](02_EDA/02_eda_feature_distributions.ipynb)
- [03_model_logistic_regression.ipynb](03_ML_MODELS/03_model_logistic_regression.ipynb)
- [03_model_knn_baseline.ipynb](03_ML_MODELS/03_model_knn_baseline.ipynb)
- [03_model_decision_tree.ipynb](03_ML_MODELS/03_model_decision_tree.ipynb)
- [03_model_xgboost.ipynb](03_ML_MODELS/03_model_xgboost.ipynb)

---

## 🔹 Preparación de Datos (ETL)

- Limpieza y unión de datasets transaccionales  
- Tratamiento de valores nulos y outliers  
- Generación de dataset final listo para análisis y modelado  

![ETL Overview](04_IMAGES/dashboard_overview.png)  

---

## 🔹 Análisis Exploratorio (EDA)

- Distribución de la variable objetivo  
- Correlaciones y relaciones entre variables  
- Validación de calidad de datos  

![Distribución de Features](04_IMAGES/feature_importance.png)  

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
![Resultados de Modelos](04_IMAGES/model_results_table.jpeg)  

---

### Resultados del modelo final

- Accuracy: 0.587
- Recall: 0.594
- Specificity: 0.577
- ROC-AUC: 0.6274

El modelo prioriza la reducción de falsos positivos, alineado con el objetivo de negocio.

---

## 🔹 Insights Clave

- Retrasos en la entrega → principal driver de insatisfacción  
- Valoraciones muy concentradas en valores altos (dataset desbalanceado)  
- Variables como precio o categoría muestran menor impacto relativo en comparación con variables logísticas, especialmente el tiempo de entrega.
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

## 🔹 Cómo instalar el proyecto

Primero clonaremos el repositorio para posteriormente instalar las dependencias necesarias a traves de pip

```bash
git clone https://github.com/JotaArj/customer-satisfaction-logistic-regression.git
cd customer-satisfaction-logistic-regression
pip install -r requirements.txt
```

- Descargar el dataset de [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce/data)
- Descomprimir en la raiz del proyecto, creando la carpeta /db/raw/

## 🔹 Ejecución del proyecto

1. Ejecutar el pipeline de datos:

- `01_ETL/01_data_preparation.ipynb`
- `01_ETL/01_data_for_dashboard.ipynb`

2. Análisis exploratorio (opcional):

- `02_EDA/02_eda_general_analysis.py`
- `02_EDA/02_eda_feature_distributions.py`

3. Modelado:

- `03_ML_MODELS/03_model_logistic_regression.ipynb`
