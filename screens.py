import tkinter as tk
import customtkinter as ctk

from theme import BG, CARD, DARK, TEXT, SUBTEXT, EASY, EASY_HOVER, HARD, HARD_HOVER, FONT, EASY_OP, EASY_OP_HOVER, HARD_OP, HARD_OP_HOVER

OPERATIONS = {
    "easy": ["Addition", "Subtraction", "Multiplication", "Division"],
    "hard": ["BODMAS", "Algebra"],
}


class MenuScreen(tk.Frame):
    def __init__(self, app):
        super().__init__(app, background=BG)
        self.app = app

        card = ctk.CTkFrame(self, fg_color=CARD, corner_radius=25, bg_color=BG)
        card.place(relx=0.5, rely=0.45, anchor="center")

        menu_heading = ctk.CTkLabel(card, text="Welcome to Qmath!",
                               font=(FONT, 50, "bold"), text_color=TEXT,
                               fg_color=CARD, corner_radius=25)
        menu_heading.grid(row=0, column=0, columnspan=2, pady=(10, 60))

        menu_subheading = tk.Label(card, text="Pick your level",
                              font=(FONT, 30, "bold"), fg=SUBTEXT, bg=CARD)
        menu_subheading.grid(row=1, column=0, columnspan=2, pady=(30, 40))

        easy_btn = ctk.CTkButton(card, text="Easy", font=(FONT, 30, "bold"),
                                 width=200, height=100, corner_radius=30,
                                 text_color=TEXT, fg_color=EASY, hover_color=EASY_HOVER,
                                 cursor="hand2", command=lambda: self.app.show_operations("easy"))

        easy_btn.grid(row=2, column=0, padx=60, pady=60)

        hard_btn = ctk.CTkButton(card, text="Hard", font=(FONT, 30, "bold"),
                                 width=200, height=100, corner_radius=30,
                                 text_color=TEXT, fg_color=HARD, hover_color=HARD_HOVER,
                                 cursor="hand2", command=lambda: self.app.show_operations("hard"))

        hard_btn.grid(row=2, column=1, padx=60, pady=60)


class OperationScreen(tk.Frame):
    def __init__(self, app, level):
        super().__init__(app, background=BG)
        self.app = app
        self.level = level

        if level == "easy":
            colour, hover = EASY_OP, EASY_OP_HOVER
        else:
            colour, hover = HARD_OP, HARD_OP_HOVER


        card = ctk.CTkFrame(self, fg_color=CARD, corner_radius=25, bg_color=BG)
        card.place(relx=0.5, rely=0.45, anchor="center")

        title = ctk.CTkLabel(card, text=f"{level.title()} level",
                                       font=(FONT, 50, "bold"), text_color=TEXT,
                                       fg_color=CARD, corner_radius=25)
        title.grid(row=0, column=0, columnspan=2, pady=(10, 60))

        subtitle = tk.Label(card, text="Choose an operation:",
                              font=(FONT, 30, "bold"), fg=SUBTEXT, bg=CARD)
        subtitle.grid(row=1, column=0, columnspan=2, pady=(30, 40))

        operations = OPERATIONS[level]
        for i, operation in enumerate(operations):
            btn = ctk.CTkButton(card, text=operation, font=(FONT, 22, "bold"),
                                width=260, height=70, corner_radius=25,
                                text_color=TEXT, fg_color=colour, hover_color=hover,
                                cursor="hand2")
            btn.grid(row=2 + i // 2, column=i % 2, padx=20, pady=15)