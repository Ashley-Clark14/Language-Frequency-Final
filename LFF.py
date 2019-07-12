#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 11:11:12 2019

@author: ashleygregory
"""

# Language-Frequency-Final
language frequency repo
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

os.chdir("/Users/ashleygregory/Desktop/IMT 511/Problem Set 4")

def LanguageFrequency(fileName):
    with open (fileName) as file_object:
        contents = file_object.read()
    s = contents.split()
    List = []
    for word in s:
        x = word.lower().strip('&%$#@!^_+=`:;"><?/\.¡*¿')
        List.append(x)

    
    counts = {}
    for word in List:
        if not word in counts:
            counts[word] =0
        counts[word] += 1

    sorted_counts = sorted (counts.items(), key = lambda kv: kv[1], reverse = True) 
    
    
    most_frequent = dict(sorted_counts[:11])
    
    
    for word in most_frequent.keys():
        most_frequent[word] = most_frequent[word]/len(sorted_counts)

    return most_frequent

print("These are the most frequent words",LanguageFrequency("eaton-boy-scouts_EN.txt"))
print("These are the most frequent words",LanguageFrequency("cherbonnel-mi-tio_SP.txt"))
print("These are the most frequent words",LanguageFrequency("schloemp-tolle-koffer_DE.txt"))
print("These are the most frequent words",LanguageFrequency("unknown-lang.txt"))

Spanish = (LanguageFrequency('cherbonnel-mi-tio_SP.txt'))
English = (LanguageFrequency('eaton-boy-scouts_EN.txt'))
German = (LanguageFrequency("schloemp-tolle-koffer_DE.txt"))
Unknown = (LanguageFrequency("unknown-lang.txt"))

for w in Spanish.keys():

    Spanish.get(w, 'none')
    print(w, abs (Spanish[w] - Unknown[w]))

def Compare (language):
    for w in language.values():
        print(w)

