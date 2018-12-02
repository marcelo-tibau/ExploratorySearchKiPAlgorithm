# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 12:09:20 2018

@author: Marcelo
"""

# Setups
Qi = "start query"
Qm = "following query"
Qn = "future state after following query"

str1 = Qi
str2 = Qm
str3 = Qn

# Fixed number
i = 1
# changeable number 
x = 2
y = 3
# Fixed sets
m = x
n = y


# Function to split the Query by words and count them
def wordCounts(str):
    counts = dict()
    words = str.split()
    
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return (counts)
    

    
# Functions to compare a pair of Queries and count the duplicate words from them    
def wordDuplicates():
    count = 0    
    str1_split = str1.split(" ")
    for word in str2.split(" "):
        if word in str1_split:
            count += 1
    return (count)
    
def wordDuplicatesTwo():
    count = 0    
    str2_split = str2.split(" ")
    for word in str3.split(" "):
        if word in str2_split:
            count += 1
    return (count)
    

# Function to Classify pair of Queries based on ESKiP Taxonomy of Query States
def QueryStateClassifier(str):
    while str in Qi:
        if wordCounts(Qi) == wordCounts(Qi) and wordDuplicates() == 0:
            print ("IS")
        elif wordCounts(Qi) == wordCounts(Qi) and wordDuplicates() > 0:
            print ("IS")
        break
    while str in Qm:
        if len(Qm.split()) < len(Qi.split()) and wordDuplicates() > 0:
            print ("GE")
        elif len(Qm.split()) > len(Qi.split()) and wordDuplicates() > 0:
            print ("SC")
        elif wordCounts (Qm) == wordCounts (Qi):
            print ("RP")
        elif wordCounts (Qm) != wordCounts (Qi) and wordDuplicates() > 0:
            print ("WS")
        elif wordCounts (Qm) != wordCounts (Qi) and wordDuplicates() > 0 and len(Qm.split()) < len(Qi.split()):
            print ("WS")
        elif wordCounts (Qm) != wordCounts (Qi) and wordDuplicates() > 0 and len(Qm.split()) > len(Qi.split()):
            print ("WS")
        elif wordCounts (Qm) != wordCounts (Qi) and wordDuplicates() == 0:
            print ("NW")
        elif wordCounts (Qm) != wordCounts (Qi) and wordDuplicates() == 0 and len(Qm.split()) < len(Qi.split()):
            print ("NW")
        elif wordCounts (Qm) != wordCounts (Qi) and wordDuplicates() == 0 and len(Qm.split()) > len(Qi.split()):
            print ("NW")
        else:
            print ("RE")
        break
    while str in Qn:
        if wordCounts(Qn) == wordCounts(Qi) and wordDuplicatesTwo() > 0:
            print ("RS")
        elif len(Qn.split()) < len(Qm.split()) and wordDuplicatesTwo() > 0:
            print ("GE")
        elif len(Qn.split()) > len(Qm.split()) and wordDuplicatesTwo() > 0:
            print ("SC")
        elif wordCounts (Qn) == wordCounts (Qm):
            print ("RP")
        elif wordCounts (Qn) != wordCounts (Qm) and wordDuplicatesTwo() > 0:
            print ("WS")
        elif wordCounts (Qn) != wordCounts (Qm) and wordDuplicatesTwo() > 0 and len(Qn.split()) < len(Qm.split()):
            print ("WS")
        elif wordCounts (Qn) != wordCounts (Qm) and wordDuplicatesTwo() > 0 and len(Qn.split()) > len(Qm.split()):
            print ("WS")
        elif wordCounts (Qn) != wordCounts (Qm) and wordDuplicatesTwo() == 0:
            print ("NW")
        elif wordCounts (Qn) != wordCounts (Qm) and wordDuplicatesTwo() == 0 and len(Qn.split()) < len(Qm.split()):
            print ("NW")
        elif wordCounts (Qn) != wordCounts (Qm) and wordDuplicatesTwo() == 0 and len(Qn.split()) > len(Qm.split()):
            print ("NW")
        else:
            print ("RE") 
        break

