from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W, font

class FrmDosen:
    def __init__(self, parent, title):
        self.parent = parent
        # self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.on_keluar)
        self.atur_komponen()

    def atur_komponen(self):
        main_frame = Frame(self.parent, bd=10)
        main_frame.pack(fill=BOTH, expand=YES)

        label_dosen = Label(main_frame, text="Dosen Content", font=font.Font(size=40))
        label_dosen.pack(padx=20, pady=20)

    def on_keluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    def update_main_window(result):
        print(result)

    root = Tk()
    aplikasi = FrmDosen(root, "Windows Dosen")
    root.mainloop()
