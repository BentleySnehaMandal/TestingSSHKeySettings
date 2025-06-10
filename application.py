import random

def main():
    print("Welcome to the guessing game.")
    n = random.randint(1, 100)
    tries = 0
    done = False
    while done == False:
        g = input("Enter guess (1-100) or exit: ")
        if g == "exit":
            print("Number was", n)
            done = True
        else:
            try:
                g = int(g)
                tries = tries + 1
                if g == n:
                    print("You win in", tries, "tries")
                    done = True
                else:
                    if g < n:
                        print("Higher")
                    if g > n:
                        print("Lower")
            except:
                print("Not a number")

if __name__ == "__main__":
    main()