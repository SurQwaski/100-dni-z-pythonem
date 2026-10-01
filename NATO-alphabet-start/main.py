import pandas as pd

nato_df = pd.read_csv("100-dni-z-pythonem/NATO-alphabet-start/nato_phonetic_alphabet.csv")
nato_phonetic_dictionary = {row.letter:row.code for (index,row) in nato_df.iterrows()}
user_input = input("Enter a word: ").upper()
result_list = [nato_phonetic_dictionary[letter] for letter in user_input]

print(result_list)

