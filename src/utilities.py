import pandas as pd


def read_file():
    arquive = pd.read_csv('./dataset/database.csv')["Tongue twister"]
    return arquive
