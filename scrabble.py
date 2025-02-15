import random
import sys
alphabet = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "C", "C", "D", "D", "D", "D", 
"E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "F", "F", "G", "G", "G", "H", "H", 
"I", "I", "I", "I", "I", "I", "I", "I", "I", "J","K", "L", "L", "L", "L", "M", "M", "N", "N", "N", "N", "N", "N", 
"O", "O", "O", "O", "O", "O", "O", "O", "P", "P", "Q", "R", "R", "R", "R", "R", "R", "S", "S", "S", "S", 
"T", "T", "T", "T", "T", "T", "U", "U", "U", "U", "V", "V", "W", "W", "X", "Y", "Y", "Z"]
sevenL = []
for i in range(7):
    x = random.randint(0, len(alphabet) - 1 )
    sevenL.append(alphabet[x])
    alphabet.remove(alphabet[x])

def wordall(word, letters):
    safety = letters.copy()
    for letter in word:
        if letter in safety:
            safety.remove(letter) 
        else:
            return False
    return True


print(sevenL)
def findword():
    with open("dico_nfa031.txt") as f: sorted_words = sorted(f.read().split(), key=len, reverse=True)
    for line in sorted_words:
        words = line.split()
        for length in range(7, 0, -1):
            for word in words:
                if len(word) == length and wordall(word, sevenL):
                    return word           
    return "There are no possible words"
print (findword())
