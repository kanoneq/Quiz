import sys
import random

print("Welcome to my quiz!")
print()
print("Remember to answer with answers, basically, if you want to make sure that your answer is correct, you can copy or rewrite it by hand")
print()
something = input("are you ready? (answer Y if yes, and q if no) ")
if something.upper() == "Y":
    print("okay then, let's go with the quiz!")
elif something.upper() == 'Q"':
    sys.exit("Why did you even launch it when you don't want to play this quiz? :c")
else:
    sys.exit("wrong parameter")

print()
print("How many letters are there in english alphabet?")
answers = ["25", "26", "20", "23"]

random.shuffle(answers)
for answer in answers:
    print(answer)
choice = input("put your answer here: ")

if choice.upper() == "26":
    print("yes, you are right! well done")
else:
    sys.exit("no, the correct answer is 26, good luck next time")

print()

print("What continent is UK located on?")

answers = ["north_america", "africa", "asia", "europe"]
random.shuffle(answers)
for answer in answers:
    print(answer)
choice = input("your answer: ")

if choice.upper() == "EUROPE":
    print("that's right! UK is located on Europe!")
else:
    sys.exit("no, the correct answer is europe, try again!")

print()
print("Okay, you are good, next question!")
print()
print("How many days does february have in a leap year?")
answers = ["32", "30", "28", "29"]
random.shuffle(answers)
for answer in answers:
    print(answer)
choice = input("that's the place for your answer: ")

if choice.upper() == "29":
    print("yup, you are right, congrats")
else:
    sys.exit("nu uh, the correct answer is 29")

print()

print("The Gulf stream flows from coast of (it's a really big country): ")
answers = ["Norway", "Idnia", "US", "Australia"]
random.shuffle(answers)
for answer in answers:
    print(answer)
choice = input("insert your answer: ")

if choice.upper() == "US":    
    print("a̟̮̤̳̩͚̟̼̒ͣ͋͛̔̎̿̀r͔͈̼̥̝̭̮̬ͬ̇ͣ͊͆̓̍̒e͎̼̩͉̤̯̦̖ͮ͋ͤ̓ͨͧ̏̐ ̩͕̹̩̘͓͔̖̄̈́̿ͨ͂ͬ̏̑ŷ̜̠̺͈̳̹̱̋̔͊ͤ̅̇̆ͅo͙͖̭̻̺̰͕͓͒͛̽ͮ̓͗̒͊ṵ̰̩̝̭̖̩͖͋͐̽̾ͦͬ̈́̚ ͇̹̤̦̗̙̺̭ͨͬͮ̆ͭ̔ͫ̍s̞͈̺̻̘̣͉̤͋ͩ̉ͭ̉͆̃̚ǘ̞̞̥͙̦̫̼͔ͭ̂ͫͦ̏̋̚r̙͕̘̤̣͚͍͕ͮ̇͋̎ͤ̔̓ͮe̞̰̣͔̗͈͕̙͆ͤͦ̎̄͛̓̐,͎͉̱̦̮̖̺̻͛ͥ̿̌͗̃͛̂ ̩͔̠͔̖͉̣̗̅͗ͧ̎ͥ̒̆̓t̜̱͕̠̲͈̹̱ͥ̽͂͑̈̿ͫͣh͕͎̭͍̬͖̦͙̓͂̄͊̔ͪ̒̉a̙͎͍̻̞̳͈̞ͤ͌̌̔ͨ̋̌̃t͈͉̰̬̩͍̯̙̑̂̋ͯ̓̏̀̓ ̤͔̝͎͕͕̰͍ͧ̈́̎ͭ̅͆̋͐y͎͍͕͕̗̝͉̜̅̓͑̅͆̽ͧͮo͙̖̤̠̦͓̞̰̒̀͌̔ͣ͌̑͌u͖͓̟̬͖͇͎͓̒̐̆ͦ̒̆ͨ̀ ̣̯̤̳̩͖͓͓̆̇͊̆ͤ̍̄ͭa͇͓̭̤̤̘̟̖ͪ̋̆ͬ͒̿̒̈́r̗̰̳̗̜̠͎̫ͦ̋͛͐͐͛̏̎ȅ̞͈̟̫̱̘̗̐ͫ͑̈́ͨ̈͒ͅ ̞̯̖͉͙̜̱̪͒̂ͣͩ͂͂ͦͣa̼̮̞̠̯̬̥͙͂̄͗̆ͨͪ̆ͦl̮̖̝̗̙̮̩̞͛̇̋̐͑͐͑ͬo͈̘̟̳̲̰̙͒̾ͫ͂̋̽͗ͪͅn̖̜̳̪̪̟̼̪ͯ̋̾̑̂̌ͮ̂e͚͖̥̣͓̙̭͚̾̿ͥ͊̊ͭ̃ͧ ̫̻̟͕̟̗͖̫̐̎̄̏̎̃̏̆i̜̪̙͙̤͎̪̭̋͌̔ͣͣ͌̂͒ń̥̰͙͚̹̱̮͈̓ͯͧ̔͛̊̚ ̳̙̳̰͇̪̝̥́̂̋̅̃̀̑̋ỹ̺͇̱̗͓̯̝̂̂̄ͮͬ͌ͬͅo̱̳̬̳̬͚̠͓͛͂̎̆͋̐̆̚u̺͎͖̼͙̹̝̣ͬ͆̽̈̾̎̉ͩr̹̟̺̘̗̩̱̘̾ͪͯ͋̓͋̏̌ ̲̙͖̤̥̩͖ͧ̿̽̈́ͫ̾̃ͪͅr͉͇̻̳̞̲̰͚ͣ͌̂̎ͥͬ̋̋ö͖̥͎̪̯̰̳͕́ͣ͗ͦͫͦ̋̚o̝̹̻̜̳̜̩̗ͩ̒ͦ̐ͣ͗̇ͧm͎͕̟̹̝͎̝̱̂̋͗͐́ͧ̽ͦ?")
else:
    sys.exit("wro◡g op▱ion")
print()
print("w̴͏̧á̸͠t̷̨͠c̷̨͏h̨͏̨ ̷̢̨|̨̕ out")

print("okay!, next question, do you feel comfortable right now? (answer A, B, C, D)")
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
elif choice.upper() == "D":
    sys.exit("very g̛̱͂̈́͢ò̡̎͑҉͇̖͇o̡͈͌ͤ́́d̞̾͘")

print()
print("there is no another question, which means that you won! thank you for participating in this quiz and I hope you did enjoy it")

sys.exit("y̸̵̸̛͒̎ͧͨ̆ͭ̀҉̷̶̷͝҉̶͙̠̖̠̖̕͝ͅo̶̶̟̞̳̤͎̼͍̗̫̹̩ͦͪ͐́ͪ͂̋͛̑͘ͅͅù̶̟͈͖͉̱͑ͮͬ͋ͪ́̐̒͊́̀͡͠ ȁ̻̥̤̗̖͉̝̻̟̪̔̅̉ͪ̾̎̂̄́ͅr̶̡̐͊̉ͪͧ̀̅̉͗͐͜͏͎̺̙̫͔̦̹̰̥eͦ̀ͯ͌͏̷̧̧̢̧̛̛͔̘̟͚̱͔̥̠̩͇͉̦̟̀̀͜ n̸̡̡ͫ̕͞͞͞҉̧̤͍̬̟̕͝ȩ̴̯̞͕͚͉͍̰̺͖̺̰̤̮ͯ̓ͤ̂̅̿ͤ͐͗̉ͪ̓́̿̀͘͜͡ͅvͩ͋͒̅̀̍ͮ̋ͦ̚͏̶̵̨̨͚̯̲̯̤̤͇͉̕͜͞͠͡͝ͅe̴̴͐ͬ̇͗̈́̂͌͡͡͏̴̢̨̨̝̞̥̪̩̝͍̠̕͢͢͡r̢̢̻̫̮̺̻͊̽̋̏́̈̾͗̚ sͣ͋̎̐͛̀ͪ͋̽͛̈́͋̈́ͤ͊҉̴̴̷̴̨̧̘̳̯̺̳̳͓͘͟͟͜͝͞͡a̴̢̢̢̯̱͈͉͇̱̯͙͋̐͒̂͒̒̔̀͘͟f̵̵̶̧̢̨̧̟̖̼̦̮̝͇̼͈̘̅ͪ̃̂͆͑̀ͬ͒͗͆̉ͯͬ̀̕͘̕͝͠e̡̜͓̝̎̉ͬ̈́̀́̀͘͟͠")