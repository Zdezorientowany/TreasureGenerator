from utils import format_text
class Treasure:
    
    def __init__(self, _name, _value, _size, _material, _quality):
        self.name = _name
        self.size = _size
        self.material = _material
        self.quality = _quality
        self.value = int(_value * (2 if self.quality == "Flawless" else 1 if self.quality == "Good Quality" else 0.5) * (4 if self.material == "Jeweled" else 3 if self.material == "Gold" else 2 if self.material == "Silver" else 1))
    
    def to_dict(self):
        quality_str = format_text(self.quality, self.quality.lower())
        material_str = format_text(self.material, self.material.lower())
        value_str = format_text(str(self.value)+"g", "value")
        first_column = str(quality_str + " " + material_str + " " + self.name)
        second_column = str(value_str + " - " + self.size)
        return {"First": first_column, "Second": second_column}