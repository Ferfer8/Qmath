import tkinter as tk

from theme import BG
from screens import MenuScreen, OperationScreen


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x700")
        self.title("Qmath")
        self.configure(background=BG)

        self.current_screen = None
        self.show_menu()          

    def switch_to(self, screen):
        """Remove the current screen and show a new one."""
        if self.current_screen is not None:
            self.current_screen.destroy()
        self.current_screen = screen
        self.current_screen.pack(fill="both", expand=True)

    def show_menu(self):
        self.switch_to(MenuScreen(self))
 
    def show_operations(self, level):
        self.switch_to(OperationScreen(self, level))



if __name__ == "__main__":
    App().mainloop()