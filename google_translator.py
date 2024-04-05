# reguirements are to install the googletrans library
# pip install googletrans==4.0.0-rc1

from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

root = Tk()
root.title("Google Translator Application")
root.geometry("1080x400")
root.resizable(False, False)
root.configure(background="white")

t1 = Translator()


def label_change():
    c1 = combo1.get()
    c2 = combo2.get()
    label1.configure(text=c1)
    label2.configure(text=c2)
    root.after(1000, label_change)


def translate_now():
    text_ = text1.get(1.0, END)
    trans_text = t1.translate(text_, src=combo1.get(), dest=combo2.get()).text
    text2.delete(1.0, END)
    text2.insert(END, trans_text)


# icon settings
image_icon = PhotoImage(file='google.png')
root.iconphoto(False, image_icon)

# arrow settings
arrow_image = PhotoImage(file='arrow.png')
image_label = Label(root, image=arrow_image, width=150)
image_label.place(x=460, y=50)

# languages download
languageV = list(LANGUAGES.values())

# first combobox
combo1 = ttk.Combobox(root, values=languageV, font="roboto 14", state="r")
combo1.place(x=110, y=20)
combo1.set("SELECT LANGUAGE")

label1 = Label(root, text="english", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

# second combobox
combo2 = ttk.Combobox(root, values=languageV, font="roboto 14", state="r")
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUAGE")

label2 = Label(root, text="english", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

# first frame
f1 = Frame(root, bg='black', bd=5)
f1.place(x=10, y=118, width=440, height=210)

text1 = Text(f1, font='Robote 20', bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, width=430, height=200)

scrollbar1 = Scrollbar(f1)
scrollbar1.pack(side='right', fill='y')
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# second frame
f2 = Frame(root, bg='black', bd=5)
f2.place(x=620, y=118, width=440, height=210)

text2 = Text(f2, font='Robote 20', bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f2)
scrollbar2.pack(side='right', fill='y')
scrollbar2.configure(command=text1.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# translate button
translate = Button(root, text='Translate', font=("roboto", 15), activebackground='white', cursor='hand2', bd=1, width=10,
                 height=2, bg='black', fg='white', command=translate_now)
translate.place(x=476, y=250)
label_change()
root.mainloop()

