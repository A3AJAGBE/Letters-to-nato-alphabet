import pandas as pd
# Convert the file to dict
data = pd.read_csv("nato_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}


print('Easily communicate a word over the phone.\n')

# User prompt
word = input("Enter a word: ").upper()

# Convert word to nato phonetics
response = [data_dict[letter] for letter in word]
print(response)

