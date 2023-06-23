import tkinter as tk
import math

class CalculatorApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('PyCalc')
        self.configure_app_window()

        self.current_operation = ''
        self.entry_text = tk.StringVar()

        self.create_widgets()

    def configure_app_window(self):
        self.geometry('500x500')
        self.resizable(False, False)

    def create_widgets(self):
        entry = tk.Entry(self, textvariable=self.entry_text, font=('Arial', 20), justify='right')
        entry.pack(fill=tk.BOTH, padx=10, pady=10)

        # Przyciski cyfr
        buttons_frame = tk.Frame(self)
        buttons_frame.pack()

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'sqrt', 'sin', 'cos', 'tan',
            'log', 'exp', 'pi',
            'C'  
        ]

        row = 0
        col = 0
        for button in buttons:
            if button == '=':
                btn = tk.Button(buttons_frame, text=button, width=5, height=2,
                                font=('Arial', 14), command=self.calculate_result)
            elif button == 'sqrt':
                btn = tk.Button(buttons_frame, text='√', width=5, height=2,
                                font=('Arial', 14), command=self.calculate_sqrt)
            elif button == 'sin':
                btn = tk.Button(buttons_frame, text='sin', width=5, height=2,
                                font=('Arial', 14), command=self.calculate_sin)
            elif button == 'cos':
                btn = tk.Button(buttons_frame, text='cos', width=5, height=2,
                                font=('Arial', 14), command=self.calculate_cos)
            elif button == 'tan':
                btn = tk.Button(buttons_frame, text='tan', width=5, height=2,
                                font=('Arial', 14), command=self.calculate_tan)
            elif button == 'log':
                btn = tk.Button(buttons_frame, text='log', width=5, height=2,
                                font=('Arial', 14), command=self.calculate_log)
            elif button == 'exp':
                btn = tk.Button(buttons_frame, text='exp', width=5, height=2,
                                font=('Arial', 14), command=self.calculate_exp)
            elif button == 'pi':
                btn = tk.Button(buttons_frame, text='π', width=5, height=2,
                                font=('Arial', 14), command=self.calculate_pi)
            elif button == 'C':
                btn = tk.Button(buttons_frame, text='C', width=5, height=2,
                                font=('Arial', 14), command=self.clear_entry)
            else:
                btn = tk.Button(buttons_frame, text=button, width=5, height=2,
                                font=('Arial', 14), command=lambda value=button: self.append_to_operation(value))

            btn.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def append_to_operation(self, value):
        self.current_operation += value
        self.entry_text.set(self.current_operation)

    def calculate_result(self):
        try:
            result = eval(self.current_operation)
            self.entry_text.set(result)
            self.current_operation = str(result)
        except:
            self.entry_text.set('Error')
            self.current_operation = ''

    def calculate_sqrt(self):
        try:
            result = math.sqrt(float(self.current_operation))
            self.entry_text.set(result)
            self.current_operation = str(result)
        except:
            self.entry_text.set('Error')
            self.current_operation = ''

    def calculate_sin(self):
        try:
            result = math.sin(float(self.current_operation))
            self.entry_text.set(result)
            self.current_operation = str(result)
        except:
            self.entry_text.set('Error')
            self.current_operation = ''

    def calculate_cos(self):
        try:
            result = math.cos(float(self.current_operation))
            self.entry_text.set(result)
            self.current_operation = str(result)
        except:
            self.entry_text.set('Error')
            self.current_operation = ''

    def calculate_tan(self):
        try:
            result = math.tan(float(self.current_operation))
            self.entry_text.set(result)
            self.current_operation = str(result)
        except:
            self.entry_text.set('Error')
            self.current_operation = ''

    def calculate_log(self):
        try:
            result = math.log(float(self.current_operation))
            self.entry_text.set(result)
            self.current_operation = str(result)
        except:
            self.entry_text.set('Error')
            self.current_operation = ''

    def calculate_exp(self):
        try:
            result = math.exp(float(self.current_operation))
            self.entry_text.set(result)
            self.current_operation = str(result)
        except:
            self.entry_text.set('Error')
            self.current_operation = ''

    def calculate_pi(self):
        self.entry_text.set(math.pi)
        self.current_operation = str(math.pi)

    def clear_entry(self):
        self.entry_text.set('')
        self.current_operation = ''

# Uruchomienie aplikacji
app = CalculatorApp()
app.mainloop()
