from ast import Str
import random
import tkinter as tk
import pyperclip    

class Events:    

    password = " "

    def makepassword(self):
        ucase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lcase = "abcdefghijklmnopqrstuvwxyz"
        numberss = "1234567890" 
        scharacter = "!#$%&'()*+,-./"

        chars = ucase + lcase + numberss + scharacter
        length = int(ent_lenght.get())
        passs = random.sample(chars, length)
        pasy = ''.join(passs)
        lbl_value["text"] = f"{pasy}"
        print(pasy)
        pyperclip.copy(pasy)
        pyperclip.paste()
        self.password = Str(pasy)
        print(self.password)
    
    def get_password(self):
        return self.password

def copypassword():
    pyperclip.copy(event.get_password)
    pyperclip.paste()




event = Events()

window = tk.Tk()
window.title("Password Generator")

window.rowconfigure([0, 1, 2, 3], minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

btn_generator = tk.Button(master=window, text="Generate", command=event.makepassword)
btn_generator.grid(row=0, column=0, sticky="nsew", columnspan=3)

lbl_value = tk.Label(master=window, text=" ")
lbl_value.grid(row=2, column=1)

ent_lenght = tk.Entry(master=window, width=10)
ent_lenght.grid(row=1, column=0, columnspan=3)

btn_copy = tk.Button(master=window, text="Copy", command=copypassword)
btn_copy.grid(row=3, column=0, sticky="nsew", columnspan=3)

window.mainloop()

