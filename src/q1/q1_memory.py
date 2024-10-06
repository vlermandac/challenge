from typing import List, Tuple
from datetime import datetime
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def q1_memory(file_path: str) -> List[Tuple[int, datetime.date, str]]:
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
        top_user_freq = date_user_freq[date][top_user]
        # logger.info(f"""Date: {date}, Frequency: {date_freq[date]},
        #             Top User: {top_user}, Top User Frequency: {top_user_freq}""")
        result.append((date_freq[date], date, top_user))

    return result
