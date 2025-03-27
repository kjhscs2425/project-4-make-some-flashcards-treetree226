import random

flashcards_easy= {
    "What's Mia's favorite color?": "blue", 
    "Does Mia prefer hot or cold weather?": "cold",
    "What's Mia's favorite animal?" : "rat", #TODO: ADD MORE MAKE WITH LIST
    "T/F:Mia like shrimp chips":"T",
    "One of Mia's favorite bands?": "green day",
    "Mia's boyfriend's name?": "Ryan",
    "What does Mia most commonly draw on other people's paper?": "pig",
    "Favorite teacher?": "ms. chun",
    "When is her birthday?": "november 15",
    "What does she want to be when she grows up?": "chemical engineer"
}

flashcards_hard= {
    "What's Mia's favorite drink at Couver coffee?": "earl gray matcha",
    "Name one of Mia's pet peeves.": "chewing with your mouth open",
    "What does Mia do when she eats good food?": "dance",
    "What food does she HATE?" :"sour cream",
    "What's her mom's name?": "jenny",
    "What smell can she not stand?": "yogurt",
    "What is Mia's favorite Teaspoon order?": "jasmine tea",
    "Her favorite Chinese dish?": "braised duck",
    "Her biggest secret?": "",
    "What could she only wear until the middle of high school?": "leggings",

}
easyquestions= list(flashcards_easy.keys())

randomquestions= random.sample(easyquestions, k=10)

score=0
accuracy= 1
asked=0
for randomquestion in randomquestions:
    response=input(randomquestion)
    if response == flashcards_easy[randomquestion]:
        print("correct!")
        score= score+1
        asked=asked+1
        accuracy=(score/asked)*100
        print(f"""Your score is {score}""")
        print(f"""Your accuracy is {accuracy}%""")
    else:
        print("wrong!")
        asked=asked+1
        accuracy=(score/asked)*100
        print(f"""Your score is {score}""")
        print(f"""Your accuracy is {accuracy}%""")

hardquestions= list(flashcards_hard.keys())
randomquestion1s=random.sample(hardquestions, k=10)

for randomquestion1 in randomquestion1s:
    response=input(randomquestion1)
    if response == flashcards_hard[randomquestion1]:
        print("correct!")
        score= score+1
        asked=asked+1
        accuracy=(score/asked)*100
        print(f"""Your score is {score}""")
        print(f"""Your accuracy is {accuracy}%""")
    else:
        print("wrong!")
        asked=asked+1
        accuracy=(score/asked)*100
        print(f"""Your score is {score}""")
        print(f"""Your accuracy is {accuracy}%""")   

# a=0
# b=30
# c=50
# d=70
# e=100

# FIX THIS PART 

if accuracy <= 29.9999999:
   print(f"""Your accuracy is {accuracy}%. Do you even know her?""")  
if accuracy <=30:
   print(f"""Your accuracy is {accuracy}%. Do you even know her name?""")  
if accuracy <= 50:
   print(f"""Your accuracy is {accuracy}%. I bet you only text her to use her for math answers.""")  
if accuracy <= 70 :
   print(f"""Your accuracy is {accuracy}%. Not bad but could be better.""")  
if accuracy == 100:
   print(f"""Your accuracy is {accuracy}%. YOU ARE WIFEY MATERIAL SLAY GIRL.""") 








