#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re
import string

def main():

    
        #This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
    def is_sentence(text):
        # Check if the text is not empty and is a string
        if not isinstance(text, str) or not text.strip():
            return False
    
        # Check for starting with a capital letter
        if not text[0].isupper():
            return False
    
        # Check for ending punctuation
        if not re.search(r'[.!?]$', text):
            return False
    
        # Check if it contains at least one word (non-whitespace characters)
        if not re.search(r'\w+', text):
            return False
    
        return True
    
    def get_sentence():
        while True:
            text = input("Enter a sentence here: ")
            if is_sentence(text):
                return text
            else:
                print("Invalid sentence.")
        
    def calculate_frequencies(text):
        text = text.lower()
        words = text.split()
        for char in string.punctuation:
            sentence = sentence.replace(char, "")
        words = sentence.split()
        frequencies = {}
        for word in words:
            frequencies[word] = frequencies.get(word, 0) + 1
        return list(frequencies.keys()), list(frequencies.values())

    def print_frequencies(text1, text2):
        print("Words:", words)
        print("Frequencies:", frequencies)
                
        
        
        
    # Get a valid sentence from the user
    sentence = get_sentence()

    # Calculate word frequencies
    words, frequencies = calculate_frequencies(sentence)
    
    # Print the results
    print_frequencies(words, frequencies)

    





