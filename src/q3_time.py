from typing import List, Tuple
from collections import Counter
import json


def q3_time(file_path: str) -> List[Tuple[str, int]]:
    users_count = Counter()

    with open(file_path, "r") as tweets_file:
        for line in tweets_file:
            try:
                users_count.update([user['username'] for user in json.loads(line)['mentionedUsers']])
            except:
                pass

    return users_count.most_common(10)