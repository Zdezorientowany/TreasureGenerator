from colorama import Fore, Style
from utils import format_text
class Treasure:
    
    def __init__(self, _name, _value, _size, _material, _quality):
        self.name = _name
        self.size = _size
        self.material = _material
        self.quality = _quality
        self.value = int(_value * (2 if self.quality == "Flawless" else 1 if self.quality == "Good Quality" else 0.5) * (4 if self.material == "Jeweled" else 3 if self.material == "Gold" else 2 if self.material == "Silver" else 1))
    
    def __str__(self):
        # Format the quality and material
        quality_str = ""
        if self.quality == "Flawless":
            quality_str = Fore.MAGENTA + self.quality + Style.RESET_ALL
        elif self.quality == "Good Quality":
            quality_str = Fore.YELLOW + self.quality + Style.RESET_ALL
        else:
            quality_str = Fore.RED + self.quality + Style.RESET_ALL
        
        material_str = ""
        if self.material == "Jeweled":
            material_str = Fore.RED + self.material + Style.RESET_ALL
        elif self.material == "Gold":
            material_str = Fore.YELLOW + self.material + Style.RESET_ALL
        elif self.material == "Silver":
            material_str = Fore.CYAN + self.material + Style.RESET_ALL
        else:
            material_str = Fore.WHITE + self.material + Style.RESET_ALL
        
        # Format the value
        value_str = Fore.YELLOW + str(self.value) + "g" + Style.RESET_ALL
        
        # Format the size
        size_str = self.size.capitalize()
        
        # Combine all the formatted strings
        item_str = "{:<25} {:<35} {:<15} {:<10}".format(
            "\033[31m{}\033[0m {}".format(quality_str.capitalize(), material_str.capitalize()),
            "\033[36m{}\033[0m".format(self.name),
            "\033[33m{}\033[0m".format(value_str),
            size_str
        )
        
        return item_str