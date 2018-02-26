#imports
import os
import re
import csv
#re.split("(?&lt;=[.!?]) +", paragraph)

#initial variables for 1
LCount1 = 0

#files
file1 ='resources/paragraph_1.txt' 

#initial solve1

with open(file1, 'r') as text1:
    paragraph1 = text1.read()
    #word count is broken by spaces, count spaces for words and add 1 for periods
    wc1 = paragraph1.count(" ") + 1
    #sentence count punctuated by end mark, find end mark at count for endings.
    #resounrces: https://dzone.com/articles/count-lines-sentences-and
    sc1 = paragraph1.count(".")+ paragraph1.count("!") + paragraph1.count("?")

#average count:
    for Char1 in paragraph1:
        if Char1.isalpha():
            LCount1 += 1
    ALCount1 = LCount1/wc1

ASentence1 = wc1/sc1

#print("Paragraph 1 Analysis:")
#print("-----------------")
#print("Approximate Word Count: " + str(wc1))
#print("Approximate Sentence Count: " + str(sc1))
#print("Average letter count: " + str(ALCount1))
#print("Average Sentence Count: " + str(ASentence1))

#initial variables for 2
LCount2 = 0

#file 2 
#mimic 1 for file 2
file2 ='resources/paragraph_2.txt' 

#initial solve1

with open(file2, 'r') as text2:
    paragraph2 = text2.read()
    wc2 = paragraph2.count(" ") + 1
    sc2 = paragraph2.count(".")+ paragraph2.count("!") + paragraph2.count("?")

#average count:
    for Char2 in paragraph2:
        if Char2.isalpha():
            LCount2 += 1
    ALCount2 = LCount2/wc2

ASentence2 = wc1/sc1

#print("Paragraph 2 Analysis:")
#print("-----------------")
#print("Approximate Word Count: " + str(wc2))
#print("Approximate Sentence Count: " + str(sc2))
#print("Average letter count: " + str(ALCount2))
#print("Average Sentence Count: " + str(ASentence2))

#total calculation:
print("Paragraph Analysis:")
print("-----------------")
TWord = (wc1)+int(wc2)
print("Total Word Count: " + str(TWord))
SCount = int(sc1) + int(sc2)
print("Total Sentence Count: " + str(SCount))
ALetter = (int(ALCount1)+int(ALCount2))/2
print("Average Letter Count: " + str(ALetter))
ASentence = (int(ASentence1)+int(ASentence2))/2
print("Average Sentence Count: " + str(ASentence))