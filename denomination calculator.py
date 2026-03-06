from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()
root.title("DENOMINATION CALCULATOR")
root.configure(bg="light blue")
root.geometry("650x400")
upload = Image.open("denomination calc.jpeg")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg="light blue")
label.place(x=180, y=20)
label1 = Label(
    root,
    text="HEY U WELCOME TO THE HOOD LIL BRUH HERE WE DO DENOMINATION CALCULATIONS NEWBIE :3",
    bg="light blue"
)
label1.place(relx=0.5, y=340, anchor=CENTER)
def msg():
    MsgBox = messagebox.showinfo(
        "YOU'VE GOT MAIL",
        "IT SAYS DO YA WANT TO CALCULATE UR DENOMINATION (ME NO SPEAK ENGLISH WELL)"
    )
    if MsgBox == "ok":
        topwin()
button1 = Button(
    root,
    text="START BOY :3",
    command=msg,
    bg="brown",
    fg="white"
)
button1.place(x=260, y=360)
def topwin():
    top = Toplevel()
    top.title("DENOMINATIONS CALCULATOR")
    top.configure(bg="light grey")
    top.geometry("600x300+50+50")
    label = Label(top, text="ENTER TOTAL AMOUNT", bg="light grey")
    entry = Entry(top)
    lbl = Label(
        top,
        text="HERE ARE THE NUMBER OF NOTES FOR EACH DENOMINATION",
        bg="light grey"
    )
    l1 = Label(top, text="2000", bg="light grey")
    l2 = Label(top, text="500", bg="light grey")
    l3 = Label(top, text="100", bg="light grey")
    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    def calculator():
        try:
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("ERROR", "PLEASE ENTER A VALID NUMBER.")
    btn = Button(
        top,
        text = "CALCULATE",
        bg="brown",
        fg="white",
        command=calculator
    )
    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140, y=170)
    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)
    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)
    top.mainloop()
root.mainloop()