import os
import json
d ={}
if os.path.exists("responses.json"):
    with open("responses.json", "r") as f:
        d = json.load(f)
responses = {}
for question in d:
    responses [question] = d[question]
answers = {}

def loose_equals (a,b):
    return a.lower() ==b.lower()

def ask_question(question, answer):

    last_response = ""
    if question in responses: 
      
        last_response = responses[question][-1]

    if loose_equals(last_response , answer): 
        return
    print(question)
    response = input()
    if question in responses:
        responses[question ].append (response)
    else:
        responses[question] = [response]
    print(f"{response = }")
    if loose_equals (response, answer):
        print("good job")
    else:  
        print("bad job")



ask_question("What is the captial of France", "Paris")
ask_question("What year did the Berlin Wall fall?", "1989")
ask_question("What is the chemical symbol for water" ,"H2O")
ask_question("What is the biggest city in Turkey" ,"Istanbul")
ask_question("Is learning mandarin diffcult", "Yes it is")
ask_question("What is the population of San Francisco" ,"808,988")
ask_question("What city will host the 2032 Summer Olympics" , "Brisbane")
ask_question("What country will host the 2027 Womens World Cup" ,"Brazil")
ask_question("What year did the USA drop the atomic bomb on Hiroshima" ,"1945")
ask_question("What is the chemical symbol for hydroxide", "OH-")
ask_question("What city is the center of Europe" ,"Bernotai in Lithuania")
ask_question("What year was the city of Barcelona founded" , "1899")
ask_question("When did the first gamboy come out" , "April 21 1989")
ask_question("What city will host the 2026 Super Bowl" , "San Francisco")
ask_question("What day was the 1994 Northridge Earthquake" , "January 17th")
ask_question("What is your favorite class" , "Computer Science")
ask_question("What is the population of New York City" , "8.258 Million")
ask_question("What is your favorite animal" , "Dogs")
ask_question("Who made the first car" , "Henry Ford")
ask_question("How old is Dr EB" , "39")
ask_question("What is you favorite food" , "Pasta")

import json
with open("responses.json", "w") as f:
    json.dump(responses,f)
