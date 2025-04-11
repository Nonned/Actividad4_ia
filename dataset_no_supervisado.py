
import pandas as pd

def cargar_dataset_rutas():
    data = {
        'origen': ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'E', 'F'],
        'destino': ['B', 'C', 'D', 'E', 'C', 'D', 'E', 'F', 'A', 'B'],
        'hora_salida': [7, 8, 9, 17, 8, 9, 10, 18, 7, 8],
        'distancia_km': [2.0, 3.5, 4.0, 6.0, 2.2, 3.7, 4.1, 6.1, 5.0, 3.0],
        'congestion': ['media', 'alta', 'baja', 'alta', 'baja', 'media', 'media', 'alta', 'baja', 'media'],
    }
    return pd.DataFrame(data)
