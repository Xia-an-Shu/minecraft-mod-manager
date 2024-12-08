import customtkinter
import styles
from model.mod import Mod

class ModCard (customtkinter.CTkFrame):
    
    def __init__(self, master, mod: Mod):
       
        self.colors = styles.Colors() 
        self.fonts = styles.Fonts()
        self.mod = mod
        
        # prepare frame args
        kwargs = {
            "corner_radius": 10,
            "bg_color": self.colors.cream,
            "fg_color": self.colors.biscotti,
            "border_color": None,
            "border_width": 0,
            "background_corner_colors": (None, None, None, None),
            "height":55,
            "width": 100
        } 
        
        # call super with updated kwargs
        super().__init__(master, **kwargs)
        
        # add mod info
        self.set_title()
        
    def set_title(self):
        self.title = customtkinter.CTkLabel(
            self,
            text=self.mod.name,
            font=self.fonts.modTitle,
            bg_color=self.colors.transparent,
            text_color=self.colors.cocoa
        )
        self.title.place(relx=0.5, rely=0.5, anchor="center")