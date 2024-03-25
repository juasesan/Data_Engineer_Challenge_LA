from typing import List, Tuple
from functions import extract_emojis
from collections import Counter
import json


def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    # Inicialización del contador de emojis
    emoji_counts = Counter()

    with open(file_path, "r") as tweets_file:
        for line in tweets_file:
            # Por cada tweet, se obtienen los emojis presentes en una lista y se actualiza el contador
            emojis = extract_emojis(json.loads(line)['content'])
            emoji_counts.update(emojis)
    
    # Retorno de los 10 emojis más comunes
    return emoji_counts.most_common(10)