#!/bin/python

from fuzzywuzzy import fuzz
from wordLists import verbs, adjectives, nouns

#fileList = ["Example1.tex", "Example2.tex","Example3.tex","Example4.tex"]
fileList = ["Example1_NF.tex", "Example2_NF.tex"]

counter_positive = 0
counter_total = 0

for infilename in fileList:
    infile=open(infilename,"r")
    for line in infile :
        for word in line.split(" ") :
            counter_total = counter_total+1
            for verb in verbs :
                score = fuzz.ratio(word,verb)
                if score > 85 :
                    #print score, word, verb
                    counter_positive = counter_positive + 1
            for noun in nouns :
                score = fuzz.ratio(word,noun)
                if score > 85 :
                    #print score, word, verb
                    counter_positive = counter_positive + 1
            for adjective in adjectives :
                score = fuzz.ratio(word,adjective)
                if score > 85 :
                    #print score, word, adjective
                    counter_positive = counter_positive + 1


    print infilename, float(counter_positive)/float(counter_total)
