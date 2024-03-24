from typing import List, Tuple
from datetime import datetime
import pandas as pd
import json

from functions import first_mode


def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Lectura del json y extracción de los campos de fecha y usuario
    with open(file_path, "r") as tweets_file:
        df = [(json.loads(line)['date'], json.loads(line)['user']['username']) for line in tweets_file]

    # Conversión a dataframe con el formato de fecha adecuado
    df = pd.DataFrame(df, columns=['date', 'username'])
    df['date'] = pd.to_datetime(df['date']).dt.date

    # Obtención de las 10 fechas con más tweets y filtrado de estas en el dataframe
    top_dates = df['date'].value_counts().head(10).index.tolist()
    df = df[df['date'].isin(top_dates)]

    # Obtención del usuario más repetido en cada fecha
    df = df.groupby('date').agg({'username': first_mode}).reset_index()

    return list(zip(df['date'], df['username']))