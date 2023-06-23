import tkinter as tk
import time

class DigitalClockApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Zegar")
        self.master.geometry("300x100")

        self.label_time = tk.Label(master, text="", font=("Arial", 36))
        self.label_time.pack(pady=20)

        self.update_time()

    def update_time(self):
        current_time = time.strftime("%H:%M:%S")
        self.label_time.config(text=current_time)
        self.master.after(1000, self.update_time)

def main():
    root = tk.Tk()
    app = DigitalClockApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
