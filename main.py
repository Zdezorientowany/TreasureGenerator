from Treasure import Treasure
import random
import json
import os
from utils import format_text
from tabulate import tabulate

with open('treasures.json') as f:
    tresure_dict = json.load(f)
    
print(tresure_dict)


MAX = 10
quality = ["Broken", "Good Quality", "Flawless"]
quality_rarity = [0.7, 0.25, 0.05]

material = ["Copper", "Silver", "Gold", "Jeweled"]
material_rarity = [0.65, 0.2, 0.1, 0.05]

os.system("cls || clear")
while True:
    
    print("\n\033[93mWelcome to Treasure Generator!\033[0m")
    print("1. Generate treasures")#Advanced Generator with promtps
    print("2. Quick Generete")#Generate random tresures by one click
    print("3. Options")#You can change crucial variables needed for quick Generate
    print("4. Exit")
    choice = input("What do you want sugar?: ")
    os.system("cls || clear")
    if choice == "1" or choice == "G" or choice == "Generate":
        print("\033[93m=======Generate treasures=======\033[0m")
        # Add code to execute Option 1 here
    elif choice == "2" or choice == "Q" or choice =="Quick" or choice == "Quick Generate":
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
        print(tabulate([i.to_dict() for i in random_items], headers=[]))
        # for i in range(quantity):
            # print(random_items[i])
        print("-" * 75)
        print("\033[92m{:<67} {:<8}\033[0m".format('Total value of items:', str(sum(item.value for item in random_items)) + 'g'))

    elif choice == "3" or choice =="O" or choice == "Options":
        print("\033[93m=======Options=======\033[0m")
        print("Maximum items generated:",MAX)
        print("=====Rarity of quality====")
        for x, y in zip(quality, quality_rarity):
            print(x+": {:.0%}".format(y))
        print("====Rarity of material====")
        for x, y in zip(material, material_rarity):
            print(x+": {:.0%}".format(y))
        print("============================\n")
        option = input("What you want to modify? (Max(m), Quality(Q), Material(M),Exit(E)): ")
        if option == "Max" or option == "m":
            try:
                MAX = int(input("Enter new value for MAX: "))
            except ValueError:
                print("Ivalid input. Please enter a valid integer")
        elif option == "Quality" or option == "Q":
            try:
                quality_choice = input("Enter a quality value (" + ", ".join(quality) + "): ")
                quality_index = quality.index(quality_choice)
                new_quality_rarity = input("Enter a new rarity value for " + quality_choice + ": ")
                quality_rarity[quality_index] = float(new_quality_rarity)
            except ValueError:
                print("Invalid input. Please enter value from 0 to 1")
        elif option == "Material" or option == "M":
            try:               
                material_choice = input("Enter a material value (" + ", ".join(material) + "): ")
                material_index = material.index(material_choice)
                new_material_rarity = input("Enter a new rarity value for " + material_choice + ": ")
                material_rarity[material_index] = float(new_material_rarity)
            except ValueError:
                print("Invalid input. Please enter value from 0 to 1")      
        elif option == "Exit" or option == "E":
            print("Returning to menu...")  
        else:
            print("Invalid choice. Returning to menu ")
        print("============================\n")   

    elif choice == "4" or choice =="E" or choice == "Exit":
        print("\033[93mExiting...\033[0m")
        break 
    else:
        print("\033[91mInvalid choice. Please enter a number between 1 and 4.\033[0m")