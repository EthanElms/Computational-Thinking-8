Score = [0,0,0,0,0]

print("this is a test to determine how much you know about space")

Answer = input("what is prograde, A) direction of current orbit, B) Opposite direction of current orbit, C) Down Relative to nearest gravity \n")
Answer = Answer.lower()

if (Answer == "a"):
    Score[0] += 1
elif (Answer != "b" or Answer != "c"):
    print()
else:
    print("Invalid Answer marked as incorrect")


Answer = input("what is prograde, A) direction of current orbit ")
Answer = Answer.lower()

if (Answer == "a"):
    Score[1] += 1
elif (Answer != "b" or Answer != "c"):
    print()
else:
    print("Invalid Answer marked as incorrect")




print("results: \n")
for x in Score:
    if (x == 1):
        print("Correct")
    else:
        print("Incorrect")