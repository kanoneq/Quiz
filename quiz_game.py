import sys

print("Welcome to my quiz!")
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
choice = input("your answer: ")

if choice.upper() == "D":
    print("that's right! UK is located on Europe!")
else:
    sys.exit("no, the correct answer is D (Europe), try again!")

print()
print("Okay, you are good, next question!")
print()
print("How many days does february have in a leap year?")
print("A - 32")
print("B - 30")
print("C - 28")
print("D - 29")
choice = input("that's the place for your answer (I dare you to answer E) ")

if choice.upper() == "E":
    sys.exit("damn, you really have balls of steel to do this")
elif choice.upper() == "D":
    print("yup, you are right, congrats")
else:
    sys.exit("nu uh, the correct answer is D (29)")
print()

print("The Gulf stream flows from coast of (it's a really big country):")
print("A - Norway")
print("D - India")
print("C - USA")
print("D - Australia")
choice = input("insert your answer: ")

if choice.upper() == "C":    
    print("a̟̮̤̳̩͚̟̼̒ͣ͋͛̔̎̿̀r͔͈̼̥̝̭̮̬ͬ̇ͣ͊͆̓̍̒e͎̼̩͉̤̯̦̖ͮ͋ͤ̓ͨͧ̏̐ ̩͕̹̩̘͓͔̖̄̈́̿ͨ͂ͬ̏̑ŷ̜̠̺͈̳̹̱̋̔͊ͤ̅̇̆ͅo͙͖̭̻̺̰͕͓͒͛̽ͮ̓͗̒͊ṵ̰̩̝̭̖̩͖͋͐̽̾ͦͬ̈́̚ ͇̹̤̦̗̙̺̭ͨͬͮ̆ͭ̔ͫ̍s̞͈̺̻̘̣͉̤͋ͩ̉ͭ̉͆̃̚ǘ̞̞̥͙̦̫̼͔ͭ̂ͫͦ̏̋̚r̙͕̘̤̣͚͍͕ͮ̇͋̎ͤ̔̓ͮe̞̰̣͔̗͈͕̙͆ͤͦ̎̄͛̓̐,͎͉̱̦̮̖̺̻͛ͥ̿̌͗̃͛̂ ̩͔̠͔̖͉̣̗̅͗ͧ̎ͥ̒̆̓t̜̱͕̠̲͈̹̱ͥ̽͂͑̈̿ͫͣh͕͎̭͍̬͖̦͙̓͂̄͊̔ͪ̒̉a̙͎͍̻̞̳͈̞ͤ͌̌̔ͨ̋̌̃t͈͉̰̬̩͍̯̙̑̂̋ͯ̓̏̀̓ ̤͔̝͎͕͕̰͍ͧ̈́̎ͭ̅͆̋͐y͎͍͕͕̗̝͉̜̅̓͑̅͆̽ͧͮo͙̖̤̠̦͓̞̰̒̀͌̔ͣ͌̑͌u͖͓̟̬͖͇͎͓̒̐̆ͦ̒̆ͨ̀ ̣̯̤̳̩͖͓͓̆̇͊̆ͤ̍̄ͭa͇͓̭̤̤̘̟̖ͪ̋̆ͬ͒̿̒̈́r̗̰̳̗̜̠͎̫ͦ̋͛͐͐͛̏̎ȅ̞͈̟̫̱̘̗̐ͫ͑̈́ͨ̈͒ͅ ̞̯̖͉͙̜̱̪͒̂ͣͩ͂͂ͦͣa̼̮̞̠̯̬̥͙͂̄͗̆ͨͪ̆ͦl̮̖̝̗̙̮̩̞͛̇̋̐͑͐͑ͬo͈̘̟̳̲̰̙͒̾ͫ͂̋̽͗ͪͅn̖̜̳̪̪̟̼̪ͯ̋̾̑̂̌ͮ̂e͚͖̥̣͓̙̭͚̾̿ͥ͊̊ͭ̃ͧ ̫̻̟͕̟̗͖̫̐̎̄̏̎̃̏̆i̜̪̙͙̤͎̪̭̋͌̔ͣͣ͌̂͒ń̥̰͙͚̹̱̮͈̓ͯͧ̔͛̊̚ ̳̙̳̰͇̪̝̥́̂̋̅̃̀̑̋ỹ̺͇̱̗͓̯̝̂̂̄ͮͬ͌ͬͅo̱̳̬̳̬͚̠͓͛͂̎̆͋̐̆̚u̺͎͖̼͙̹̝̣ͬ͆̽̈̾̎̉ͩr̹̟̺̘̗̩̱̘̾ͪͯ͋̓͋̏̌ ̲̙͖̤̥̩͖ͧ̿̽̈́ͫ̾̃ͪͅr͉͇̻̳̞̲̰͚ͣ͌̂̎ͥͬ̋̋ö͖̥͎̪̯̰̳͕́ͣ͗ͦͫͦ̋̚o̝̹̻̜̳̜̩̗ͩ̒ͦ̐ͣ͗̇ͧm͎͕̟̹̝͎̝̱̂̋͗͐́ͧ̽ͦ?")
else:
    sys.exit("wro◡g op▱ion")
print()
print("w̴͏̧á̸͠t̷̨͠c̷̨͏h̨͏̨ ̷̢̨|̨̕ out")

print("okay!, next question, do you feel comfortable right now?")
print("A - ◆►◡○")
print("B - yes")
print("C - i don't know, maybe yes, maybe no")
print("D - no")
choice = input("p҉͟u͡t̵҉͢ y̷͟͡ơ̸̡͞úŗ̴̡́͜͞ answer here")

if choice.upper() == "A":
    sys.exit("◄̢̪ͯ⁓ͤ̐҉̱͎◆̢̾͌̅ͨͪ͛̕҉̴̙̹̳̣̘͝▱̛͎̖̞͒ͥ̓○̡̰̳̯͒̿̂̿́͟͞ͅ◡̷̣̟͔͖̅͊̏͛͟͜≣̴̌̊͜͏̻̘")
elif choice.upper() == "B":
    print("that's great!, let's go to á̵̵͟͟͜͞͠͝͞ņ̶́́o̴͢͠t̢̡̛́͢͢͠h̀͡e͢҉̷̢̡́͜͠r̡̧͟͟ q͏̴̵̵̷̛́͘͢͡͡͡ư̶͟͢͡͏̡e̴̸̡̢̛͘̕͞͠͞s͏̶̷̴̡̛̛̀́̀̀͢͞t̶̴͜͡į̷̸̛͟͟͢͞͏҉ǫ̵̵̵̵̡́̀̕͟͡ņ̴̧̡̢́͢")
elif choice.upper() == "C":
    sys.exit("v̇͝͏̵̜̟e̴̛̥̓͢r͖̯̾́ͅỳ̸̵̶̛̜̖̺ͨͯ good")
elif choice.uppper() == "D":
    sys.exit("very g̛̱͂̈́͢ò̡̎͑҉͇̖͇o̡͈͌ͤ́́d̞̾͘")

print()
print("there is no another question, which means that you won! thank you for participating in this quiz and I hope you did enjoy it")

sys.exit("y̸̵̸̛͒̎ͧͨ̆ͭ̀҉̷̶̷͝҉̶͙̠̖̠̖̕͝ͅo̶̶̟̞̳̤͎̼͍̗̫̹̩ͦͪ͐́ͪ͂̋͛̑͘ͅͅù̶̟͈͖͉̱͑ͮͬ͋ͪ́̐̒͊́̀͡͠ ȁ̻̥̤̗̖͉̝̻̟̪̔̅̉ͪ̾̎̂̄́ͅr̶̡̐͊̉ͪͧ̀̅̉͗͐͜͏͎̺̙̫͔̦̹̰̥eͦ̀ͯ͌͏̷̧̧̢̧̛̛͔̘̟͚̱͔̥̠̩͇͉̦̟̀̀͜ n̸̡̡ͫ̕͞͞͞҉̧̤͍̬̟̕͝ȩ̴̯̞͕͚͉͍̰̺͖̺̰̤̮ͯ̓ͤ̂̅̿ͤ͐͗̉ͪ̓́̿̀͘͜͡ͅvͩ͋͒̅̀̍ͮ̋ͦ̚͏̶̵̨̨͚̯̲̯̤̤͇͉̕͜͞͠͡͝ͅe̴̴͐ͬ̇͗̈́̂͌͡͡͏̴̢̨̨̝̞̥̪̩̝͍̠̕͢͢͡r̢̢̻̫̮̺̻͊̽̋̏́̈̾͗̚ sͣ͋̎̐͛̀ͪ͋̽͛̈́͋̈́ͤ͊҉̴̴̷̴̨̧̘̳̯̺̳̳͓͘͟͟͜͝͞͡a̴̢̢̢̯̱͈͉͇̱̯͙͋̐͒̂͒̒̔̀͘͟f̵̵̶̧̢̨̧̟̖̼̦̮̝͇̼͈̘̅ͪ̃̂͆͑̀ͬ͒͗͆̉ͯͬ̀̕͘̕͝͠e̡̜͓̝̎̉ͬ̈́̀́̀͘͟͠")