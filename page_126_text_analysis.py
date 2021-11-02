"""
Author: Nguyen Duc Thang
Date: 24/09/2021
Program: page_126_text_analysis.py
Problem: Text Analysis
Solution:
    Computes and displays the Flesch Index and the Grade
    Level Equivalent for the readability of a text file.
    Nhap file text.txt

"""
# Take the inputs: file text.txt
fileName = input("Enter the file name: ")
inputFile = open(fileName, 'r')
text = inputFile.read()
print(f'debug_tex',{text})
# Count the sentences
sentences = text.count('.') + text.count('?') + \
            text.count(':') + text.count(';') + \
            text.count('!')
print(f'debug_sentences',{sentences})
# Count the words
words = len(text.split())
print(f'debug_words',{words})
# Count the syllables
syllables = 0
vowels = "aeiou"
for word in text.split():
    for vowel in vowels:
        syllables += word.count(vowel)
    for ending in ['es', 'ed', 'e']:
        if word.endswith(ending):
            syllables -= 1
    if word.endswith('le'):
        syllables += 1
print(f'debug_syllables',{syllables})
# Compute the Flesch Index and Grade Level
index = 206.835-1.015 * (float(words) / float(sentences)) - \
84.6 * (float(syllables) / float(words))
level = round(0.39 * (words / float(sentences)) + 11.8 * (syllables / float(words))-15.59)
# Output the results
print("The Flesch Index is", index)
print("The Grade Level Equivalent is", level)
print(sentences, "sentences")
print(words, "words")
print(syllables, "syllables")