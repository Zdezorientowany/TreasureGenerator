from Treasure import Treasure
import random
import json
import os
from utils import format_text
from tabulate import tabulate
import subprocess

with open('treasures.json') as f:
    tresure_dict = json.load(f)
    
with open('settings.json') as f:
    settings_dict = json.load(f)

MAX = settings_dict["MAX"]

quality = list(settings_dict["quality"].keys())
quality_rarity = list(settings_dict["quality"].values())


material = list(settings_dict["material"].keys())
material_rarity = list(settings_dict["material"].values())


def generate_treasures_for_discord():
    quantity = random.randint(0, MAX)
    result_quality = random.choices(quality,quality_rarity, k=quantity)
    result_material = random.choices(material,material_rarity, k=quantity)
    items = random.choices(tresure_dict["Items"], k=quantity)
    random_items = []
    for i in range(quantity):
        random_items.append(Treasure(items[i]["name"], items[i]["value"], items[i]["size"], result_material[i], result_quality[i]))
    return tabulate([i.to_dict_for_discord() for i in random_items], headers=[])

if __name__ == "__main__":
    os.system("cls || clear")
    while True:
        print(format_text("\n"+"="*75,"main"))  
        print(format_text("-"*28,"dark"),format_text("Treasure Generator","light"),format_text("-"*27,"dark"))
        print("1. ",format_text("Advanced Generate","light"))#Advanced Generator with promtps
        print("2. ",format_text("Quick Generate","light"))#Generate random tresures by one click
        print("3. ",format_text("Quick Generate to DISCORD","light"))#Generate random tresures by one click
        print("4. ",format_text("Options","light"))#You can change crucial variables needed for quick Generate
        print("5. ",format_text("Exit","light"))
        print(format_text("-"*75,"dark")) 
        print(format_text("="*75,"main"))  
        choice = input("Enter your choice: ")
        os.system("cls || clear")

        if choice == "1" or choice == "G" or choice == "Generate":
            print("\033[93m=======Generate treasures=======\033[0m")
            # Add code to execute Option 1 here

        elif choice == "2" or choice == "Q" or choice =="Quick" or choice == "Quick Generate":
            print(format_text("="*30,"dark"),format_text("Quick Generate","light"),format_text("="*29,"dark"))
            quantity = random.randint(0, MAX)
            result_quality = random.choices(quality,quality_rarity, k=quantity)
            result_material = random.choices(material,material_rarity, k=quantity)
            items = random.choices(tresure_dict["Items"], k=quantity)
            print(format_text("\nYou found "+str(quantity)+" items!","main"))
            print(format_text("\n"+"="*75,"dark")) 
            random_items = []
            for i in range(quantity):
                random_items.append(Treasure(items[i]["name"], items[i]["value"], items[i]["size"], result_material[i], result_quality[i]))
            print(tabulate([i.to_dict() for i in random_items], headers=[]))
            print(format_text("="*75,"dark")) 
            print('Total value of items:'+" "*48+ format_text(str(sum(item.value for item in random_items)) + 'g',"light"))
            input()
            os.system("cls || clear")
            
        elif choice == "3" or choice == "D" or choice =="Discord" or choice == "Quick Generate to DISCORD":
            result = subprocess.run(['python', 'bot.py'])

        elif choice == "4" or choice =="O" or choice == "Options":
            print(format_text("="*33,"dark"),format_text("Options","light"),format_text("="*33,"dark"))
            print("Maximum items generated:",format_text(str(MAX),"light"))
            print("\n"+format_text("="*28,"dark"),format_text("Rarity of quality","light"),format_text("="*28,"dark"))
            for x, y in zip(quality, quality_rarity):
                print(x+format_text(": {:.0%}".format(y),"light"))
            print("\n"+format_text("="*28,"dark"),format_text("Rarity of material","light"),format_text("="*27,"dark"))    
            for x, y in zip(material, material_rarity):
                print(x+format_text(": {:.0%}".format(y),"light"))
            print(format_text("\n"+"="*75,"dark")) 
            print(format_text("(Max(m), Quality(Q), Material(M),Exit(E))","main"))
            option = input(format_text("What you want to modify?: ","light"))

            if option == "Max" or option == "m":
                try:
                    MAX = int(input(f"Enter new value for MAX({MAX}): "))
                    settings_dict["MAX"] = MAX
                    with open('settings.json', 'w') as f:
                        json.dump(settings_dict, f, indent=4)
                except ValueError:
                    os.system("cls || clear")
                    print(format_text("Invalid choice. Returning to menu ","false"))
            elif option == "Quality" or option == "Q":
                try:
                    quality_choice = input(f"Enter a quality value ({', '.join([f'{q} ({r})' for q, r in zip(quality, quality_rarity)])}): ")
                    quality_index = quality.index(quality_choice)
                    new_quality_rarity = input(f"Enter a new rarity value for {quality_choice} ({quality_rarity[quality_index]}):")
                    quality_rarity[quality_index] = float(new_quality_rarity)
                    settings_dict["quality"][quality_choice] = quality_rarity[quality_index]
                    with open('settings.json', 'w') as f:
                        json.dump(settings_dict, f, indent=4)
                except ValueError:
                    os.system("cls || clear")
                    print(format_text("Invalid choice. Returning to menu ","false"))
            elif option == "Material" or option == "M":
                try:               
                    material_choice = input(f"Enter a material value ({', '.join([f'{m} ({r})' for m, r in zip(material, material_rarity)])}): ")
                    material_index = material.index(material_choice)
                    new_material_rarity = input(f"Enter a new rarity value for {material_choice} ({material_rarity[material_index]}):")
                    material_rarity[material_index] = float(new_material_rarity)
                    settings_dict["material"][material_choice] = material_rarity[material_index]
                    with open('settings.json', 'w') as f:
                        json.dump(settings_dict, f, indent=4)
                except ValueError:
                    os.system("cls || clear")
                    print(format_text("Invalid input. Returning to menu ","false"))    
            elif option == "Exit" or option == "E":
                print("Returning to menu...")  
            else:
                os.system("cls || clear")
                print(format_text("Invalid choice. Returning to menu ","false"))
            os.system("cls || clear")

        elif choice == "5" or choice =="E" or choice == "Exit":
            print(format_text("Exiting...","light")) 
            break 
        else:
            print(format_text("Invalid choice. Please enter a number between 1 and 4.","false")) 