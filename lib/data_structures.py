spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    # using a for loop
    # names = []
    # for food in spicy_foods :
    #     names.append( food['name'] )
    # return names

    # using a map function and turning the return value into a list
    # return list( map( lambda food : food['name'], spicy_foods ) )
    
    # using a list comprehension
    return [ food['name'] for food in spicy_foods ]

def get_spiciest_foods(spicy_foods):
    # For Loop Option 1 
    # name = []
    # for food in spicy_foods:
    #     if food["heat_level"] > 5:
    #         name.append(food)
    # return name 
    
    return [food for food in spicy_foods if food["heat_level"] > 5] #list comprehension option2 

def print_spicy_foods(spicy_foods):
    for food in spicy_foods : 
# for loop that  iterates over each dictionary in the spicy_foods list. It extracts the name, cuisine, and heat level of each food item and prints them in the specified format
        print( f"{ food['name'] } ({ food['cuisine'] }) | Heat Level: { '🌶' * food['heat_level'] }" )

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods : #sets up a loop that iterates over each item in the spicy_foods collection.
        if food['cuisine'] == cuisine : # If condition food['cuisine'] == cuisine is true, it means that the current food item matches the desired cuisine.
            return food # exits the loop and immediately returns the matching food item


def print_spiciest_foods(spicy_foods):
    # spiciest_foods = get_spiciest_foods( spicy_foods ) // Option 1
    # print_spicy_foods( spiciest_foods ) // Option 1

    print_spicy_foods( get_spiciest_foods( spicy_foods ) ) # option 2 

# for food in spicy_foods: // Option 2 - A For loop 
#         heat = '🌶' * food['heat_level'] // Creates a string composed of the chili pepper emoji repeated food['heat_level'] times.
#         print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat}")

def get_average_heat_level(spicy_foods): #returns average heat_levels in spicy_foods
    total_heat_level = 0
    for food in spicy_foods : #foor loop that iterates over each item in spicy_foods
        total_heat_level += food['heat_level'] #retrieves the heat level value from the current food and adds that value to the running total.
    return round( total_heat_level / len( spicy_foods ) ) 



def create_spicy_food(spicy_foods, spicy_food): #function that returns original list of spicy foods with new spicy_food added.
    spicy_foods.append(spicy_food)
    return spicy_foods
