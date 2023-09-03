import time
Questions = {'tag' : '1', 'question': 'Is Elephant mammal?', 'ans': 'yes'}

def home():
    
    print("What Do you want to do?\n")
    print("[1] Test.  [2] Edit Question.  [3] View Questions.\n")
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



def test():
    score = 0
    if len(Questions) == 0: 
        print("Please Add some question!")
        home()
    else: 
        print("Press enter to proceed..., please answer in small letters")
        x = input()
        if x == "":
            for q in Questions:
                if q == 'question':
                    print(Questions[q]+"\n")
                if q == 'ans':
                    inans = input()
                    if inans == Questions[q]:
                        print("Correct!!")
                        score += 1
                    else :
                        print("Sorry, incorrect!!")
            
            print(f"Game Over, your score is {score}\n\n\n")
        else:
            test()
        for i in range(3, 0, -1):
            print(f"Jumping to home page in {i}", end ='\r', flush=True)
            time.sleep(1)  # Delay for 1 second
        home() 

def edit():
    pass

def view():
    pass

def main():
    home()

if __name__ == "__main__":
    main()

