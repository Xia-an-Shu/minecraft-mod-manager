import customtkinter
import tkinter as tk
import styles.colors as co
import styles.fonts as fo
import gui

from PIL import Image

# CTtinker: Custom tkinter for modern GUIs
# Docs: https://customtkinter.tomschimansky.com/documentation/windows/window
# Git: https://github.com/TomSchimansky/CustomTkinter?tab=readme-ov-file

# ~ ~ ~ ~ ~ ~ ~ ~ App setup ~ ~ ~ ~ ~ ~ ~ ~ #

assets_path = "./assets"
window_icon_path = f"{assets_path}/icos/allay.ico"

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()
app.configure(fg_color=co.strongyellow)

# Center the window
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
window_width = 735
window_height = 412
center_x = int((screen_width - window_width) / 2 + window_width*0.1)
center_y = int((screen_height - window_height) / 2)

app.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
app.resizable(False, False)
app.title("Mod Manager")

# Change the window icon
app.iconbitmap(window_icon_path)

# ~ ~ ~ ~ ~ ~ ~ ~ Content ~ ~ ~ ~ ~ ~ ~ ~ #

# Set GUI contents
gui.content(app)

app.mainloop()