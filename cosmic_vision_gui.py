import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class CosmicVisionGUI:
    def __init__(self, master):
        self.master = master
        master.title("Cosmic Vision")
        master.geometry("800x600")
        master.config(bg="#2E2E2E")

        self.label = tk.Label(master, text="Welcome to Cosmic Vision", bg="#2E2E2E", fg="#FFFFFF", font=("Arial", 24))
        self.label.pack(pady=20)

        self.img_button = tk.Button(master, text="Load Image", command=self.load_image, bg="#4CAF50", fg="#FFFFFF")
        self.img_button.pack(pady=10)

        self.canvas = tk.Canvas(master, width=500, height=400, bg="#FFFFFF")
        self.canvas.pack(pady=20)

    def load_image(self):
        file_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.display_image(file_path)

    def display_image(self, path):
        img = Image.open(path)
        img = img.resize((500, 400), Image.ANTIALIAS)
        self.tk_image = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

if __name__ == "__main__":
    root = tk.Tk()
    gui = CosmicVisionGUI(root)
    root.mainloop()