# All the screens: the menu, the operations page and the quiz pages for easy and hard.

import tkinter as tk
import customtkinter as ctk

from questions import generate_question
from theme import (BG, CARD, DARK, DARK_HOVER, TEXT, SUBTEXT, CORRECT, WRONG,
                   EASY, EASY_HOVER, HARD, HARD_HOVER, FONT,
                   EASY_OP, EASY_OP_HOVER, HARD_OP, HARD_OP_HOVER)

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
                                cursor="hand2",
                                command=lambda op=operation: self.app.show_quiz(level, op))
            btn.grid(row=2 + i // 2, column=i % 2, padx=20, pady=15)

        back_btn = ctk.CTkButton(card, text="Back", font=(FONT, 20, "bold"),
                                 width=140, height=50, corner_radius=20,
                                 text_color=TEXT, fg_color=DARK, hover_color=DARK_HOVER,
                                 cursor="hand2", command=self.app.show_menu)
        back_btn.grid(row=4, column=0, columnspan=2, pady=(30, 20))


class QuizScreen(tk.Frame):
    """Base page for answering questions.

    Shows one question at a time, checks the typed answer and keeps a score.
    Subclasses only choose the level and its colours.
    """

    level = ""
    colour = ""
    hover = ""

    def __init__(self, app, operation):
        super().__init__(app, background=BG)
        self.app = app
        self.operation = operation
        self.question = None
        self.answered = False      # True once the current question is checked
        self.correct_count = 0
        self.total_count = 0

        card = ctk.CTkFrame(self, fg_color=CARD, corner_radius=25, bg_color=BG)
        card.place(relx=0.5, rely=0.45, anchor="center")

        title = ctk.CTkLabel(card, text=f"{self.level.title()}: {operation}",
                             font=(FONT, 34, "bold"), text_color=TEXT,
                             fg_color=CARD)
        title.grid(row=0, column=0, columnspan=2, padx=40, pady=(20, 10))

        self.score_label = tk.Label(card, font=(FONT, 20, "bold"),
                                    fg=SUBTEXT, bg=CARD)
        self.score_label.grid(row=1, column=0, columnspan=2, pady=(0, 20))

        self.question_label = tk.Label(card, font=(FONT, 44, "bold"),
                                       fg=TEXT, bg=CARD)
        self.question_label.grid(row=2, column=0, columnspan=2, padx=40, pady=20)

        self.answer_entry = ctk.CTkEntry(card, font=(FONT, 30, "bold"),
                                         width=220, height=60, corner_radius=20,
                                         justify="center", text_color=TEXT,
                                         fg_color=DARK, border_color=self.colour,
                                         placeholder_text="answer")
        self.answer_entry.grid(row=3, column=0, columnspan=2, pady=10)

        self.feedback_label = tk.Label(card, text="", font=(FONT, 22, "bold"),
                                       fg=TEXT, bg=CARD, height=2)
        self.feedback_label.grid(row=4, column=0, columnspan=2, pady=10)

        # One button doubles as "Submit" and "Next" depending on state.
        self.action_btn = ctk.CTkButton(card, text="Submit", font=(FONT, 22, "bold"),
                                        width=180, height=60, corner_radius=25,
                                        text_color=TEXT, fg_color=self.colour,
                                        hover_color=self.hover, cursor="hand2",
                                        command=self.on_action)
        self.action_btn.grid(row=5, column=1, padx=20, pady=(10, 25))

        back_btn = ctk.CTkButton(card, text="Back", font=(FONT, 22, "bold"),
                                 width=140, height=60, corner_radius=25,
                                 text_color=TEXT, fg_color=DARK, hover_color=DARK_HOVER,
                                 cursor="hand2",
                                 command=lambda: self.app.show_operations(self.level))
        back_btn.grid(row=5, column=0, padx=20, pady=(10, 25))

        # Pressing Enter does the same as clicking the action button.
        self.answer_entry.bind("<Return>", lambda event: self.on_action())

        self.next_question()

    def next_question(self):
        """Load a fresh question and reset the answer box."""
        self.question = generate_question(self.level, self.operation)
        self.answered = False
        self.question_label.config(text=f"{self.question.text} = ?"
                                   if self.level == "easy" else self.question.text)
        self.answer_entry.configure(state="normal")
        self.answer_entry.delete(0, "end")
        self.feedback_label.config(text="")
        self.action_btn.configure(text="Submit")
        self.update_score()
        self.answer_entry.focus_set()

    def on_action(self):
        """Submit the answer, or move on if it has already been checked."""
        if self.answered:
            self.next_question()
        else:
            self.check_answer()

    def check_answer(self):
        """Compare the typed answer with the correct one and show feedback."""
        raw = self.answer_entry.get().strip().lower().replace(" ", "")
        if raw.startswith("x="):          # accept "x=4" as well as "4"
            raw = raw[2:]

        try:
            value = int(raw)
        except ValueError:
            self.feedback_label.config(text="Please enter a whole number.", fg=WRONG)
            return

        self.answered = True
        self.total_count += 1
        if value == self.question.answer:
            self.correct_count += 1
            self.feedback_label.config(text="Correct!", fg=CORRECT)
        else:
            self.feedback_label.config(
                text=f"Wrong. The answer was {self.question.answer}.", fg=WRONG)

        self.answer_entry.configure(state="disabled")
        self.action_btn.configure(text="Next")
        self.update_score()

    def update_score(self):
        self.score_label.config(text=f"Score: {self.correct_count}/{self.total_count}")


class EasyQuizScreen(QuizScreen):
    """Easy level: basic arithmetic questions."""
    level = "easy"
    colour, hover = EASY_OP, EASY_OP_HOVER


class HardQuizScreen(QuizScreen):
    """Hard level: BODMAS and algebra questions."""
    level = "hard"
    colour, hover = HARD_OP, HARD_OP_HOVER
