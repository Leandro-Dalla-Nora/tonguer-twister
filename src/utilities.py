from typing import List, Tuple

import pandas as pd
from collections import Counter


def read_file():
    return pd.read_csv('./dataset/database.csv')["Tongue twister"].tolist()


def counter_words(db) -> list[int]:
    return [len(frase.split()) for frase in db]


def repetition_letters(db) -> list[list[tuple[str, int]]]:
    lista = []

    for frase in db:
        lista.append(Counter(frase.lower().replace(' ', '')).most_common(2))

    return lista




