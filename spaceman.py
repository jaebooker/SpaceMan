word = ["S","P","A","C","E","M","A","N"]
word_reveal = ["","","","","","","",""]
spaceman = 0
count = 0
while (count < len(word_reveal)) and (spaceman < 7):
    word1 = raw_input("Enter a letter: ").upper()
    counter = 0
    for i in range(0, len(word)):
        if word1 == word[i]:
            word_reveal[i] = word[i]
            count += 1
        else:
            counter += 1
    if counter == len(word)-1:
        spaceman += 1
    print(word_reveal)
