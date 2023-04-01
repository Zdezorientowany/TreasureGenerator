from Treasure import Treasure
import random
import json
import os
import colorama

with open('treasures.json') as f:
    tresure_dict = json.load(f)
    
print(tresure_dict)


MAX = 5
quality = ["Broken", "Good Quality", "Flawless"]
quality_rarity = [0.7, 0.25, 0.05]

material = ["Copper", "Silver", "Gold", "Jeweled"]
material_rarity = [0.65, 0.2, 0.1, 0.05]

colorama.init()
os.system("cls || clear")
while True:
    
    print("\n\033[93mWelcome to Treasure Generator!\033[0m")
    print("1. Generate treasures")#Advanced Generator with promtps
    print("2. Quick Generete")#Generate random tresures by one click
    print("3. Options")#You can change crucial variables needed for quick Generate
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    os.system("cls || clear")
    if choice == "1":
        print("\033[93m=======Generate treasures=======\033[0m")
        # Add code to execute Option 1 here
    elif choice == "2":
        print("\033[93m=======Quick Generate=======\033[0m")
        quantity = random.randint(0, MAX)
        result_quality = random.choices(quality,quality_rarity, k=quantity)
        result_material = random.choices(material,material_rarity, k=quantity)
        items = random.choices(tresure_dict["Items"], k=quantity)
        print("\nYou found",quantity,"items!\n")
        print("-" * 75)
        random_items = []
        for i in range(quantity):
            random_items.append(Treasure(items[i]["name"], items[i]["value"], items[i]["size"], result_material[i], result_quality[i]))
        for i in range(quantity):
            print(random_items[i])
        print("-" * 75)
        print("\033[92m{:<67} {:<8}\033[0m".format('Total value of items:', str(sum(item.value for item in random_items)) + 'g'))
    elif choice == "3":
        print("\033[93m=======Options=======\033[0m")
        # Add code to execute Option 3 here
    elif choice == "4":
        print("\033[93mExiting the menu. Goodbye!\033[0m")
        break 
    else:
        print("\033[91mInvalid choice. Please enter a number between 1 and 4.\033[0m")