import customtkinter

class Fonts:
    def __init__(self):
        self.family = "Bahnschrift"
        self.title = customtkinter.CTkFont(family = self.family, size = 35, weight = "bold")

class Colors:
    def __init__(self):
        # Black, white & brown colors
        self.transparent = "transparent"
        self.cream = "#fffdd0"
        self.latte = "#d0bca1" # literally like the coffee, darker than biscotti
        self.toffee = "#9f815b" # darker than latte
        self.cocoa = "#80614a" # very dark, like the cocoa seed
        self.biscotti = "#dac09b" # subtle, similar
        
        # Yellow colors
        self.strongyellow = "#ffc107"
        self.lightyellow = "#fbff10"
        self.darkyellow = "#191800"
        
        # Blue colors
        self.foxcream = "#ede4de"
        self.bluesky = "#67a7ff"
        self.lightblue = "#c2e9fb"
        self.seafom = "#00c4cd"