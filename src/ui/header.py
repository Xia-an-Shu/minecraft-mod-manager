import customtkinter
import styles

class Header (customtkinter.CTkFrame):
    
    def __init__(self, master):

        # set styles        
        self.colors = styles.Colors() 
        self.fonts = styles.Fonts()
        
        # prepare frame args
        kwargs = {
            "corner_radius": 0,
            "bg_color": self.colors.transparent, # Change this to change background color
            "fg_color": self.colors.transparent, # Leave as transparent always
            "border_color": None,
            "border_width": 0,
            "background_corner_colors": (None, None, None, None)
        }
        
        # call super with updated kwargs
        super().__init__(master, **kwargs)
        
        # other contents
        self.set_title()
        
    def set_title(self):
        self.title = customtkinter.CTkLabel(
            self,
            text="Mod Manager",
            font=self.fonts.title,
            bg_color=self.colors.transparent,
            text_color=self.colors.cocoa
        )
        self.title.place(relx=0.5, rely=0.5, anchor="center")