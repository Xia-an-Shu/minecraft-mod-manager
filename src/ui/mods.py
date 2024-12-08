import customtkinter
import styles

class Mods (customtkinter.CTkScrollableFrame):
    
    def __init__(self, master, items=[]):

        # set styles        
        self.colors = styles.Colors() 
        self.fonts = styles.Fonts()
        self.items = items
        
        # prepare frame args
        kwargs = {
            "corner_radius": 20,
            "bg_color": self.colors.cocoa, # Change this to change background color
            "fg_color": self.colors.cream, # Leave as transparent always
            "border_color": None,
            "border_width": 0,
            "scrollbar_fg_color": self.colors.cream,
            "scrollbar_button_color": self.colors.cocoa,
            "scrollbar_button_hover_color": self.colors.black,
            "orientation": "vertical"
        }
        
        # call super with updated kwargs
        super().__init__(master, **kwargs)
        
        # Add items to the frame
        for item in self.items:
            self.add_item(item)
            
    def add_item(self, item):
        label = customtkinter.CTkLabel(self, text=item, font=self.fonts.modTitle, text_color=self.colors.black, bg_color=self.colors.cream)
        label.pack(fill="x", padx=10, pady=5)
        