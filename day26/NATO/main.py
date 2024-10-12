import pandas as pd

data=pd.read_csv("day26/NATO/nato_phonetic_alphabet.csv")
# print(data)

p_dict={row.letter:row.code for index,row in data.iterrows()}
# print(p_dict)


word=input("Enter a word: ").upper()
ol=[p_dict[letter] for letter in word]

print(ol)