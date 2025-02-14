sevenL = ["T", "O", "X", "I", "Q", "U", "E"]
def word6(word, letters):
    counter = 0
    for letter in word:
        if letter not in letters:
            counter += 1
    return counter 


print(word6("TOXIQUE", sevenL))