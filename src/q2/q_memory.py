from typing import Dict
import json
import emoji


def q_memory(file_path: str) -> Dict[str, int]:
    """
    Se utiliza un diccionario para almacenar los datos del archivo. Se lee
    el archivo linea por linea y se extraen los emojis de cada tweet con la ayuda de la libreria emoji
    """
    emoji_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            entry = json.loads(line)
            st = entry['content']
            emojis = emoji.emoji_list(st)
            for emoji_entry in emojis:
                token = emoji_entry['emoji']
                if token not in emoji_dict:
                    emoji_dict[token] = 0
                emoji_dict[token] += 1

    return emoji_dict
