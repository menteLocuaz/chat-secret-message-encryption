from tkinter import *
from tkinter import messagebox
import base64


# funcion de decifrado
def decrypt():
    password = code.get()
    if password == "12345":
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00db56")

        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("ascii")

        Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#00db56").place(
            x=10, y=0
        )
        text2 = Text(
            screen2, font=("Roboto 10"), bg="white", relief=GROOVE, wrap=WORD, bd=0
        )
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypt)
    elif password == "":
        messagebox.showerror("encrytion", "Input password")
    elif password != "12345":
        messagebox.showerror("encryption", "Invalid password")


def encrypt():
    password = code.get()
    if password == "12345":
        screen3 = Toplevel(screen)
        screen3.title("encryption")
        screen3.geometry("400x200")
        screen3.configure(bg="#ed3833")

        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen3, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(
            x=10, y=0
        )
        text2 = Text(
            screen3, font=("Roboto 10"), bg="white", relief=GROOVE, wrap=WORD, bd=0
        )
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypt)
    elif password == "":
        messagebox.showerror("encrytion", "Input password")
    elif password != "12345":
        messagebox.showerror("encryption", "Invalid password")


# comenzando en definir la dimision del la app
def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("375x398")
    # poner los iconos
    image_icon = PhotoImage(file="image/keys.png")
    screen.iconphoto(False, image_icon)
    screen.title("Chat App")
    # cuadro de texto 1
    Label(
        text="Enter text for encryption and decryption", fg="black", font=("calbri", 13)
    ).place(x=10, y=10)
    text1 = Text(font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=3555, height=100)
    # cuadro de rexto 2 el de cifrado
    Label(
        text="Enter secret key for encryption and decryption",
        fg="black",
        font=("calibri", 13),
    ).place(x=10, y=170)
    # mostra palabra en *
    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(
        x=10, y=200
    )
    # fruncion para resetear
    def reset():
        code.set("")
        text1.delete(1.0, END)

    # bonotnes descritivos
    Button(
        text="ENCRYPT",
        height="2",
        width=23,
        bg="#ed3833",
        fg="white",
        bd=0,
        command=encrypt,
    ).place(x=10, y=250)
    Button(
        text="DECRYPT",
        height="2",
        width=23,
        bg="#00bd56",
        fg="white",
        bd=0,
        command=decrypt,
    ).place(x=200, y=250)
    Button(
        text="RESET", height=2, width=50, bg="#1089ff", fg="white", bd=0, command=reset
    ).place(x=10, y=300)
    screen.mainloop()


main_screen()
