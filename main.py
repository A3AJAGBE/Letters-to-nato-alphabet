
import pandas as pd
data = pd.read_csv("nato_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(data_dict)


