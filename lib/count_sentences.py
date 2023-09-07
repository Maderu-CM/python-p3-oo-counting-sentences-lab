#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value):
        if isinstance(value, str):
            self.value = value
        else:
            raise ValueError("Value must be a string")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
       
        sentences = re.split(r'[.!?]', self.value)
        
        return len([sentence for sentence in sentences if sentence.strip()])

# test
string = MyString("This is a string! It has three sentences. Right?")
print("Is a sentence:", string.is_sentence())
print("Is a question:", string.is_question())
print("Is an exclamation:", string.is_exclamation())
print("Count of sentences:", string.count_sentences())

