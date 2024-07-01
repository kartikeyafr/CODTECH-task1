import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.configure(bg="white")
        
        self.expression = ""
        self.text_input = tk.StringVar()

        self.entry = tk.Entry(root, textvariable=self.text_input, font=('Helvetica', 18), bd=5, relief=tk.FLAT, width=14, justify='right', bg="white")
        self.entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

        self.clear_button = tk.Button(self.root, text='C', font=('Helvetica', 18), command=self.clear, bg="Coral2", relief=tk.FLAT)
        self.clear_button.grid(row=5, column=0, columnspan=4, sticky="nsew")

    def create_button(self, text, row, col):
        button = tk.Button(self.root, text=text, font=('Helvetica', 18), command=lambda: self.on_button_click(text), bg="gray25", relief=tk.FLAT)
        button.grid(row=row, column=col, sticky="nsew", ipadx=8, ipady=8)
        self.root.grid_rowconfigure(row, weight=1)
        self.root.grid_columnconfigure(col, weight=1)

    def on_button_click(self, char):
        if char == '=':
            try:
                self.expression = str(eval(self.expression))
                self.text_input.set(self.expression)
            except:
                self.text_input.set("Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.text_input.set(self.expression)

    def clear(self):
        self.expression = ""
        self.text_input.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

