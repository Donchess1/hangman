#module for category selection
import random
#A dictionary of categories
pool = {1: "Animal", 2: "Place", 3: "Names", 4: "Courses", 5: "Plants"}

#Lists of elements each categories
elements = {
        "Plants": ["neem", "cashew"], "Animals": ["lion", "cat", "fish"], "P;aces": ["Nigeria", "Ghana", "Mali"], "Names": ["Tade", "James"]
        }

def pick_category(pool):
    key = int(input("kindly enter your prefered category: "))
    if key in pool:
        value = pool[key]
        print(f"You selected {key} with category {value}")
        pool_elements(key)
    else:
        print("Enter a valid category key" )

def pool_elements(key):

    #create a list of words from a chosen category
    chosen_list = elements.get(key, [])

    #create random word from list
    chosen_word = random.choice(chosen_list)
    return chosen_word
