from typing import List, Tuple
from collections import Counter
import json


def q3_time(file_path: str) -> List[Tuple[str, int]]:
    # Inicialización del contador de usuarios
    users_count = Counter()

    with open(file_path, "r") as tweets_file:
        for line in tweets_file:
            # Conteo de usuarios mencionados en caso de existir (mentionedUsers no es None), caso contrario, pasar por alto.
            try:
                users_count.update([user['username'] for user in json.loads(line)['mentionedUsers']])
            except:
                pass

    # Retorno de los 10 usuarios más mencionados.
    return users_count.most_common(10)