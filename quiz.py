quiz = {
    "question1":{
        "question" :  "what is the capital of france",
        "answer" : "paris"
    },
    
     "question2":{
        "question" :  "what is the capital of germany",
        "answer" : "Barlin"
    } ,
     
      "question3":{
        "question" :  "what is the capital of italy",
        "answer" : "Roma"
    },
       "question4":{
        "question" :  "what is the capital of Spain",
        "answer" : "Madrid"
    },
        "question1":{
        "question" :  "what is the capital of Portugal",
        "answer" : "Lisbon"
    },
         "question1":{
        "question" :  "what is the capita;l of Switzerland",
        "answer" : "Bem"
    }
}
score = 0
for key , value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")
    if answer.lower() == value['answer'].lower():
        print("correct")
        score = score +1
        print("your score is " + str(score))
    else:
        print("wrong!")
        print(" the answer is : " + value['answer'])
        print("your score is " + str(score))
        