from typing import List, Tuple
from datetime import datetime
import pandas as pd
import json

from functions import first_mode


def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Lectura del json y extracción de los campos de fecha y usuario
    with open(file_path, "r") as tweets_file:
        df = [(json.loads(line)['date'], json.loads(line)['user']['username']) for line in tweets_file]
    
    # Conversión a dataframe con el formato de fecha adecuado
    df = pd.DataFrame(df, columns=['date', 'username'])
    df['date'] = pd.to_datetime(df['date']).dt.date

    # Agrupamiento por conteo de fechas y usuario más común en cada una (representado por la medida estadística de "moda")
    df = df.groupby('date').agg({'username':[lambda x: x.count(), first_mode]}).reset_index()
    df.columns=['date', 'count', 'user']

    # Ordenamiento según el conteo y obtención del top 10
    df = df.sort_values(by='count', ascending=False).head(10)

    return list(zip(df['date'], df['user']))

