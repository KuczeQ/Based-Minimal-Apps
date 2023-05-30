import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, root):
        self.root = root

        self.color_button = tk.Button(self.root, text="Wybierz kolor", command=self.choose_color)
        self.color_button.pack()

        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()

        self.canvas.bind("<B1-Motion>", self.draw)

    def draw(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x-2, y-2, x+2, y+2, fill=self.color_button["bg"])

    def choose_color(self):
        color = colorchooser.askcolor()[1]  
        self.color_button.configure(bg=color)

root = tk.Tk()
root.geometry("800x600")  
root.resizable(False, False)  
app = PaintApp(root)
root.mainloop()
