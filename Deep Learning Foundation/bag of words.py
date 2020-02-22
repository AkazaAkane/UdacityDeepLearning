test_text = 'the quick brown fox jumps over the lazy dog'

# version 1
def bag_of_words(text):
    text = text.split(" ")
    dic = {}
    for i in text:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic

print(bag_of_words(test_text))

# version 2
from collections import Counter

def bag_of_words(text):
    # TODO: Implement bag of words
    return Counter(text.split())

print(bag_of_words(test_text))
