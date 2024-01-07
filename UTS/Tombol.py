from tkinter import Tk, Button, PhotoImage

def on_button_click():
    print("HEHEHEH")

# Buat instance dari Tkinter
root = Tk()
root.title("Tombol dengan Gambar")

# Load gambar untuk tombol
image_path = 'C:/Users/nazar/PBO/Pertemuan_3/Media/play.png'
button_image = PhotoImage(file=image_path)

# Buat tombol dengan gambar
button = Button(root, image=button_image, command=on_button_click)
button.pack()

# Jalankan loop utama
root.mainloop()
