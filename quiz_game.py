questions = ("What is the capital of France?",  
             "How does a blockchain work?",  
             "What are the main principles of object-oriented programming?",  
             "How can I optimize a SQL query for better performance?",  
             "What are the differences between supervised and unsupervised learning?")
options = (
    ("A. London", "B. Paris", "C. Berlin", "D. Madrid", "E. Rome"),  
    ("A. Blockchain is a traditional relational database.", "B. A blockchain is a type of cloud storage.",  
     "C. A blockchain is a single, centralized server.", "D. Blockchain only works with Bitcoin.",  
     "E. A blockchain is a decentralized ledger."),  
    ("A. Encapsulation is a form of encryption.", "B. OOP stands for Overly Optimized Processing.",  
     "C. OOP only exists in Python.", "D. Encapsulation, Abstraction, Inheritance, Polymorphism.",  
     "E. Polymorphism means a class can only have one method."),  
    ("A. Always use SELECT * for better performance.", "B. Never use JOINs in SQL.",  
     "C. Avoid using indexes in large tables.", "D. Use proper indexing.",  
     "E. SQL queries run the same regardless of optimization."),  
    ("A. Supervised learning and unsupervised learning are the same.", "B. Supervised learning has labeled data.",  
     "C. Unsupervised learning is only used in image recognition.", "D. Supervised learning does not require any labels.",  
     "E. Unsupervised learning cannot be used for clustering.")  
)

answers = ("B", "E", "D", "D", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter A/B/C/D/E: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else: 
        print("INCORRECT!")
    question_num += 1
    
    
print("-----------------------------------")
print("             RESULTS               ")    
print("-----------------------------------")

print("Answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

print(f"Score: {score}/5")
score = int(score/len(questions)*100)
print(f"Percent: {score}%")
