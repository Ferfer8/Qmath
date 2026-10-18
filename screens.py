import tkinter as tk
import customtkinter as ctk

from theme import BG, CARD, DARK, TEXT, SUBTEXT, EASY, EASY_HOVER, HARD, HARD_HOVER, FONT



class MenuScreen(tk.Frame):
    def __init__(self, app):
        super().__init__(app, background=BG)
        self.app = app

        card = ctk.CTkFrame(self, fg_color=CARD, corner_radius=25, bg_color=BG)
        card.place(relx=0.5, rely=0.45, anchor="center")

        heading = ctk.CTkLabel(card, text="Welcome to Qmath!",
                               font=(FONT, 50, "bold"), text_color=TEXT,
                               fg_color=CARD, corner_radius=25)
        heading.grid(row=0, column=0, columnspan=2, pady=(10, 60))

        subheading = tk.Label(card, text="Pick your level",
                              font=(FONT, 30, "bold"), fg=SUBTEXT, bg=CARD)
        subheading.grid(row=1, column=0, columnspan=2, pady=(30, 40))

        easy_btn = ctk.CTkButton(card, text="Easy", font=(FONT, 30, "bold"),
                                 width=200, height=100, corner_radius=30,
                                 text_color=TEXT, fg_color=EASY, hover_color=EASY_HOVER,
                                 cursor="hand2")
                                 
        easy_btn.grid(row=2, column=0, padx=60, pady=60)

        hard_btn = ctk.CTkButton(card, text="Hard", font=(FONT, 30, "bold"),
                                 width=200, height=100, corner_radius=30,
                                 text_color=TEXT, fg_color=HARD, hover_color=HARD_HOVER,
                                 cursor="hand2")
                               
        hard_btn.grid(row=2, column=1, padx=60, pady=60)



