"""
Author: Nguyen Duc Thang
Date: 10/10/2021
Program: page_150_Generating_Sentences.py
Problem: Generating Sentences
Solution:
    Generates and displays sentences using simple grammar and vocabulary. Words are chosen at random.

"""
import random
# Vocabulary: words in 4 different parts of speech
articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL")
verbs = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")
def sentence():
    """Builds and returns a sentence."""
    return nounphrase() + " " + verbphrase()
def nounphrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)
def verbphrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounphrase() + " " + \
    prepositionalphrase()
def prepositionalphrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounphrase()
def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())
# The entry point for program execution
if __name__ == "__main__":
    main()
