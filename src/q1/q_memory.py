from typing import List, Tuple
from datetime import datetime
import json


def q_memory(file_path: str) -> List[Tuple[datetime.date, str, int]]:
    """
    Evitamos crear excesivas estructuras de datos en memoria. En lugar de eso, leemos el archivo
    línea por línea y actualizamos los contadores a medida que leemos el archivo.
    """
    # Contadores de frecuencia de fechas y de usuarios por fecha
    date_freq = {}
    date_user_freq = {}

    # Leer el archivo línea por línea
    with open(file_path, 'r') as file:
        for line in file:
            entry = json.loads(line)
            date_str = entry['date']
            username = entry['user']['username']

            # Convertir la fecha a un objeto datetime.date
            date = datetime.fromisoformat(date_str).date()

            # Actualizar contadores de fechas
            if date not in date_freq:
                date_freq[date] = 0
                date_user_freq[date] = {}
            date_freq[date] += 1

            # Actualizar contadores de usuarios por fecha
            if username not in date_user_freq[date]:
                date_user_freq[date][username] = 0
            date_user_freq[date][username] += 1

    # Obtener las 10 fechas con más tweets
    top_10_dates = sorted(date_freq.items(), key=lambda x: x[1], reverse=True)[:10]

    result = []
    for date, _ in top_10_dates:
        # Obtener el usuario con más tweets en esa fecha y las frecuencias
        top_user = max(date_user_freq[date].items(), key=lambda x: x[1])[0]
        result.append((date, top_user, date_freq[date]))

    return result
