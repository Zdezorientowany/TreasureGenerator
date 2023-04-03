
colors = {
    "broken": (100, 100, 100),
    "rusted": (100,30,30),
    "polished": (30,100,30),
    "flawless": (30,30,100),
    "enchanted": (100,30,100),

    "copper": (0, 0, 0),
    "silver": (50, 50, 50),
    "gold": (100, 100, 100),
    "jeweled": (150, 150, 150),

    "dark": (54, 79, 89),
    "main": (90,146,148),
    "light": (181,230,211),
    "value": (255, 190, 120),

    "false": (200,0,0)
}

def format_text(text, color,shade="copper"):
    x, y, z = colors[shade]
    r, g, b = colors[color]
    r += x
    g += y
    b += z
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"