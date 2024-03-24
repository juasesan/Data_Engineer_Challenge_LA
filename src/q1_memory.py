from typing import List, Tuple
from datetime import datetime
import pandas as pd
import json

from functions import first_mode


def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    with open(file_path, "r") as tweets_file:
        df = [(json.loads(line)['date'], json.loads(line)['user']['username']) for line in tweets_file]
    
    df = pd.DataFrame(df, columns=['date', 'username'])
    df['date'] = pd.to_datetime(df['date']).dt.date

    df = df.groupby('date').agg({'username':[lambda x: x.count(), first_mode]}).reset_index()
    df.columns=['date', 'count', 'user']

    df = df.sort_values(by='count', ascending=False).head(10)

    return list(zip(df['date'], df['user']))

