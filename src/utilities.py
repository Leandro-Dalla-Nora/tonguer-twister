from typing import List, Tuple

import pandas as pd
from collections import Counter


def read_file() -> list[str]:
    return pd.read_csv('./dataset/database.csv')["Tongue twister"].tolist()


def counter_words(db: list[str]) -> list[int]:
    return [len(frase.split()) for frase in db]


def repetition_letters(db: list[str]) -> list[list[tuple[str, int]]]:
    return [Counter(frase.lower().replace(' ', '')).most_common(2) for frase in db]




