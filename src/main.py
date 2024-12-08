import customtkinter
import styles
from ui.header import Header
from ui.body import Body

# CTtinker: Custom tkinter for modern GUIs
# Docs: https://customtkinter.tomschimansky.com/documentation/windows/window
# Git: https://github.com/TomSchimansky/CustomTkinter?tab=readme-ov-file

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.assets_path = "./assets"
        icon_path = f"{self.assets_path}/icos/ghost.ico"
        
        # ~ ~ ~ ~ ~ ~ ~ ~ App setup ~ ~ ~ ~ ~ ~ ~ ~ #
        
        # Load styles
        self.fonts = styles.Fonts()
        self.colors = styles.Colors()
        
        self.configure(fg_color=self.colors.cream)

        # Center the window
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = 735
        window_height = 412
        center_x = int((screen_width - window_width) / 2 + window_width*0.1)
        center_y = int((screen_height - window_height) / 2)

        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.resizable(False, False)
        self.title("Mod Manager")

        # Change the window icon
        self.iconbitmap(icon_path)

        # ~ ~ ~ ~ ~ ~ ~ ~ Content ~ ~ ~ ~ ~ ~ ~ ~ #
        self.header = Header(self)
        self.body = Body(self)
        
        # place content
        self.header.place(relx=0, rely=0, anchor="nw", relwidth=1.0001, relheight=0.2)
        self.body.place(relx=0, rely=0.2, anchor="nw", relwidth=1.0001, relheight=0.8)

if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

    app = App()
    app.mainloop()