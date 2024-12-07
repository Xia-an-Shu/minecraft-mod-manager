import customtkinter
import tkinter as tk
import styles.colors as co
import styles.fonts as fo

def content(app):
    test_frame = customtkinter.CTkFrame(
        app,
        corner_radius=20,
        bg_color="transparent",
        fg_color="white",
        border_color="white",
        border_width=0,
        background_corner_colors=(None, None, None, None)
    )
    test_frame.place(relx=0.5, rely=0.5, anchor="center")