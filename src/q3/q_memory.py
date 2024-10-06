from typing import Dict
import json


def q_memory(file_path: str) -> Dict[str, int]:
    """
    Se mide la frecuencia de menciones de usuarios en un diccionario.
    """
    mention_count = {}

    with open(file_path, 'r') as file:
        for line in file:
            entry = json.loads(line)
            mentions = entry['mentionedUsers']
            # Si no hay menciones, la entrada es null
            if mentions is None:
                continue

            for mention in mentions:
                mentioned_user = mention['username']
                if mentioned_user in mention_count:
                    mention_count[mentioned_user] += 1
                else:
                    mention_count[mentioned_user] = 1

    return mention_count
