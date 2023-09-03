import time
import sys 
Questions = [{'question': 'Is Elephant mammal?', 'ans': 'yes'}]

def home():
    
    print("\n+-----------------------------------------------------+\n")
    print("What Do you want to do?\n")
    print("[1]Test. [2]Edit Question. [3]View Questions. [4]Quit.\n")
    print("\n+-----------------------------------------------------+\n")
    m = input()
    match m:
        case "1":
            print("Entering Test....\n")
            test()
        case "2":
            print("Editing Mode.\n")
            edit()
        case "3":
            print("Viewing Test.\n")
            view()
        case "4":
            sys.exit("You quit the game. Bye bye!\n")
        case _:
            print("invalid input.\n")
            home()



def test():
    score = 0
    if len(Questions) == 0: 
        print("\n+-----------------------------------------------------+\n")
        print("Please Add some question!")
        print("\n+-----------------------------------------------------+\n")
        home()
    else: 
        print("\n+-----------------------------------------------------+\n")
        print("Press enter to proceed..., please answer in small letters")
        print("\n+-----------------------------------------------------+\n")
        x = input()
        if x == "":
            print("\n+-----------------------------------------------------+\n")
            for q in Questions:
                print(q['question']+"\n")
                inans = input()
                if inans == q['ans']:
                    print("\n\n-------------------Correct!!-------------------")
                    score += 1
                else :
                    print("\n\n-------------------Sorry, incorrect!!-------------------")
            print("\n+-----------------------------------------------------+\n")
            print(f"Game Over, your score is {score}\n\n\n")
            print("\n+-----------------------------------------------------+\n")
        else:
            test()
        for i in range(3, 0, -1):
            print(f"Jumping to home page in {i}", end ='\r', flush=True)
            time.sleep(1)  # Delay for 1 second
        home() 

def edit():
    print("\n+-----------------------------------------------------+\n")
    print("This is the edit page...\n")
    questionin = input("Type a question.\n")
    ansinn = input("Type the answer.\n")

    Questions.append({'question': questionin, 'ans': ansinn})
    print(f"\nThis is the question:  {questionin}\n\n The answer is {ansinn}\n\n")
    print("\n+-----------------------------------------------------+\n")
    while True:
        y = input("Do you want to add more questions? (y/n):")
        if y == 'y': 
            edit()
        elif y == 'n': 
            home()
        else:
            pass
    
  
def view(): 
    print("\n+-----------------------------------------------------+\n")
    input("Press any key to continue...")
    i = 0
    for q in Questions:
        print(f"--------------Question {i+1}--------------\n")
        print(q['question']+"\n")
        print(f"---------Answer for Question {i+1}--------\n")
        print(q['ans']+"\n")
        i+=1
    print("--------------End of Question List--------------")
    print("\n+-----------------------------------------------------+\n")
    input("\nPress any key to continue...\n")
    home()
        

def main():
    home()

if __name__ == "__main__":
    main()

