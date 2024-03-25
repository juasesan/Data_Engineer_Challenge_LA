from typing import List, Tuple
from collections import Counter
import json


def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    def generate_usernames(file):
        for line in file:
            users_mentioned = json.loads(line).get('mentionedUsers')
            if users_mentioned:
                for user in users_mentioned:
                    yield user['username']
    
    users_count = Counter(generate_usernames(open(file_path, "r")))
    
    return users_count.most_common(10)