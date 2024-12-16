on = True

while (on) :
    word = input("What does Grandma like \n")

    if len(word) > 5 and len(word) < 10 and "g" in word and W not in word:
        print("Grandma likes " + word)
    else :
        print("Grandma doesn't like " + word)