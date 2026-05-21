from ai import call_gpt

def main():
    x = 0
    salir = False
    while not (x == 4):
        print("----Anime Quiz----")
        print("Choose a category")
        print("1. Battle shonen anime")
        print("2. Sports anime")
        print("3. Romance comedy anime")
        print("4. Exit")
        x = int(input("Choose a option: "))
        
        while not (1<= x <=4):
            x = int(input("Choose a valid option: "))

        if x==1:
            genre = "Battle Shonen anime"
            animequiz(genre)
        elif x==2:
            genre = "Sports anime"
            animequiz(genre)
        elif x==3:
            genre = "Romance comedy anime"
            animequiz(genre)

        
def animequiz(genre):
    exit = "y"
    while not exit == "n": 
        question = call_gpt(f"Ask me a question about {genre}, just tell me the question and make sure it's about technical details. You can ask about which anime a certain character belongs to, how many episodes an anime has, things like that.")
        answergpt = call_gpt(f"Answer {question} in one word. no add end point and quotation marks.")
        
        #New variable to compare user answer and gpt answer
        answer = answergpt.lower()
        
        #print(answergpt)
        print(question)
        
        user_answer = (input("Your Answer: ")).lower()
        
        if user_answer == answer:
            print(f"Congrats! you win, the answer was {answergpt} ")
        else: 
            print(f"You are wrong, the answer is {answergpt}")
        exit = input("Wanna continue? Press N to exit. ").lower()

if __name__ == "__main__":
    main()