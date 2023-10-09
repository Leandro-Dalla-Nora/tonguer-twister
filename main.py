from src.utilities import *

tonguer_twister_db = read_file()

qtd_words = counter_words(tonguer_twister_db)

letters_most_popular = degree_letters_repetition(tonguer_twister_db, qtd_words)

difficulty_level = calculate_difficulty(qtd_words, letters_most_popular)

result_presentation(difficulty_level, tonguer_twister_db)


