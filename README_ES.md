# 🚀 Predicción de Satisfacción del Cliente (Olist E-commerce)

## 🧠 Resumen Ejecutivo

Proyecto de Machine Learning enfocado en predecir la satisfacción del cliente en un entorno real de e-commerce utilizando el dataset de Olist.

* 📊 Dataset: +100k pedidos reales
* 🎯 Objetivo: Clasificar clientes satisfechos vs no satisfechos
* 🤖 Modelos: Logistic Regression, KNN, Decision Tree, Gradient Boosting, XGBoost
* 🏆 Mejor modelo: Logistic Regression
* 🔑 Insight clave: El retraso en la entrega es el principal predictor de insatisfacción
* 📈 Valor de negocio: Identificación temprana de clientes en riesgo para mejorar la retención

---

## 📌 Descripción del Proyecto

Este proyecto analiza el comportamiento del cliente y el rendimiento del servicio para entender qué factores influyen en la satisfacción dentro de un entorno de e-commerce.

Cubre todo el ciclo analítico:

* Preparación de datos (ETL)
* Análisis exploratorio (EDA)
* Ingeniería de variables
* Entrenamiento y evaluación de modelos
* Generación de insights orientados a negocio

---

## 🎯 Objetivos

* Identificar los factores clave que afectan la satisfacción del cliente
* Construir y evaluar modelos de clasificación
* Comparar diferentes enfoques de Machine Learning
* Traducir resultados técnicos en decisiones de negocio

---

## 📊 Dataset

* Fuente: Olist Brazilian E-Commerce Dataset (Kaggle)
* Tamaño: ~100k pedidos
* Tipo: Datos transaccionales reales

**Variable objetivo:**

* `satisfaction` (binaria)

**Principales variables:**

* Valoraciones de clientes
* Tiempo de entrega
* Características del pedido
* Información del vendedor

---

## 🛠️ Tecnologías Utilizadas

* Python (Pandas, NumPy, Scikit-learn)
* Matplotlib / Seaborn
* Power BI
* Jupyter Notebooks
* Excel
* Git & GitHub

---

## 🧪 Estructura del Proyecto y Metodología

El proyecto sigue un enfoque **iterativo y experimental**, con múltiples notebooks que exploran diferentes modelos y configuraciones de variables.

### Convención de Naming

* `01_*` → Preparación de datos
* `02_*` → Análisis exploratorio (EDA)
* `03_*` → Modelado y experimentación

---

### 🔹 Preparación de Datos

* `01_data_preparation.ipynb`
* `01_data_for_dashboard.ipynb`

Incluye:

* Limpieza y unión de datos
* Tratamiento de valores nulos y outliers
* Generación del dataset final

---

### 🔹 Análisis Exploratorio (EDA)

* `02_eda_general_analysis.py`
* `02_eda_feature_distributions.py`

Incluye:

* Análisis de la variable objetivo
* Correlaciones
* Exploración de variables
* Validación de calidad de datos

---

### 🔹 Modelado

#### Regresión Logística

* `03_model_logistic_regression.ipynb`

#### KNN (múltiples experimentos)

* `03_model_knn_baseline.ipynb`
* `03_model_knn_experiment_1.ipynb`
* `03_model_knn_experiment_2.ipynb`
* `03_model_knn_experiment_3.ipynb`
* `03_model_knn_feature_1var.ipynb`
* `03_model_knn_feature_3var.ipynb`
* `03_model_knn_feature_5var.ipynb`

#### Modelos de Árbol

* `03_model_decision_tree.ipynb`

#### Modelos Boosting

* `03_model_gradient_boosting_2_features.ipynb`
* `03_model_gradient_boosting_3_features.ipynb`
* `03_model_xgboost.ipynb`

👉 La existencia de múltiples notebooks refleja un proceso de **experimentación controlada con distintas configuraciones y variables**

---

## 🤖 Evaluación de Modelos

Los modelos se evaluaron utilizando:

* Accuracy
* Recall (Sensibilidad)
* Specificity ⚠️ *(métrica clave en este proyecto)*
* F1-score
* ROC-AUC

### 🏆 Modelo Final: Logistic Regression

Seleccionado por:

* Mejor equilibrio global entre métricas
* Alta especificidad → reduce falsos positivos

👉 Esto es clave para evitar clasificar erróneamente clientes satisfechos como insatisfechos.

---

## 📈 Resultados

![Comparación de modelos](olist-project-files/images/model_comparison_heatmap.jpg)

* Algunos modelos maximizan accuracy pero fallan en otras métricas
* Logistic Regression presenta el comportamiento más estable

---

## 🔍 Insights Clave

* 🚚 **El retraso en la entrega es el principal driver de insatisfacción**
* ⭐ Las valoraciones están muy concentradas en valores altos (dataset desbalanceado)
* 📦 Variables como precio, categoría o tamaño del pedido tienen bajo impacto
* ❌ Entregas tardías o fallidas están fuertemente correlacionadas con malas valoraciones

---

## 📊 Visualización (Power BI)

Se desarrollaron dos dashboards:

* Visión general del negocio
* Análisis de retrasos en la entrega

![Dashboard general](olist-project-files/images/dashboard_overview.jpg)
![Dashboard retrasos](olist-project-files/images/dashboard_delay_analysis.jpg)

---

## ⚠️ Limitaciones

* Dataset desbalanceado (predominio de valoraciones positivas)
* No se han utilizado datos textuales (reviews)
* Limitación en la profundidad de variables
* Posibles mejoras mediante técnicas de NLP

---

## 🚀 Mejoras Futuras

* Incorporar análisis de texto (NLP)
* Uso de embeddings semánticos
* Optimización de hiperparámetros
* Técnicas de balanceo (SMOTE, etc.)
* Pipeline automatizado de entrenamiento

---

## ▶️ Cómo ejecutar el proyecto

```bash id="4w2zqz"
git clone <repository_url>
cd <repository>
pip install -r requirements.txt
```

Ejecutar notebooks en orden:

1. `01_*` → Preparación de datos
2. `02_*` → EDA
3. `03_*` → Modelado

---

## 📁 Recursos adicionales

* Documentación disponible en `/docs`
* Dashboard en `/reports`
* Dataset original en Kaggle

---

## 💡 Conclusión

Este proyecto demuestra la capacidad de:

* Trabajar con datos reales complejos
* Realizar análisis end-to-end
* Construir y evaluar modelos de Machine Learning
* Extraer insights con impacto en negocio

El principal valor reside en identificar los factores críticos que afectan la satisfacción del cliente, permitiendo tomar decisiones basadas en datos.

---
