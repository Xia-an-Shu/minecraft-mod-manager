import customtkinter
import styles
from ui.mods import Mods
from ui.controls import Controls

class Body (customtkinter.CTkFrame):
    
    def __init__(self, master):

        # set styles        
        self.colors = styles.Colors() 
        self.fonts = styles.Fonts()
        
        # prepare frame args
        kwargs = {
            "corner_radius": 20,
            "bg_color": self.colors.cocoa, # Change this to change background color
            "fg_color": self.colors.transparent, # Leave as transparent always
            "border_color": None,
            "border_width": 0,
            "background_corner_colors": (self.colors.cream, self.colors.cream, None, None)
        }
        
        # call super with updated kwargs
        super().__init__(master, **kwargs)
        
        # other contents
        self.set_modlist()
        self.set_controls()
        
    def set_modlist(self):
        self.mods = Mods(self)
        self.mods.place(relx=0.05, rely=0.1, anchor="nw", relwidth=0.5, relheight=0.8)
        
    def set_controls(self):
        self.controls = Controls(self)
        self.controls.place(relx=0.6, rely=0.1, anchor="nw", relwidth=0.35, relheight=0.8)