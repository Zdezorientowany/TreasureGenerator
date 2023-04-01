from Treasure import Treasure
import random
import json

with open('treasures.json') as f:
    tresure_dict = json.load(f)
    
print(tresure_dict)


MAX = 5
quality = ["Broken", "Good Quality", "Flawless"]
quality_rarity = [0.7, 0.25, 0.05]

material = ["Copper", "Silver", "Gold", "Jeweled"]
material_rarity = [0.65, 0.2, 0.1, 0.05]

print("Welcome to Tresure Generator!")
print("1. Generate treasures")#Advanced Generator with promtps
print("2. Quick Generete")#Generate random tresures by one click
print("3. Options")#You can change crucial variables needed for quick Generate
print("4. Exit")

while True:
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("You chose Option 1.")
        # Add code to execute Option 1 here
    elif choice == "2":
        print("\n=======Quick Generate=======")
        quantity = random.randint(0, MAX)
        result_quality = random.choices(quality,quality_rarity, k=quantity)
        result_material = random.choices(material,material_rarity, k=quantity)
        items = random.choices(tresure_dict["Items"], k=quantity)
        print("You found",quantity,"items!")
        print("============================")
        random_items = []
        for i in range(quantity):
            random_items.append(Treasure(items[i]["name"], items[i]["value"], items[i]["size"], result_material[i], result_quality[i]))
        for i in range(quantity):
            print(random_items[i])
        print("============================")
        print("Total value of items: "+str(sum(item.value for item  in random_items))+"g")
        print("============================\n")
    elif choice == "3":
        print("\n=========Options==========")
        print("Maximum items generated:",MAX)
        print("=====Rarity of quality====")
        for x, y in zip(quality, quality_rarity):
            print(x+": {:.0%}".format(y))
        print("====Rarity of material====")
        for x, y in zip(material, material_rarity):
            print(x+": {:.0%}".format(y))
        print("============================\n")
        option = input("What you want to modify? (Max, Quality, Material): ")
        if option == "Max":
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
        else:
            print("Invalid choice. Returning to menu ")
        print("============================\n")   
    elif choice == "4":
        print("Exiting the menu. Goodbye!")
        break 
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")