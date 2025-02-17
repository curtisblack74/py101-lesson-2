def titlize(sentence):
    words = sentence.split()
    new_words = []

    for word in words:
        if len(word) > 2:
            word = word.capitalize()
            # print(word)        # Delete line
            new_words.append(word)
        else:
            new_words.append(word)

    return ' '.join(new_words)

title = 'hello world of programming'
print(titlize(title))
# titlize(title)