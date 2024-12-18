#begining
#array stores score
Score = [0,0,0,0,0]

print("this is a test to determine how much you know about space\n")

#Middle
Answer = input("what is prograde \nA) direction of current orbit \nB) Opposite direction of current orbit \nC) Down Relative to nearest gravity \n")
#makes it lower case
Answer = Answer.lower()

if (Answer == "a"):
    Score[0] += 1
    #records answer in array depending on question
elif (Answer != "b" or Answer != "c"):
    #invalid answer marked as wrong
    print("Invalid Answer marked as incorrect")
    

Answer = input("How many planets are there in the solar system \nA) 5 \nB) 9 \nC) 8")
Answer = Answer.lower()

if (Answer == "c"):
    Score[1] += 1
elif (Answer != "a" or Answer != "b"):
    print("Invalid Answer marked as incorrect")


Answer = input("What is DeltaV \nA) Change in velocity \nB) Current velocity \nC) Mass\n")
Answer = Answer.lower()

if (Answer == "a"):
    Score[2] += 1
elif (Answer != "b" or Answer != "c"):
    print("Invalid Answer marked as incorrect")

Answer = input("Most effective place to do a prograde burn \nA) Midpoint \nB) apoapsis \nC) Periapsis\n")
Answer = Answer.lower()

if (Answer == "c"):
    Score[3] += 1
elif (Answer != "b" or Answer != "a"):
    print("Invalid Answer marked as incorrect")


Answer = input("Roughly how many stars are there in the galaxy \nA) 100 Million \nB) Current velocity \nC) Mass\n")
Answer = Answer.lower()

if (Answer == "b"):
    Score[4] += 1
elif (Answer != "a" or Answer != "c"):
    print("Invalid Answer marked as incorrect")

#end
print("results: \n")
#prints array
for x in Score:
    if (x == 1):
        print("Correct")
    else:
        print("Incorrect")