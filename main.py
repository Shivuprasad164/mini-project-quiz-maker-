class Question:
    name=input("enter the name") 
    def __init__(self, question, answer): 
        self.question = question          
        self.answer = answer              

    def ask_and_evaluate(self):         
        print(self.question)            
        return self.answer == input()  

question_prompts = [ 
    "From which of the following ? the output will be 32 ?\n(a) print(64//2)\n(b) print(65//2)\n(c) Both of the above\n(d) print(66//2)",

    "print(1000<300) will return ?\n(a) 1000\n(b) 3000\n(c) 300\n(d) None of the above",

    "print(1000==300) will return ?\n(a) True\n(b) False\n(c) Error\n(d) None of the above",

    "What is the use of the '%' operator ? \n(a) To find the division\n(b) To find the remainder\n(c) To find the power\n(d) Nothing",

    "What is the use of the '**' operator ? \n(a) Multiplication \n(b) Square \n(c) Double multiple \n(d) Power",
     
    "How we can convert the given list into the set ? \n(a) list.set() \n(b) set.list() \n(c) set(list) \n(d) None of the above",

    "Which of the following are immutable? \n(a) String \n(b) Tuple \n(c) Dictionary \n(d) List",

    "Can I add elements into a list present inside a tuple? \n(a) Yes \n(b) No",

    "What will be the output of the following code: 'a = (1,2,3) , b = (1,2,3),print(id(a) == id(b))' ,\n(a) true \n(b) false",

    "Which of the Following is False? \n(a) Dict Keys are Unique \n(b) Set Keys are Immutable \n(c) Tuple inside a list can be edited \n(d) List inside a tuple can be edited",


]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "d"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "d"),
    Question(question_prompts[5], "c"),
    Question(question_prompts[6], "a,b"),
    Question(question_prompts[7], "a"),
    Question(question_prompts[8], "b"),
    Question(question_prompts[9], "c"),
]

def run_quiz(questions):           
    score = 0                       
    for question in questions:      
        if question.ask_and_evaluate():     
            score += 1                     
    print(f"You got {score} out of {len(questions)}") 

run_quiz(questions)     
