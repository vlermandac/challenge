from .q_time import q_time
from .q_memory import q_memory
from typing import List, Tuple, Callable
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime


def run_function(func: Callable[[str], List[Tuple[datetime.date, str, int]]], file_paths: str) -> List[Tuple[datetime.date, str]]:
    """
    Ejecuta la función func en paralelo para cada archivo en file_paths y combina los resultados.
    """
    combined_results = {}
    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(func, file_path): file_path for file_path in file_paths}
        for future in as_completed(futures):
            result = future.result()
            for date_obj, username, value in result:
                # Si la fecha ya existe, se suma el valor
                if date_obj in combined_results:
                    combined_results[date_obj]['value'] += value
                # Si no, se agrega
                else:
                    combined_results[date_obj] = {'value': value, 'username': username}

    # Se ordena en base a la frecuencia
    srt = sorted(combined_results.items(), key=lambda item: item[1]['value'], reverse=True)

    # Se genera el output en el formato solicitado
    output = [(date_obj, data['username']) for date_obj, data in srt]

    return output


def q1_time(file_paths: List[str]) -> List[Tuple[str, int]]:
    """
    Solución q1: versión optimizada para tiempo de ejecución.
    """
    freq = run_function(q_time, file_paths)
    return freq[:10]


def q1_memory(file_paths: List[str]) -> List[Tuple[str, int]]:
    """
    Solución q1: versión optimizada para uso de memoria.
    """
    freq = run_function(q_memory, file_paths)
    return freq[:10]
