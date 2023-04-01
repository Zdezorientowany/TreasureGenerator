from Treasure import Treasure
import random

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
        print("=======Quick Generate=======.")
        quantity = random.randint(0, MAX)
        result_quality = random.choices(quality,quality_rarity, k=quantity)
        result_material = random.choices(material,material_rarity, k=quantity)
        print(result_quality,result_material)

    elif choice == "3":
        print("You chose Option 3.")
        # Add code to execute Option 3 here
    elif choice == "4":
        print("Exiting the menu. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")