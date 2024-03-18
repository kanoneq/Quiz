import sys

print("Welcome in my quiz!")
print()
print("Remember to answer with letters, not whole answers, good luck!")
print()
something = input("are you ready? (answer Y if yes, and anything else if no) ")
if something.upper() == "Y":
    print("okay then, let's go with the quiz!")
else:
    sys.exit("Why did you even launch it when you don't want to play this quiz? :c")

print()
print("How many letters are there in english alphabet?")
print("A - 25")
print("B - 26")
print("C - 20")
print("D - 23")
choice = input("put your answer here: ")
# int stands for a number
if choice.upper() == "B":
    print("yes, you are right! well done")
else:
    sys.exit("no, the correct answer is B (26), good luck next time")

print()

print("What continent is UK located on?")
print("A - Americas (yes, i mean both of them)")
print("B - Africa")
print("C - Asia")
print("D - Europe")
choice_2 = input("your answer: ")

if choice_2.upper() == "D":
    print("that's right! UK is located on Europe!")
else:
    sys.exit("no, the correct answer is D (Europe), try again!")

print()
print("Okay, you are good, next question!")
print()
print("how many days does february have in a leap year?")
print("A - 32")
print("B - 30")
print("C - 28")
print("D - 29")
choice_3 = input("that's the place for your answer (i dare you to answer E) ")

if choice_3.upper() == "E":
    sys.exit("damn, you really have balls of steel to do this")
elif choice_3.upper() == "D":
    print("yup, you are right, congrats")
else:
    sys.exit("nu uh, the correct answer is D (29)")

print()
print("Congratulations user! You just won nothing! I hope you did enjoy the quiz tho")