word1 = raw_input("Enter a letter: ")
word = ["S","P","A","C","E","M","A","N"]
word_reveal = ["","","","","","","",""]
victory = False
spaceman = False
while (victory != True) and (spaceman != True):
    for i in range(0, len(word)):
        if word1 == word[i]:
            word_reveal[i] = word[i]
        else:
            pass
    print(word_reveal)
    victory = True
