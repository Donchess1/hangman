#module for pick_category
import random

#A dictionary of categories
pool = {1: "Animals", 2: "Places", 3: "Names", 4: "Courses", 5: "Plants"}
# a word randomly chosen
#Lists of elements each categories
elements = {
        "Plants": ["neem", "cashew"], "Animals": ["lion", "cat", "fish"], "Places": ["Nigeria", "Ghana", "Mali"], "Names": ["Tade", "James"]
        }

def pick_category(pool):

    while True:
        key = int(input("kindly enter your prefered category: "))
        if key in pool:
            value = pool[key]
            print(f"You selected {key} with category {value}")
            chosen_list = elements.get(value, [])
            chosen_word = random.choice(chosen_list)
            return chosen_word
        else:
            print("Enter a valid category key" )

def swap_spaces(chosen_word):
    trials = []
    word_len = len(chosen_word)
    dash = ['_'] * word_len
    attempt = 3
    while "_" in dash:
        guess = input("what is on your mind: ")
        if len(guess) == 1 and guess.isalpha():
            if guess in trials:
                print("character already tried, try another")
            else:
                trials.append(guess)
                if guess in chosen_word:
                    for index in range(word_len):
                        if chosen_word[index] == guess:
                            dash[index] = guess
                    print(''.join(dash))
                else:
                    print("not in")
