"""
Code by @M-b850
Charcter-Finder is lokking for special words: charcter by charcter,
there is a sentence in input.txt
"""
import os

from core.function import Search

dir_path = os.path.dirname(os.path.realpath(__file__))
file = f"{dir_path}/input.txt"

word = input("Enter The Word That you're Looking for in input.txt: \n")

with open(file) as f:
    content = f.read()
    res = Search(word, content).Find_Char()

    if res is None:
        print("it's not here.")
    else:
        print("It's Here.")

    f.close()
