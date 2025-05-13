import tkinter as tk

class SimpleCalculator:
    def __init__(self, root):
        self.expression = ""
        self.input_text = tk.StringVar()

        root.title("Simple Calculator")
        root.geometry("300x400")
        root.resizable(False, False)

        self.create_widgets(root)

    def create_widgets(self, root):
        input_frame = tk.Frame(root, bd=2, relief=tk.RIDGE)
        input_frame.pack(side=tk.TOP, fill=tk.BOTH)

        input_field = tk.Entry(input_frame, textvariable=self.input_text, font=('arial', 18, 'bold'), bd=5, relief=tk.FLAT, justify='right')
        input_field.pack(ipady=10, fill=tk.BOTH)

        btns_frame = tk.Frame(root)
        btns_frame.pack()

        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+')
        ]

        for row in buttons:
            row_frame = tk.Frame(btns_frame)
            row_frame.pack(expand=True, fill='both')
            for btn in row:
                b = tk.Button(row_frame, text=btn, font=('arial', 18), relief=tk.GROOVE, border=0,
                              command=lambda x=btn: self.on_click(x))
                b.pack(side=tk.LEFT, expand=True, fill='both')

        clear_btn = tk.Button(root, text='C', font=('arial', 18), relief=tk.GROOVE, border=0,
                              command=self.clear)
        clear_btn.pack(side=tk.BOTTOM, expand=True, fill='both')

    def on_click(self, char):
        if char == "=":
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except Exception:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_text.set("")


if __name__ == "__main__":
    root = tk.Tk()
    calc = SimpleCalculator(root)
    root.mainloop()
