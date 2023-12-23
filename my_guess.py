from unpack import pick_category
pool = {1: "Animal", 2: "Place", 3: "Names", 4: "Courses"}
def my_guess(frag):
    attempt = 3
    trials = []
    while True:
        pick_category(pool) #calls the user to select a game category and returns category
        guess = input("guess a letter in my word: ")
        if len(guess) == 1 and guess.isalpha():
            frag()
            if guess in trials:
                print("character already tried, try another")
            else:
                if guess not in frag:
                    attempt -=1
                    if attempt > 1:
                        print ("try again, you have {} attempts left".format(attempt))
                    elif attempt == 1:
                        print("try again, you have {} attempt left".format(attempt))
                    else:
                        print("Sorry, you lost")
                        break
                else:
                    if len(trials) != len(frag):
                        print("yeah, keep going. You have {} attempts left". format (attempt))
                    else:
                        print("That is it")
                        break
                trials.append(guess)
        else:
            raise TypeError("Enter single character pls")
