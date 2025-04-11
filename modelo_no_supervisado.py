

from dataset_no_supervisado import cargar_dataset_rutas
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 1. Cargar datos
df = cargar_dataset_rutas()

# 2. Preprocesamiento (variables categóricas + numéricas)
X = df[['origen', 'destino', 'hora_salida', 'distancia_km', 'congestion']]

preprocesador = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), ['origen', 'destino', 'congestion'])
    ],
    remainder='passthrough'
)

# 3. Modelo de clustering (agrupamiento)
pipeline = Pipeline(steps=[
    ('preprocesador', preprocesador),
    ('cluster', KMeans(n_clusters=3, random_state=42))
])

# 4. Entrenar modelo
pipeline.fit(X)

# 5. Asignar etiquetas de grupo (cluster) a cada ruta
df['grupo'] = pipeline.named_steps['cluster'].labels_

# 6. Mostrar resultados
print(df)

# 7. Visualización (opcional)
plt.scatter(df['hora_salida'], df['distancia_km'], c=df['grupo'], cmap='viridis')
plt.xlabel('Hora de salida')
plt.ylabel('Distancia (km)')
plt.title('Agrupación de rutas por características')
plt.colorbar(label='Grupo')
plt.show()
