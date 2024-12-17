Score = [0,0,0,0,0]

print("this is a test to determine how much you know about space\n")

Answer = input("what is prograde \nA) direction of current orbit \nB) Opposite direction of current orbit \nC) Down Relative to nearest gravity \n")
Answer = Answer.lower()

if (Answer == "a"):
    Score[0] += 1
elif (Answer != "b" or Answer != "c"):
    print("Invalid Answer marked as incorrect")
    

Answer = input("How many planets are there in the solar system \nA) 5 \nB) 9 \nC) 8")
Answer = Answer.lower()

if (Answer == "b"):
    Score[1] += 1
elif (Answer != "a" or Answer != "c"):
    print("Invalid Answer marked as incorrect")


Answer = input("DeltaV \nA) 5 \nB) 9 \nC) 8")
Answer = Answer.lower()

if (Answer == "a"):
    Score[2] += 1
elif (Answer != "b" or Answer != "c"):
    print("Invalid Answer marked as incorrect")


print("results: \n")
for x in Score:
    if (x == 1):
        print("Correct")
    else:
        print("Incorrect")