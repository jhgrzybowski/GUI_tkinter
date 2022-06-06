import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Projekt SI")
root.iconbitmap("./static/icon.ico")

title = tk.Label(root, text="Wykrywanie języka")
title.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

info = tk.Label(root, text="Wpisz zdanie w dowolnym języku")
info.grid(row=1, column=0)

text_input = tk.Entry(root, borderwidth=5, width=25)
text_input.grid(row=1, column=1)

def language_recognizer():
    eng_flag = ImageTk.PhotoImage(Image.open("./static/eng.png"))
    deu_flag = ImageTk.PhotoImage(Image.open("./static/deu.png"))
    esp_flag = ImageTk.PhotoImage(Image.open("./static/esp.png"))
    por_flag = ImageTk.PhotoImage(Image.open("./static/por.png"))
    default = ImageTk.PhotoImage(Image.open("./static/default.png"))
    image_list = [eng_flag, deu_flag, esp_flag, por_flag, default]
    


    if(text_input.get()=="eng"):
        lang_lab = tk.Label(root, image=image_list[0], width=300, height=200)
        lang_lab.photo=image_list[0]
    elif(text_input.get()=="deu"):
        lang_lab = tk.Label(root, image=image_list[1], width=300, height=200)
        lang_lab.photo = image_list[1]
    elif(text_input.get() == "esp"):
        lang_lab = tk.Label(root, image=image_list[2], width=300, height=200)
        lang_lab.photo = image_list[2]
    elif (text_input.get() == "por"):
        lang_lab = tk.Label(root, image=image_list[3], width=300, height=200)
        lang_lab.photo = image_list[3]
    else:
        lang_lab = tk.Label(root, image=default, width=300, height=200)
        lang_lab.photo = default

    #lang_label = tk.Label(root, text="Wykryty język to: " + text_input.get(), padx=10, pady=10)
    #lang_label.grid(row=3, column=0, columnspan=3)

    lang_lab.grid(row=3, column=0, columnspan=3)


b = tk.Button(root, text='SUBMIT', command=language_recognizer, width=50, padx=5, pady=15)
b.grid(row=2, column=0, columnspan=3)

root.mainloop()