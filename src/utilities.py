import pandas as pd
from collections import Counter


def read_file() -> list[str]:
    return pd.read_csv('./dataset/database.csv')["Tongue twister"].tolist()


def qtd_words_tonguer_twister(db) -> list[int]:
    return [len(frase.split()) for frase in db]


# def repetition_letters(db):
#     return [Counter(letters for letters in tonguer_twister for tonguer_twister in db)]


frases = ['Coy knows pseudonoise codes.', 'Sheena leads, Sheila needs.']

contadores = Counter(frase.lower() for frase in frases).most_common(2)
print(contadores)

for frase in frases:
    print(Counter(frase.lower()).most_common(2))


# print([letra for frase in frases for letra in frase])

