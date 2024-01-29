import customtkinter as ctk
from tkinter import *

window = ctk.CTk()

class MainFrame():
    def __init__(self):
        self.window = window
        self.theme()
        self.main_window_config()
        self.main_window_screen()
        window.mainloop()

    def theme(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def main_window_config(self):
        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()
        self.window.geometry(f"{width}x{height}+0+0")

        self.window.title("Automated Trading System")
        self.window.iconbitmap("../assets/icon.ico")

    def main_window_screen(self):
        pass

if __name__ == "__main__":
    MainFrame()