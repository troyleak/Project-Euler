#!/usr/bin/env python3

"""
Names scores
Problem 22
Using names.txt, a text file containing over five-thousand first names,
begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name, multiply this value by
its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

import csv
import string

def score_name(name):
    score = 0
    for i in name:
        score += char_position(i)
    return score

def char_position(letter): # returns the alphabetical index of a letter
    return int(string.ascii_uppercase.index(letter) + 1)

def calculate():
    for i in names:
        yield (score_name(i) * int(names.index(i) + 1))


with open('p022_names.txt', 'r') as f:
  reader = csv.reader(f)
  names = list(reader)[0]

names.sort()
# print(char_position("C"))
# print(score_name("COLIN"))
# print(int(names.index("COLIN") + 1))
print(sum(calculate()))
