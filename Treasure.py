class Treasure:
    
    def __init__(self, _name, _value, _size, _material, _quality):
        self.name = _name
        self.size = _size
        self.material = _material
        self.quality = _quality
        self.value = int(_value * (2 if self.quality == "Flawless" else 1 if self.quality == "Good Quality" else 0.5) * (4 if self.material == "Jeweled" else 3 if self.material == "Gold" else 2 if self.material == "Silver" else 1))
    
    def __str__(self):
        return f"""{self.material} {self.quality} {self.name} - {self.value}g - {self.size}"""

