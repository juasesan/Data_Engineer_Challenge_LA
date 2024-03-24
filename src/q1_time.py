from typing import List, Tuple
from datetime import datetime
import pandas as pd
import json

from functions import first_mode


def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    with open(file_path, "r") as tweets_file:
        df = [(json.loads(line)['date'], json.loads(line)['user']['username']) for line in tweets_file]

    df = pd.DataFrame(df, columns=['date', 'username'])
    df['date'] = pd.to_datetime(df['date']).dt.date

    top_dates = df['date'].value_counts().head(10).index.tolist()

    df = df[df['date'].isin(top_dates)]

    df = df.groupby('date').agg({'username': first_mode}).reset_index()

    return list(zip(df['date'], df['username']))