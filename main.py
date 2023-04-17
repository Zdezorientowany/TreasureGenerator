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

with open('presets.json') as f:
    presets_dict = json.load(f)

MAX = settings_dict["MAX"]
MIN = settings_dict["MIN"]

quality = list(settings_dict["quality"].keys())
quality_rarity = list(settings_dict["quality"].values())


material = list(settings_dict["material"].keys())
material_rarity = list(settings_dict["material"].values())

def generate_result_string(header, quantity, items):  
    table = tabulate([i.to_dict_for_discord() for i in items], headers=[]) 
    temp = (55-len(str(header)))
    if temp%2 > 0:
        temp = int(temp/2)+1
        header = str(("="*temp)+" "+header+" "+("="*(temp-1)))
    else:
        temp = int(temp/2)
        header = str(("="*temp)+" "+header+" "+("="*(temp)))
    
    
    return str(header+"\n\n"
               + "You found "+str(quantity)+" items!" + "\n\n" 
               + "="*57 + "\n" 
               + table + "\n" 
               + "="*57 + "\n" 
               + "Total value of items:" + " "*32 + str(sum(item.value for item in items)) + 'g')

if __name__ == "__main__":
    os.system("cls || clear")
    while True:
        print(format_text("\n"+"="*75,"main"))  
        print(format_text("-"*28,"dark"),format_text("Treasure Generator","light"),format_text("-"*27,"dark"))
        print("1. ",format_text("Advanced Generate","light"))#Advanced Generator with promtps
        print("2. ",format_text("Quick Generate","light"))#Generate random treasures by one click
        print("3. ",format_text("Preset Generate","light"))#Generate treasures from preconfigured settings
        print("4. ",format_text("Options","light"))#You can change crucial variables needed for quick Generate
        print("5. ",format_text("Exit","light"))#Close program
        print(format_text("-"*75,"dark")) 
        print(format_text("="*75,"main"))  
        choice = input("Enter your choice: ")
        os.system("cls || clear")
        choice = choice.lower()

        if choice in ("1", "G", "Generate", "Advanced", "A", "Advanced Generate"):
            flag = True
            while flag:
                print(format_text("\n"+"="*75,"main")) 
                print(format_text("-"*28,"dark"),format_text("Advanced Generate","light"),format_text("-"*28,"dark"))
                try:
                    min = input("Enter minimum number of treasure to generate: ")
                    max = input("Enter maximum number of treasure to generate: ")
                    quantity = random.randint(int(min), int(max))

                    quality_values = []
                    print(format_text("Enter rarity for quality of treasures:","main"))
                    for a,b in zip(quality,quality_rarity):
                        b = input(""+a+":")
                        quality_values.append(float(b))

                    material_values = []
                    print(format_text("Enter rarity for material of treasures:","main"))
                    for a,b in zip(material,material_rarity):
                        b = input(""+a+":")
                        material_values.append(float(b))
                    os.system("cls || clear")
                except ValueError:
                    os.system("cls || clear")
                    print(format_text("Invalid input. Try again ","false"))
                    continue
                while True:
                    print(format_text("\n"+"="*75,"main")) 
                    print(format_text("-"*28,"dark"),format_text("Advanced Generate","light"),format_text("-"*28,"dark"))
                    print(format_text("\n"+"="*75,"main"))
                    print(format_text("-"*31,"dark"),format_text("Your Setting","main"),format_text("-"*30,"dark"))
                    print(format_text("-"*75,"dark"))
                    print(format_text("-"*32,"dark"),format_text(" Quantity ","main"),format_text("-"*31,"dark"))
                    print("Minimum:",min, "  Maximum:",max,"  Rolled:",quantity)
                    print(format_text("-"*29,"dark"),format_text(" Quality Rarity ","main"),format_text("-"*28,"dark"))
                    for a,b in zip(quality, quality_values):
                        print(a+": "+str(b), end='  ')
                    print("\n"+format_text("-"*28,"dark"),format_text(" Material Rarity ","main"),format_text("-"*28,"dark"))
                    for a,b in zip(material, material_values):
                        print(a+": "+str(b), end='  ')
                    result_quality = random.choices(quality,quality_values, k=int(quantity))
                    result_material = random.choices(material,material_values, k=quantity)
                    items = random.choices(tresure_dict["Items"], k=quantity)
                    print(format_text("\n"+"-"*75,"dark"))
                    print(format_text("-"*75,"dark"))
                    print(format_text("="*75,"main")) 
                    print(format_text("-"*34,"dark"),format_text("Result","light"),format_text("-"*33,"dark"))
                    print(format_text("\n"+"="*75,"dark")) 
                    random_items = []
                    for i in range(quantity):
                        random_items.append(Treasure(items[i]["name"], items[i]["value"], items[i]["size"], result_material[i], result_quality[i]))
                    print(tabulate([i.to_dict() for i in random_items], headers=[]))
                    print(format_text("="*75,"dark")) 
                    print('Total value of items:'+" "*48+ format_text(str(sum(item.value for item in random_items)) + 'g',"light"))
                    print(format_text("\n"+"-"*75,"dark")) 
                    print(format_text("="*75,"main")) 
                    option = input("1 - Roll again | 2 - Reroll treasures |  3 - Reset | 4 - Print to DISCORD | 5 - Back to menu : ")
                    if option in ("1"):
                        os.system("cls || clear")
                        quantity = random.randint(int(min), int(max))
                    elif option in("2"):
                        os.system("cls || clear")
                    elif option in("3"):
                        os.system("cls || clear")
                        break
                    elif option in ("4"):
                        subprocess.run(['python', 'bot.py', generate_result_string("Advanced Generating",quantity,random_items)])
                        input()
                        os.system("cls || clear")  
                    elif option in("4"):
                        os.system("cls || clear")
                        flag = False
                        break
                    else:
                        os.system("cls || clear")
                        print(format_text("Invalid choice. ","false"))

        elif choice in ("2", "Q", "Quick", "Quick Generate"):
            print(format_text("\n"+"="*75,"main")) 
            print(format_text("-"*30,"dark"),format_text("Quick Generate","light"),format_text("-"*29,"dark"))

            quantity = random.randint(MIN, MAX)
            result_quality = random.choices(quality,quality_rarity, k=quantity)
            result_material = random.choices(material,material_rarity, k=quantity)
            items = random.choices(tresure_dict["Items"], k=quantity)
            print(format_text("\nYou found "+str(quantity)+" items!","light"))
            print(format_text("\n"+"="*75,"dark")) 
            random_items = []
            for i in range(quantity):
                random_items.append(Treasure(items[i]["name"], items[i]["value"], items[i]["size"], result_material[i], result_quality[i]))
            print(tabulate([i.to_dict() for i in random_items], headers=[]))
            print(format_text("="*75,"dark")) 
            print('Total value of items:'+" "*48+ format_text(str(sum(item.value for item in random_items)) + 'g',"light"))
            print(format_text("\n"+"-"*75,"dark")) 
            print(format_text("="*75,"main")) 
            option = input("1 - Print on Discord | 2 - Back to menu : ")
            if option in ("1"):
                subprocess.run(['python', 'bot.py', generate_result_string("Quick Generate",quantity,random_items)])
                input()
                os.system("cls || clear")        
            elif option in("2"):          
                os.system("cls || clear")
        
        elif choice in ("3", "P", "Preset", "Preset Generate", "Pre"):
            flag = True
            while flag:
                print(format_text("\n"+"="*75,"main")) 
                print(format_text("-"*30,"dark"),format_text("Preset Generate","light"),format_text("-"*29,"dark"))
                for i in presets_dict:
                    print(i)
                
                print(format_text("\n"+"-"*75,"dark")) 
                print(format_text("="*75,"main")) 
                choice = input("Which preset you want to use?: ")
                temp = (73-len(str(choice)))/2
                if temp%2 > 0:
                    temp = int(temp)+1
                    header = format_text("-"*temp,"dark")+" "+format_text(str(choice),"light")+" "+format_text("-"*(temp-1),"dark")
                else:
                    temp = int(temp)
                    header = format_text("-"*temp,"dark")+" "+format_text(str(choice),"light")+" "+format_text("-"*(temp),"dark")
                chosen_preset = presets_dict[str(choice)]
                quantity = random.randint(chosen_preset["MIN"], chosen_preset["MAX"])
                while True: 
                    os.system("cls || clear")
                    print(format_text("\n"+"="*75,"main")) 
                    print(header)
                    result_quality = random.choices(list(chosen_preset["quality"].keys()),list(chosen_preset["quality"].values()), k=quantity)
                    result_material = random.choices(list(chosen_preset["material"].keys()),list(chosen_preset["material"].values()), k=quantity)
                    items = random.choices(tresure_dict["Items"], k=quantity)
                    print(format_text("\nYou found "+str(quantity)+" items!","light"))
                    print(format_text("\n"+"="*75,"dark")) 
                    random_items = []
                    for i in range(quantity):
                        random_items.append(Treasure(items[i]["name"], items[i]["value"], items[i]["size"], result_material[i], result_quality[i]))
                    print(tabulate([i.to_dict() for i in random_items], headers=[]))
                    print(format_text("="*75,"dark")) 
                    print('Total value of items:'+" "*48+ format_text(str(sum(item.value for item in random_items)) + 'g',"light"))
                    print(format_text("\n"+"-"*75,"dark")) 
                    print(format_text("="*75,"main"))              
                    option = input("1 - Roll again | 2 - Reroll treasures |  3 - Reset | 4 - Print on DISCORD | 5 - Back to menu : ")
                    if option in ("1"):
                        os.system("cls || clear")
                        quantity = random.randint(chosen_preset["MIN"], chosen_preset["MAX"])
                        continue
                    elif option in("2"):
                        os.system("cls || clear")
                        continue
                    elif option in("3"):
                        os.system("cls || clear")
                        break
                    elif option in ("4"):
                        subprocess.run(['python', 'bot.py', generate_result_string(choice,quantity,random_items)])
                        input()
                        os.system("cls || clear")  
                    elif option in("5"):
                        os.system("cls || clear")
                        flag = False
                        break
                    else:
                        os.system("cls || clear")
                        print(format_text("Invalid choice. ","false"))
                        continue

        elif choice in ("4", "O", "Options"):
            flag = True
            while flag:
                os.system("cls || clear")
                print(format_text("="*75,"main")) 
                print(format_text("-"*33,"dark"),format_text("Options","light"),format_text("-"*33,"dark"))
                print("Minimum items generated:",format_text(str(MIN),"light"))
                print("Maximum items generated:",format_text(str(MAX),"light"))
                print(format_text("-"*28,"dark"),format_text("Rarity of quality","light"),format_text("-"*28,"dark"))
                for x, y in zip(quality, quality_rarity):
                    print(x+format_text(": {:.0%}".format(y),"light"))
                print(format_text("-"*28,"dark"),format_text("Rarity of material","light"),format_text("-"*27,"dark"))    
                for x, y in zip(material, material_rarity):
                    print(x+format_text(": {:.0%}".format(y),"light"))
                print(format_text("-"*34,"dark"),format_text("Presets","light"),format_text("-"*33,"dark"))    
                for i in presets_dict:
                    print(i)
                print(format_text("-"*75,"dark")) 
                print(format_text("="*75,"main")) 

                print(format_text("Min(1) - Max(2) - Quality(3) - Material(4) - Presets(5) - Exit(6)","main"))
                option = input(format_text("What do you want to modify?: ","light"))
                if option in("Min", "1"):
                    try:
                        MIN = int(input(f"Enter new value for MIN: "))
                        settings_dict["MIN"] = MIN
                        with open('settings.json', 'w') as f:
                            json.dump(settings_dict, f, indent=4)
                    except ValueError:
                        os.system("cls || clear")
                        print(format_text("Invalid choice. Returning to menu ","false"))
                        break
                    continue
                elif option in("Max", "2"):
                    try:
                        MAX = int(input(f"Enter new value for MAX: "))
                        settings_dict["MAX"] = MAX
                        with open('settings.json', 'w') as f:
                            json.dump(settings_dict, f, indent=4)
                    except ValueError:
                        os.system("cls || clear")
                        print(format_text("Invalid choice. Returning to menu ","false"))
                        break
                    continue
                elif option in ("Quality", "Q", "3"):
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
                        break
                    continue
                elif option in ("Material", "M", "4"):
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
                        break
                    continue  
                elif option in("Presets", "P", "5"):
                    choice = input(format_text("Wchich preset you want to choose?: ","light"))
                    os.system("cls || clear")
                    while True:
                        print(format_text("\n"+"="*75,"main")) 
                        temp = (73-len(str(choice)))/2
                        if temp%2 > 0:
                            temp = int(temp)+1
                            print(format_text("-"*temp,"dark"),format_text(str(choice),"light"),format_text("-"*(temp-1),"dark"))
                        else:
                            temp = int(temp)
                            print(format_text("-"*temp,"dark"),format_text(str(choice),"light"),format_text("-"*(temp),"dark"))
                        print(format_text("-"*33,"dark"),format_text("Quantity","main"),format_text("-"*32,"dark"))
                        print("Minimum:",presets_dict[str(choice)]["MIN"], "  Maximum:",presets_dict[str(choice)]["MAX"])
                        print(format_text("-"*29,"dark"),format_text(" Quality Rarity ","main"),format_text("-"*28,"dark"))
                        for a,b in zip(presets_dict[str(choice)]["quality"].keys(), presets_dict[str(choice)]["quality"].values()):
                            print(a+": "+str(b), end='  ')
                        print("\n"+format_text("-"*28,"dark"),format_text(" Material Rarity ","main"),format_text("-"*28,"dark"))
                        for a,b in zip(presets_dict[str(choice)]["material"].keys(), presets_dict[str(choice)]["material"].values()):
                            print(a+": "+str(b), end='  ')
                        print(format_text("-"*75,"dark")) 
                        print(format_text("="*75,"main")) 
                        print(format_text("Min(1) - Max(2) - Quality(3) - Material(4) - Exit(5)","main"))
                        option = input(format_text("What do you want to modify?: ","light"))
                        if option in("Min", "1"):
                            try:
                                min = int(input(f"Enter new value for Minimum: "))
                                presets_dict[str(choice)]["MIN"] = min
                                with open('presets.json', 'w') as f:
                                    json.dump(presets_dict, f, indent=4)
                            except ValueError:
                                os.system("cls || clear")
                                print(format_text("Invalid choice. Returning to options ","false"))
                                break
                            os.system("cls || clear")
                            continue
                        
                        elif option in("Max", "2"):
                            try:
                                max = int(input(f"Enter new value for Maximum: "))
                                presets_dict[str(choice)]["MAX"] = max
                                with open('presets.json', 'w') as f:
                                    json.dump(presets_dict, f, indent=4)
                            except ValueError:
                                os.system("cls || clear")
                                print(format_text("Invalid choice. Returning to options ","false"))
                                break
                            os.system("cls || clear")
                            continue
                        
                        elif option in ("Quality", "Q", "3"):
                            try:
                                quality_choice = input(f"Enter a quality value ({', '.join([f'{q} ({r})' for q, r in zip(presets_dict[str(choice)]['quality'].keys(), presets_dict[str(choice)]['quality'].values())])}): ")
                                quality_index = list(presets_dict[str(choice)]['quality'].keys()).index(quality_choice)
                                new_quality_rarity = input(f"Enter a new rarity value for {quality_choice}:")
                                list(presets_dict[str(choice)]['quality'].values())[quality_index] = float(new_quality_rarity)
                                presets_dict[str(choice)]['quality'][quality_choice] = float(new_quality_rarity)

                                with open('presets.json', 'w') as f:
                                    json.dump(presets_dict, f, indent=4)
                            except ValueError:
                                os.system("cls || clear")
                                print(format_text("Invalid choice. Returning to menu ","false"))
                                break
                            os.system("cls || clear")
                            continue
                        elif option in ("Material", "M", "4"):
                            try:
                                material_choice = input(f"Enter a quality value ({', '.join([f'{q} ({r})' for q, r in zip(presets_dict[str(choice)]['material'].keys(), presets_dict[str(choice)]['material'].values())])}): ")
                                material_index = list(presets_dict[str(choice)]['material'].keys()).index(material_choice)
                                new_material_rarity = input(f"Enter a new rarity value for {material_choice}:")
                                list(presets_dict[str(choice)]['material'].values())[material_index] = float(new_material_rarity)
                                print(presets_dict[str(choice)]['material'][material_choice],"Przypisz",list(presets_dict[str(choice)]["material"].values())[material_index])
                                presets_dict[str(choice)]['material'][material_choice] = float(new_material_rarity)

                                with open('presets.json', 'w') as f:
                                    json.dump(presets_dict, f, indent=4)
                            except ValueError:
                                os.system("cls || clear")
                                print(format_text("Invalid choice. Returning to menu ","false"))
                                break
                            os.system("cls || clear")
                            continue
                        elif option in("Exit", "E", "6"):
                            os.system("cls || clear")
                            print("Returning to menu...") 
                            break 

                        break
                    continue 
                elif option in("Exit", "E", "6"):
                    print("Returning to menu...") 
                    os.system("cls || clear")
                    break 
                else:
                    os.system("cls || clear")
                    print(format_text("Invalid choice. Returning to menu ","false"))
                    break

        elif choice in ("5", "E", "Exit"):
            print(format_text("Exiting...","light")) 
            break 
