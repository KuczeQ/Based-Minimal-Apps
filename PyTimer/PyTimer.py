import time
import threading
import tkinter as tk

class StopwatchApp:
    def __init__(self, master):
        self.master = master
        self.master.title("PyTimer")
        self.master.geometry("300x200")

        self.start_time = None
        self.total_elapsed_time = 0

        self.label_time = tk.Label(master, text="0.0 sekundy", font=("Arial", 24))
        self.label_time.pack(pady=20)

        self.button_start = tk.Button(master, text="Start", command=self.start_stopwatch)
        self.button_start.pack()

        self.button_stop = tk.Button(master, text="Stop", state=tk.DISABLED, command=self.stop_stopwatch)
        self.button_stop.pack()

        self.button_quit = tk.Button(master, text="Zakończ", command=self.quit_app)
        self.button_quit.pack(pady=20)

    def start_stopwatch(self):
        self.start_time = time.time()
        self.button_start.config(state=tk.DISABLED)
        self.button_stop.config(state=tk.NORMAL)
        self.update_time()

    def stop_stopwatch(self):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        self.total_elapsed_time += elapsed_time
        self.start_time = None
        self.button_start.config(state=tk.NORMAL)
        self.button_stop.config(state=tk.DISABLED)

    def update_time(self):
        if self.start_time is not None:
            elapsed_time = self.total_elapsed_time + (time.time() - self.start_time)
            self.label_time.config(text=f"{elapsed_time:.1f} sekundy")
        self.master.after(100, self.update_time)

    def quit_app(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
