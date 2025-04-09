import random
import json


# read file
with open("questions.json", "r") as f:
    c=json.load(f)



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

# what is the lowest number correct 
lowest_number_correct = 1000000
for q, right in c.items():
    if right < lowest_number_correct:
        lowest_number_correct=right

# lowest number correct easy questions
wrong_easy = {}
for q, answer in flashcards_easy.items():
    right=c[q]
    if right==lowest_number_correct:
        wrong_easy[q]=answer
    


# highest number correct easy questions
right_easy = {}
for q, answer in flashcards_easy.items():
    right=c[q]
    if right!=lowest_number_correct:
        right_easy[q]=answer

# lowest number correct hard questions
wrong_hard = {}
for q, answer in flashcards_hard.items():
    right=c[q]
    if right==lowest_number_correct:
        wrong_hard[q]=answer


# highest number correct hard questions
right_hard = {}
for q, answer in flashcards_hard.items():
    right=c[q]
    if right!=lowest_number_correct:
        right_hard[q]=answer

score=0
accuracy= 1
asked=0

def show_questions(flashcards):
    global score
    global accuracy
    global asked
    questions= list(flashcards.keys())
    randomquestions= random.sample(questions, k=len(questions))
    for randomquestion in randomquestions:
        response=input(randomquestion)
        if response == flashcards[randomquestion]:
            print("correct!")
            score= score+1
            asked=asked+1
            accuracy=(score/asked)*100
            print(f"""Your score is {score}""")
            print(f"""Your accuracy is {accuracy}%""")
            c[randomquestion]+=1
        else:
            print("wrong!")
            asked=asked+1
            accuracy=(score/asked)*100
            print(f"""Your score is {score}""")
            print(f"""Your accuracy is {accuracy}%""")
            print(f"""The answer is {flashcards[randomquestion]}.""") 

show_questions(wrong_easy)
show_questions(right_easy)
show_questions(wrong_hard)
show_questions(right_hard)

if accuracy <= 30:
   print(f"""Your accuracy is {accuracy}%. Do you even know her?""")  
elif accuracy <=50:
   print(f"""Your accuracy is {accuracy}%. Do you even know her name?""")  
elif accuracy <= 70:
   print(f"""Your accuracy is {accuracy}%. I bet you only text her to use her for math answers.""")  
elif accuracy == 100:
   print(f"""Your accuracy is {accuracy}%. YOU ARE WIFEY MATERIAL SLAY GIRL.""") 

# read file
with open("data.json", "r") as f:
    d=json.load(f)

     # add new accuracy to the games list
    d["game"].append(accuracy)

with open("data.json","w") as f:
    json.dump(d,f, indent=2)
    
with open("questions.json", "w") as f:
    json.dump(c,f, indent=2)

print(f"""Previous accuracies were {d["game"]}""")




