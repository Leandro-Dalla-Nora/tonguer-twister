import operator
import pandas as pd
from collections import Counter


def read_file() -> list[str]:
    return pd.read_csv('./dataset/database.csv')["Tongue twister"].tolist()


def counter_words(db: list[str]) -> list[int]:
    return [len(frase.split()) for frase in db]


def letters_most_common(db: list[str]) -> list[list[tuple[str, int]]]:
    return [Counter(frase.lower().replace(' ', '')).most_common(2) for frase in db]


def degree_letters_repetition(db: list[str], qtd_words: list[int]) -> list[float]:
    repetition_letters = letters_most_common(db)

    degree_fst_letter = list(map(operator.truediv, (letter[0][1] for letter in repetition_letters), qtd_words))
    degree_scd_letter = list(map(operator.truediv, (letter[1][1] for letter in repetition_letters), qtd_words))

    return list(map(operator.mul, degree_fst_letter, degree_scd_letter))


def calculate_difficulty(qtd_words: list[int], difficulty_tonguer_twister: list[float]) -> list[float]:
    return list(map(operator.mul, difficulty_tonguer_twister, qtd_words))


def find_hardest(diffiulty: list[float], db: list[str]) -> str:
    return db[diffiulty.index(max(diffiulty))]


def find_easily(diffiulty: list[float], db: list[str]) -> str:
    return db[diffiulty.index(min(diffiulty))]


def result_presentation(difficulty_level: list[float], tonguer_twister_db: list[str]) -> None:
    print('Difficulty level: tonguer-twister')
    print('\n'.join([f"{difficulty:.2f}: {tonguer_twister}" for difficulty, tonguer_twister in zip(difficulty_level, tonguer_twister_db)]))
    print(f'\nHardest: \n{find_hardest(difficulty_level, tonguer_twister_db)}')
    print(f'Easily: \n{find_easily(difficulty_level, tonguer_twister_db)}')

