

def hangman(word):
    oportunities = 0
    used_list = []
    unknown_list = ["*"]*len(word)
    number_tokens = len(word)
    while oportunities < 6 and number_tokens != 0:
        letter = input("Enter a letter:")
        if letter == used_list:
            print("The letter was used")
            continue
        else:
            used_list.append(letter)
            found = False
        for index in range(len(word)):
            if letter == word[index]:
                unknown_list[index] = letter
                number_tokens -= 1
                found = True
        if not found:
            print("Error")
            oportunities += 1
    if number_tokens == 0:
        print("User won:", unknown_list)
    else:
        print("Game Over:", word)
hangman("algebra")


