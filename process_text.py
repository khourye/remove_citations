import json


def remove_citations(text):
    char = 0
    while char < len(text):
        if text[char] == '[':
            text = text[0:char] + text[char+3:]
        else:
            char += 1

    return text
