word_dict = {}
text = input("Please enter a sentence: ")
words = text.split()
for word in words:
    quantity = word_dict.get(word, 0)
    word_dict[word] = quantity + 1

words = list(word_dict.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_dict[word]))