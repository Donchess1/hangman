from category import pick_category, pool, elements
chosen_word = pick_category(pool) #calls the user to select a game category and returns category
def my_guess():
    attempt = 3
    trials = []
    while True:

        guess = input("guess a letter in my word: ")
        if len(guess) == 1 and guess.isalpha():
            if guess in trials:
                print("character already tried, try another")
            else:
                if guess not in chosen_word:
                    attempt -=1
                    if attempt > 1:
                        print ("try again, you have {} attempts left".format(attempt))
                    elif attempt == 1:
                        print("try again, you have {} attempt left".format(attempt))
                    else:
                        print(f"Sorry, you lost. The word is {chosen_word}")

                        break
                else:
                    if len(trials) != len(chosen_word):
                        print("yeah, keep going. You have {} attempts left". format (attempt))
                    else:
                        print("That is it")
                        break
                trials.append(guess)
        else:
            raise TypeError("Enter single character pls")
