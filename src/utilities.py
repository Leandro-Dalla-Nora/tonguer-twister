import pandas as pd


def read_file():
    arquive = pd.read_csv('./dataset/database.csv')["Tongue twister"].tolist()
    return arquive


def qtd_words_tonguer_twister(db):
    return [len(frase.split()) for frase in db]


