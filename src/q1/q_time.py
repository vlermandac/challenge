from typing import List, Tuple
from datetime import datetime
import json
from heapq import heappush, heappop


def q_time(file_path: str) -> List[Tuple[datetime.date, str, int]]:
    """
    Utilizamos heap. En promedio tiene inserciones más lentas que un diccionario
    (aunque peor caso es más rápido), pero obtenemos los elementos más
    frecuentes en tiempo O(log n) en lugar de O(n).
    """
    # Diccionarios para contar tweets por fecha y por usuario
    date_freq = {}
    date_user_freq = {}

    # Heaps para mantener las fechas y los usuarios más frecuentes
    date_user_heap = {}
    date_heap = []

    # Leer el archivo json línea por línea
    with open(file_path, 'r') as file:
        for line in file:
            entry = json.loads(line)
            date_str = entry['date']
            username = entry['user']['username']

            # Convertir la fecha a un objeto datetime.date
            date = datetime.fromisoformat(date_str).date()

            # Inicializar frecuencia y diccionarios si no existen
            if date not in date_freq:
                date_freq[date] = 0
                date_user_freq[date] = {}
                date_user_heap[date] = []

            # Actualizar frecuencia de fecha y agregar a heap
            date_freq[date] += 1
            heappush(date_heap, (-1 * date_freq[date], date))

            # Inicializar frecuencia de usuario si no existe
            if username not in date_user_freq[date]:
                date_user_freq[date][username] = 0

            # Actualizar frecuencia de usuario para fecha especifica y agregar a heap
            date_user_freq[date][username] += 1
            heappush(date_user_heap[date], (-1 * date_user_freq[date][username], username))

    # Lista de tuplas con las 10 fechas y usuarios más frecuentes a retornar
    result = []

    # Hacemos pop en el heap de fechas mientras no hayan 10 elementos en el resultado
    while (len(date_heap) > 0) and (len(result) < 10):

        # Sacamos la fecha con mayor frecuencia
        date_top = heappop(date_heap)
        date_top_freq = date_top[0] * -1
        date_top_name = date_top[1]

        # Verificamos si la fecha está repetida
        if date_top_freq < date_freq[date_top_name]:
            continue

        # Obtenemos el usuario con mayor frecuencia para la fecha
        user_top = heappop(date_user_heap[date_top_name])

        # Agregamos la fecha y usuario a la lista de resultados
        result.append((date_top_name, user_top[1], date_top_freq))

    return result
