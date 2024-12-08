import customtkinter

class Fonts:
    def __init__(self):
        self.family = "Bahnschrift"
        self.title = customtkinter.CTkFont(family = self.family, size = 35, weight = "bold")
        self.modTitle = customtkinter.CTkFont(family = self.family, size = 20, weight = "normal")

class Colors:
    def __init__(self):
        # Ordered from light to dark
        self.transparent = "transparent"
        self.black = "black"
        self.white = "white"
        
        self.cream = "#ede4de"
        self.darkcream = "#d5cdc7" # brownish
        
        self.biscotti = "#dac09b" # subtle
        self.latte = "#d0bca1" # literally like the coffee, darker than biscotti
        self.toffee = "#9f815b" # darker than latte
        self.cocoa = "#80614a" # very dark, like the cocoa seed
        