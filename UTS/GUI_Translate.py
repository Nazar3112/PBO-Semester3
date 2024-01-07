from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W, OptionMenu, StringVar
from googletrans import Translator
from PIL import Image, ImageTk

class FrmTranslator:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("500x250")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen() 
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        # pasang Label
        Label(mainFrame, text='Masukkan teks:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Hasil Terjemahan:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Pilih Bahasa:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        
        # pasang textbox
        self.txtSumber = Entry(mainFrame, width=50) 
        self.txtSumber.grid(row=0, column=1, padx=5, pady=5)

        self.txtHasil = Entry(mainFrame, width=50) 
        self.txtHasil.grid(row=3, column=1, padx=5, pady=5)

        # Pasang OptionMenu untuk memilih bahasa
        bahasa_options = ["id", "en", "ru", "sv"]  # Kode bahasa: Indonesia, Inggris, Rusia, Swedia
        self.selected_bahasa = StringVar()
        self.selected_bahasa.set(bahasa_options[0])  # Default: Indonesia

        dropdown_bahasa = OptionMenu(mainFrame, self.selected_bahasa, *bahasa_options)
        dropdown_bahasa.grid(row=1, column=1, padx=5, pady=5)

        # Pasang Button dengan gambar
        trans_icon_path = 'C:/Users/nazar/PBO/UTS/Media/transicon.png'
        trans_icon_image = Image.open(trans_icon_path)
        trans_icon_image = ImageTk.PhotoImage(trans_icon_image)

        self.btnTranslate = Button(mainFrame, image=trans_icon_image, command=self.onTranslate)
        self.btnTranslate.image = trans_icon_image  # Referensi agar gambar tidak dihapus oleh garbage collector
        self.btnTranslate.grid(row=2, column=1, padx=5, pady=5) 

    def onTranslate(self):
        # membuat instance object
        penterjemah = Translator()

        # menterjemahkan
        hasil = penterjemah.translate(self.txtSumber.get(), src='auto', dest=self.selected_bahasa.get()) 
       
        # menampilkan hasil terjemahan
        self.txtHasil.delete(0, END)
        self.txtHasil.insert(END, hasil.text)

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmTranslator(root, "Program Translator")
    root.mainloop()
