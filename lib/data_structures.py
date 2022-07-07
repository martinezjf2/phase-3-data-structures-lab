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
    }
]

def get_names(spicy_foods):
    
    # Strategy 1: Breaking Down Concepts
    # new_list = []
    # for food in spicy_foods:
    #     food_name = food["name"]
    #     new_list.append(food_name)
    # return new_list
    
    # Strategy 2: Using List comprehension
    new_list = [food['name'] for food in spicy_foods]
    return new_list


def get_spiciest_foods(spicy_foods):
    
    # Strategy 1: Breaking Down Concepts
    # new_list = []
    # for food in spicy_foods:
    #     heat_level = food["heat_level"]
    #     if (heat_level > 5):
    #         new_list.append(food)
    # return new_list
    
    # Strategy 2: Using List comprehension
    new_list = [food for food in spicy_foods if food["heat_level"] > 5]
    return new_list
    pass

def print_spicy_foods(spicy_foods):
    # Strategy 1: Breaking Down Concepts
    for food in spicy_foods:
        # heat_level = "🌶" * food['heat_level']
        # print(heat_level)
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")
    
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    

def sort_by_heat(spicy_foods):
    # Resource on this: https://note.nkmk.me/en/python-dict-list-sort/
    return sorted(spicy_foods, key=lambda x: x['heat_level'])
    # for food in spicy_foods:
        
    pass

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food['heat_level'] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

    pass

def get_average_heat_level(spicy_foods):
    i = 0
    for food in spicy_foods:
        i = i + food['heat_level']
    i = i / len(spicy_foods)
    return i
    pass
