import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract

class TextExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Extractor")

        self.image_path = None

        # Create widgets
        self.label = tk.Label(root, text="Pilih Gambar:")
        self.label.pack(pady=10)

        self.choose_button = tk.Button(root, text="Pilih", command=self.choose_image)
        self.choose_button.pack(pady=5)

        self.extract_button = tk.Button(root, text="Ekstrak Teks", command=self.extract_text)
        self.extract_button.pack(pady=5)

        self.text_display = tk.Text(root, wrap=tk.WORD, width=40, height=10)
        self.text_display.pack(pady=10)

    def choose_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
        if file_path:
            self.image_path = file_path
            self.display_image(file_path)

    def display_image(self, file_path):
        image = Image.open(file_path)
        image.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(image)

        if hasattr(self, 'image_label'):
            self.image_label.destroy()

        self.image_label = tk.Label(self.root, image=photo)
        self.image_label.image = photo
        self.image_label.pack(pady=10)

    def extract_text(self):
        if self.image_path:
            image = Image.open(self.image_path)
            text = pytesseract.image_to_string(image)
            self.text_display.delete(1.0, tk.END)
            self.text_display.insert(tk.END, text)
        else:
            self.text_display.delete(1.0, tk.END)
            self.text_display.insert(tk.END, "Pilih gambar terlebih dahulu.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextExtractorApp(root)
    root.mainloop()
