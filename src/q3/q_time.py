from typing import Dict
import json
import networkx as nx


def q_time(file_path: str) -> Dict[str, int]:
    """
    Se espera que el uso de un grafo entregue un rendimiento en tiempo similar
    o mejor que el uso de un diccionario.
    """
    G = nx.DiGraph()

    with open(file_path, 'r') as file:
        for line in file:
            entry = json.loads(line)
            user = entry['user']['username']
            mentions = entry['mentionedUsers']
            # Si no hay menciones, la entrada es null
            if mentions is None:
                continue
            for mention in mentions:
                mentioned_user = mention['username']
                if G.has_edge(user, mentioned_user):
                    G[user][mentioned_user]['weight'] += 1
                else:
                    G.add_edge(user, mentioned_user, weight=1)

    mention_count = G.in_degree(weight='weight')

    mention_count = dict(mention_count)
    return mention_count
