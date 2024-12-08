import customtkinter
import styles
from ui.mod_card import ModCard
from model.mod import Mod
from model.model import ModManager

class Mods (customtkinter.CTkScrollableFrame):
    
    def __init__(self, master):
       
        self.colors = styles.Colors() 
        self.fonts = styles.Fonts()
        self.modManager = ModManager()
        
        # prepare frame args
        kwargs = {
            "corner_radius": 20,
            "bg_color": self.colors.cocoa,
            "fg_color": self.colors.cream,
            "border_color": None,
            "border_width": 0,
            "scrollbar_fg_color": self.colors.cream,
            "scrollbar_button_color": self.colors.cocoa,
            "scrollbar_button_hover_color": self.colors.black,
            "orientation": "vertical"
        }
        
        # call super with updated kwargs
        super().__init__(master, **kwargs)
        
        # add version selector
        self.set_version_selector()
        
        # Refresh mod list
        self.refresh()
        
    def set_version_selector(self):
        self.version_selector = customtkinter.CTkComboBox(
            self,
            values=self.modManager.find_all_versions(),
            font=self.fonts.modTitle,
            bg_color=self.colors.cream,
            fg_color=self.colors.cocoa,
            border_width=0,
            corner_radius=10,
            width=10,
            justify="center",
            text_color=self.colors.cream,
            command=self.on_version_change
        )
        self.version_selector.pack(fill="x", padx=10, pady=10)
        
    def on_version_change(self, choice):
        # version selected looks like: "forge 1.21.0", split it
        print(f"Version selected: {choice}")
        engine = choice.split()[0]
        version = choice.split()[1]
        self.refresh(engine, version)
            
    def refresh(self, engine: str = None, version: str = None):
        # refresh modManager
        self.modManager.refresh(engine, version)
        # Destroy all widgets except version selector
        for widget in self.winfo_children():
            if widget != self.version_selector:
                widget.destroy()
            
        # check if mods are ready
        if self.modManager.isready:
            self.set_mods()
        else:
            self.no_mods()
            
        # Restore version selector to top
        self.version_selector.pack(fill="x", padx=10, pady=10)
            
    def no_mods(self):
        no_mods = customtkinter.CTkLabel(
            self,
            text="No mods found",
            font=self.fonts.modTitle,
            bg_color=self.colors.transparent,
            text_color=self.colors.cocoa
        )
        no_mods.pack(fill="x", padx=10, pady=10)
            
    def set_mods(self):
        for mod in self.modManager.mods:
            self.add_item(mod)
            
    def add_item(self, mod: Mod):
        mod_card = ModCard(self, mod)
        mod_card.pack(fill="x", padx=10, pady=10)