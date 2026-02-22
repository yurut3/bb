import tkinter as tk
from tkinter import messagebox

class CosmicVisionGUI:
    def __init__(self, master):
        self.master = master
        master.title("Cosmic Vision GUI")

        self.label = tk.Label(master, text="Welcome to Cosmic Vision!")
        self.label.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start)
        self.start_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()

    def start(self):
        # Place logic for starting the Cosmic Vision application here
        messagebox.showinfo("Cosmic Vision", "Cosmic Vision has started!")

if __name__ == '__main__':
    root = tk.Tk()
    cosmic_vision_gui = CosmicVisionGUI(root)
    root.mainloop()
