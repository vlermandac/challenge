from typing import Dict
import json
import emoji
import pandas as pd


def q_time(file_path: str) -> Dict[str, int]:
    """
    Se utiliza un DataFrame de pandas para almacenar los datos del archivo. La idea es utilizar la
    facilidad de pandas, esperando que este modulo sea eficiente al aplicar operaciones sobre los datos.
    """
    content = []
    with open(file_path, 'r') as file:
        for line in file:
            entry = json.loads(line)
            st = entry['content']
            content.append(st)

    emoji_df = pd.DataFrame(content, columns=['content'])

    # Se extraen los emojis de cada tweet con la ayuda de la libreria emoji
    emoji_df['content'] = \
        emoji_df['content'].apply(lambda x: [em['emoji'] for em in emoji.emoji_list(x)])

    emoji_freq = emoji_df['content'].explode().value_counts().to_dict()

    return emoji_freq
