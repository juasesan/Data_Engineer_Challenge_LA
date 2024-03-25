from typing import List, Tuple
from functions import extract_emojis
from collections import Counter
import json


def q2_time(file_path: str) -> List[Tuple[str, int]]:
    with open(file_path, "r") as tweets_file:
        tweets = [json.loads(line)['content'] for line in tweets_file]
    
    emoji_counts = Counter()

    for tweet in tweets:
        emojis = extract_emojis(tweet)
        emoji_counts.update(emojis)
    
    return emoji_counts.most_common(10)