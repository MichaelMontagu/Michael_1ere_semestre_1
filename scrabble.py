import random
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J","K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
sevenL = []
for i in range(7):
    i = random.randint(0, 25)
    sevenL.append(alphabet[i])
print(sevenL)
sevenL = ["T", "O", "X", "I", "Q", "U", "E"]
with open("dico_nfa031.txt", "r") as file:
    for line in file:
        word = line.strip()  
        if len(word) != 7:   
            continue
        available_letters = sevenL.copy()
        for letter in sevenL:
            if letter not in word:
                continue
            else:
                print(word)    

