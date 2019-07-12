#!/usr/bin/env python3
# -*- coding: utf-8 -*-
**Language Frequency Predictor**

import os
import math

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
        most_frequent[word] = most_frequent[word]/len(List)

    return most_frequent

#print("These are the most frequent words",LanguageFrequency("eaton-boy-scouts_EN.txt"))
#print("These are the most frequent words",LanguageFrequency("cherbonnel-mi-tio_SP.txt"))
#print("These are the most frequent words",LanguageFrequency("schloemp-tolle-koffer_DE.txt"))
#print("These are the most frequent words",LanguageFrequency("unknown-lang.txt"))

Spanish = (LanguageFrequency('cherbonnel-mi-tio_SP.txt'))
English = (LanguageFrequency('eaton-boy-scouts_EN.txt'))
German = (LanguageFrequency("schloemp-tolle-koffer_DE.txt"))
Unknown = (LanguageFrequency("unknown-lang.txt"))


Sb = 0  # total difference for SP
Gb = 0
Eb = 0      
for u in Unknown.keys():
    U = Unknown.get(u, 0)
    S = Spanish.get(u, 0)
    Sdiff = abs(S-U)
    Sb = Sb + Sdiff
    
    G = German.get(u, 0)
    Gdiff = abs(G-U)
    Gb = Gdiff + Gb

    E = English.get(u, 0)
    Ediff = abs (E-U)
    Eb = Ediff + Eb
    
print("The difference in languages is", Sb, "in Spanish.")
print("The difference in language is", Gb, "in German.")
print("The difference in language is,", Eb, "in English")

if Sb < Eb and Sb < Gb:
        print("The document is in Spanish")
elif Eb < Sb and Eb < Gb:
        print("The document is in English")
elif Gb < Sb and Gb < Eb:
        print("The document is in German")
    