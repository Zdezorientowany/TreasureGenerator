
colors = {
    "copper": (210, 77, 0),
    "silver": (192, 192, 192),
    "gold": (255, 189, 27),
    "broken": (128, 128, 128),
    "good": (100,200,150),
    "flawless": (255, 165, 0),
    "jeweled": (160, 32, 240),
    "dark": (54, 79, 89),
    "main": (90,146,148),
    "light": (181,230,211),
    "value": (100,200,150),
    "false": (200,0,0)
}

def format_text(text, color):
    r, g, b = colors[color]
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"