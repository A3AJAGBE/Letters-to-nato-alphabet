import pandas as pd
# Convert the file to dict
data = pd.read_csv("nato_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}


print('Easily communicate a word over the phone.\n')


def word_convert():
    """This function convert the word to nato alphabet"""
    # User prompt
    word = input("Enter a word: ").upper()

    # prevent input that's not a letter
    try:
        # Convert word to nato phonetics
        response = [data_dict[letter] for letter in word]
        print(response)
    except KeyError:
        print("Invalid input, only letters in the alphabet.\n")
        word_convert()


word_convert()


