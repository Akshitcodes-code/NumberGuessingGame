import random
def difficulty():
    print("E-Easy H-Hard I-Insane")
    while True:
        try:
            diff = input("Enter the difficulty level you want:(E/H/I): ").lower()
            if diff in "ehi":
                break
            else:
                print("Invalid difficulty choice")
        except:
            print("No choice")
    if diff == "e":
        return  1000000000000
    elif diff == "h":
        return 5
    elif diff == "i":
        return 3        

def game():
    give_tries = difficulty()
    while True:
        try:
            a = int(input("Enter any number from(0-100): "))
        except:
            print("Invalid choice")
        rn = random.randint(0,100)
        count = 0
        if a > 100 or a<0:
            print("Invalid response")
        else:
            while count < give_tries:
                if a == rn:
                    print("You win")
                    count+=1
                    break
                else:
                    if a>rn:
                        print("Too High")
                        count+=1
                    elif a<rn:
                        print("Too Low")
                        count+=1
                    if count == give_tries:
                        print("YOU LOST ALL YOUR CHANCES ARE OVER")
                        print("The number was: ",rn)
                    while count<give_tries :
                        a = int(input("Enter any number: "))
                        if a >100 or a<0:
                            print("Invalid response enter again ")
                        else:
                            break            
            print("You took ",count," tries")
            choice = input("Do you want to play again(Y/N): ").lower()
            if choice == "y":
                give_tries = difficulty()
                pass
            elif choice == "n":
                break
            else:
                print("Invalid Choice")
if __name__ == "__main__":
    game()
