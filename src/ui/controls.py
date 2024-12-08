import customtkinter
import styles

class Controls (customtkinter.CTkFrame):
    
    def __init__(self, master):

        # set styles        
        self.colors = styles.Colors() 
        self.fonts = styles.Fonts()
        
        # prepare frame args
        kwargs = {
            "corner_radius": 20,
            "bg_color": self.colors.cocoa, # Change this to change background color
            "fg_color": self.colors.cream, # Leave as transparent always
            "border_color": None,
            "border_width": 0,
            "background_corner_colors": (None, None, None, None)
        } 
        
        # call super with updated kwargs
        super().__init__(master, **kwargs)