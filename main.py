# from string import punctuation
# import numpy as np
# import os
# import pandas as pd
# from collections import Counter
from src.utilities import *

tonguer_twister_db = read_file()

qtd_words = counter_words(tonguer_twister_db)

letters_most_popular = repetition_letters(tonguer_twister_db)

print(letters_most_popular)


