"""This is where the questions are made. No GUI in here, just the maths.

The screens call generate_question() and get back the question and its answer.
All the answers are whole numbers.
"""

import random
from dataclasses import dataclass


@dataclass
class Question:
    text: str
    answer: int


# --------------------------------------------------------------------------
# Easy level: basic arithmetic


def _addition() -> Question:
    a, b = random.randint(1, 50), random.randint(1, 50)
    return Question(f"{a} + {b}", a + b)


def _subtraction() -> Question:
    # Make sure `a` is the larger number so the answer is never negative.
    a, b = sorted((random.randint(1, 50), random.randint(1, 50)), reverse=True)
    return Question(f"{a} - {b}", a - b)


def _multiplication() -> Question:
    a, b = random.randint(2, 12), random.randint(2, 12)
    return Question(f"{a} × {b}", a * b)


def _division() -> Question:
    # Work backwards: pick the divisor and the answer, then multiply them to
    # get the dividend. This guarantees the division has no remainder.
    divisor, answer = random.randint(2, 12), random.randint(2, 12)
    return Question(f"{divisor * answer} ÷ {divisor}", answer)


# --------------------------------------------------------------------------
# Hard level: BODMAS (order of operations)


def _bodmas_multiply_first() -> Question:
    # a + b × c  -> the multiplication happens before the addition
    a, b, c = random.randint(1, 20), random.randint(2, 9), random.randint(2, 9)
    return Question(f"{a} + {b} × {c}", a + b * c)


def _bodmas_brackets_first() -> Question:
    # (a + b) × c  -> the brackets happen before the multiplication
    a, b, c = random.randint(1, 15), random.randint(1, 15), random.randint(2, 9)
    return Question(f"({a} + {b}) × {c}", (a + b) * c)


def _bodmas_subtract_product() -> Question:
    # a × b - c  -> c is kept below a × b so the answer stays positive
    a, b = random.randint(2, 9), random.randint(2, 9)
    c = random.randint(1, a * b - 1)
    return Question(f"{a} × {b} - {c}", a * b - c)


def _bodmas_divide_first() -> Question:
    # a + b ÷ c  -> the division happens before the addition
    a, c, quotient = random.randint(1, 20), random.randint(2, 9), random.randint(2, 9)
    return Question(f"{a} + {c * quotient} ÷ {c}", a + quotient)


def _bodmas_bracket_difference() -> Question:
    # (a - b) × c
    b = random.randint(1, 15)
    a = b + random.randint(1, 15)
    c = random.randint(2, 9)
    return Question(f"({a} - {b}) × {c}", (a - b) * c)


def _bodmas_bracket_divide() -> Question:
    # (a + b) ÷ c  -> a + b is built as a multiple of c so it divides evenly
    c, quotient = random.randint(2, 9), random.randint(2, 9)
    total = c * quotient
    a = random.randint(1, total - 1)
    return Question(f"({a} + {total - a}) ÷ {c}", quotient)


_BODMAS_TEMPLATES = [
    _bodmas_multiply_first,
    _bodmas_brackets_first,
    _bodmas_subtract_product,
    _bodmas_divide_first,
    _bodmas_bracket_difference,
    _bodmas_bracket_divide,
]


# --------------------------------------------------------------------------
# Hard level: simple algebra (solve for x)


def _algebra_add() -> Question:
    x, b = random.randint(1, 15), random.randint(1, 15)
    return Question(f"x + {b} = {x + b}", x)


def _algebra_subtract() -> Question:
    b = random.randint(1, 10)
    x = b + random.randint(1, 15)  # x > b keeps the right-hand side positive
    return Question(f"x - {b} = {x - b}", x)


def _algebra_multiply() -> Question:
    a, x = random.randint(2, 9), random.randint(1, 12)
    return Question(f"{a}x = {a * x}", x)


def _algebra_two_step_add() -> Question:
    a, x, b = random.randint(2, 9), random.randint(1, 12), random.randint(1, 15)
    return Question(f"{a}x + {b} = {a * x + b}", x)


def _algebra_two_step_subtract() -> Question:
    a, x = random.randint(2, 9), random.randint(2, 12)
    b = random.randint(1, a * x - 1)  # keeps the right-hand side positive
    return Question(f"{a}x - {b} = {a * x - b}", x)


def _algebra_brackets() -> Question:
    a, x, b = random.randint(2, 6), random.randint(1, 10), random.randint(1, 9)
    return Question(f"{a}(x + {b}) = {a * (x + b)}", x)


_ALGEBRA_TEMPLATES = [
    _algebra_add,
    _algebra_subtract,
    _algebra_multiply,
    _algebra_two_step_add,
    _algebra_two_step_subtract,
    _algebra_brackets,
]


# --------------------------------------------------------------------------
# Public entry point

def generate_question(level: str, operation: str) -> Question:
    """Return a random question for the given level and operation.

    `level` is "easy" or "hard"; `operation` is one of the names listed in
    `screens.OPERATIONS` (e.g. "Addition", "BODMAS", "Algebra").
    """
    generators = {
        ("easy", "Addition"): [_addition],
        ("easy", "Subtraction"): [_subtraction],
        ("easy", "Multiplication"): [_multiplication],
        ("easy", "Division"): [_division],
        ("hard", "BODMAS"): _BODMAS_TEMPLATES,
        ("hard", "Algebra"): _ALGEBRA_TEMPLATES,
    }
    return random.choice(generators[(level, operation)])()
