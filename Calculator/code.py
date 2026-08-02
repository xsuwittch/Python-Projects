import tkinter as tk

def calculate(expression: str) -> str:
    allowed_chars = set("0123456789+-*/(). ")
    if not expression:
        return "Error"
    if not all(c in allowed_chars for c in expression):
        return "Error"
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except ZeroDivisionError:
        return "Error: Div by 0"
    except Exception:
        return "Error"

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(False, False)

        self.expression = ""
        self.display_var = tk.StringVar(value="0")

        display = tk.Entry(
            root,
            textvariable=self.display_var,
            font=("Consolas", 24),
            justify="right",
            bd=10,
            relief="ridge",
        )
        display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        buttons = [
            ("C", 1, 0), ("(", 1, 1), (")", 1, 2), ("/", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("⌫", 5, 2), ("=", 5, 3),
        ]

        for (text, row, col) in buttons:
            btn = tk.Button(
                root,
                text=text,
                font=("Consolas", 16),
                width=4,
                height=2,
                command=lambda t=text: self.on_button(t),
            )
            btn.grid(row=row, column=col, padx=3, pady=3)

    def on_button(self, char: str):
        if char == "C":
            self.expression = ""
        elif char == "⌫":
            self.expression = self.expression[:-1]
        elif char == "=":
            self.expression = calculate(self.expression)
        else:
            self.expression += char

        self.display_var.set(self.expression if self.expression else "0")

def main():
    root = tk.Tk()
    Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()