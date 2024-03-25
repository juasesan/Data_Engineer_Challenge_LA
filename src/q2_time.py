from typing import List, Tuple
from functions import extract_emojis
from collections import Counter
import json


def q2_time(file_path: str) -> List[Tuple[str, int]]:
    # Lectura de los tweets en el archivo json
    with open(file_path, "r") as tweets_file:
        tweets = [json.loads(line)['content'] for line in tweets_file]
    
    # Inicialización del contador
    emoji_counts = Counter()

    # Por cada tweet, se extraen los emojis en una lista y se actualiza el contador
    for tweet in tweets:
        emojis = extract_emojis(tweet)
        emoji_counts.update(emojis)
    
    # Retorno de los 10 emojis más comunes
    return emoji_counts.most_common(10)