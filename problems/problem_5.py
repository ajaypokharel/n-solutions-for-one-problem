"""
todo: Check if a sentence is a pangram. A sentence is a pangram if it contains every English letter alphabet.
"""


# solution 1
def pangram_1(sentence):
    return len(set(sentence)) == 26


# solution 2
def pangram_2(sentence):
    for i in sentence:
        if i not in 'abcdefghijklmnopqrstuvwxyz':
            return False
        return True


# solution 3
def pangram_3(sentence):
    if len(sentence) < 26:
        return False
    return len(sentence(sentence)) == 26

