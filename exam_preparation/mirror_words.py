# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 21:32:05 2022

https://judge.softuni.org/Contests/Practice/Index/2307#1

@author: h.d.
"""
import re

text_string = input()
pattern = r"(\@|\#)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"

matched = re.findall(pattern, text_string)
count = len(matched)
mirrored = []
if matched:
    print(f"{count} word pairs found!")

    for pairs in matched:
        match_1 = pairs[1]
        match_2 = pairs[2]
        if match_1 == match_2[::-1]:
            mirrored.append(f"{match_1} <=> {match_2}")
            
else:
    print("No word pairs found!")            
    
if mirrored:
    print("The mirror words are:")
    print(', '.join(mirrored))
else:
    print("No mirror words!")
    