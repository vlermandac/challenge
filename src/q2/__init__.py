from .q_time import q_time
from .q_memory import q_memory
from typing import List, Tuple, Dict, Callable
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import Counter


def run_function(func: Callable[[str], Dict[str, int]], file_paths: str) -> List[Tuple[str, int]]:
    """
    Ejecuta la función func en paralelo para cada archivo en file_paths y combina los resultados.
    """
    combined_results = Counter()
    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(func, file_path): file_path for file_path in file_paths}
        for future in as_completed(futures):
            result = future.result()
            combined_results += Counter(result)
    return list(combined_results.items())


def q2_time(file_paths: List[str]) -> List[Tuple[str, int]]:
    """
    Solución q2: versión optimizada para tiempo de ejecución.
    """
    freq = run_function(q_time, file_paths)
    freq.sort(key=lambda x: x[1], reverse=True)
    return freq[:10]


def q2_memory(file_paths: List[str]) -> List[Tuple[str, int]]:
    """
    Solución q2: versión optimizada para uso de memoria.
    """
    freq = run_function(q_memory, file_paths)
    freq.sort(key=lambda x: x[1], reverse=True)
    return freq[:10]
