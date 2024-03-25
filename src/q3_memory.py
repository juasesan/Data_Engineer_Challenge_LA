from typing import List, Tuple
from collections import Counter
import json


def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    # Definición un generador que retorne los usuarios listados en la sección de mentionedUsers.
    def generate_usernames(file):
        for line in file:
            users_mentioned = json.loads(line).get('mentionedUsers')
            if users_mentioned:
                for user in users_mentioned:
                    yield user['username']
    
    # Uso de la "lazy evaluation" al contar los usuarios utilizando un generador en vez de obtener todos y guardarlos en memoria a la vez.
    users_count = Counter(generate_usernames(open(file_path, "r")))
    
    # Retorno de los 10 usuarios más mencionados.
    return users_count.most_common(10)