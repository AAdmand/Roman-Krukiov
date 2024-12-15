def single_root_words(root_word, *other_words):
    same_words = []
    upper_word = root_word.upper()
    for word in other_words:
        if upper_word in word.upper() or word.upper() in upper_word:
            same_words.append(word)
    return same_words

result = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result)
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result2)