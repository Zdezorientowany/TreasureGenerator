from utils import format_text
class Treasure:
    
    def __init__(self, _name, _value, _size, _material, _quality):
        self.name = _name
        self.size = _size
        self.material = _material
        self.quality = _quality
        self.value = int(_value * (0.25 if self.quality == "broken" else 0.5 if self.quality == "rusty" else 1 if self.quality == "polished" else 1.5 if self.quality == "flawless" else 2) * (4 if self.material == "Jeweled" else 3 if self.material == "Gold" else 2 if self.material == "Silver" else 1))
    
    def to_dict(self):
        quality_str = format_text(self.quality, self.quality.lower(),self.material.lower())
        material_str = format_text(self.material, self.quality.lower(),self.material.lower())
        name_str = format_text(self.name, self.quality.lower(),self.material.lower())
        value_str = format_text(str(self.value)+"g", "value")
        first_column = str(quality_str + " " + material_str + " " + name_str)
        second_column = str(value_str + " - " + self.size)
        return {"First": first_column, "Second": second_column}
    
    def to_dict_no_color(self):
        first_column = str(self.quality + " " + self.material + " " + self.name)
        second_column = str(str(self.value) + "g" + " - " + self.size)
        return {"First": first_column, "Second": second_column}