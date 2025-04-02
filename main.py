import random
import json

flashcards_easy= {
    "What's Mia's favorite color?": "blue", 
    "Does Mia prefer hot or cold weather?": "cold",
    "What's Mia's favorite animal?" : "rat", 
    "T/F:Mia like shrimp chips":"T",
    "One of Mia's favorite bands?": "green day",
    "Mia's boyfriend's name?": "ryan",
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
        print(f"""The answer is {flashcards_easy[randomquestion]}.""") 

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
        print(f"""The answer is {flashcards_hard[randomquestion1]}.""")  

if accuracy <= 30:
   print(f"""Your accuracy is {accuracy}%. Do you even know her?""")  
elif accuracy <=50:
   print(f"""Your accuracy is {accuracy}%. Do you even know her name?""")  
elif accuracy <= 70:
   print(f"""Your accuracy is {accuracy}%. I bet you only text her to use her for math answers.""")  
elif accuracy == 100:
   print(f"""Your accuracy is {accuracy}%. YOU ARE WIFEY MATERIAL SLAY GIRL.""") 

# with open "main.txt", "w" as f:
#     f.write("__")

# read file
with open("data.json", "r") as f:
    d=json.load(f)

     # add new accuracy to the games list
    d["game"].append(accuracy)

with open("data.json","w") as f:
    json.dump(d,f)

#FIX HERE
print(f"""Previous accuracies were {d["game"]}""")





