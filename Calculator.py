from tkinter import *

root = Tk()
root.title("Simple Calculator")

number_box = Entry(root, width=35, borderwidth=3)
number_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_click(number):
    current = number_box.get()
    number_box.delete(0, END)
    number_box.insert(0, str(current) + str(number))


def button_clear():
    number_box.delete(0, END)


def button_del():
    number_box.delete((len(number_box.get()) - 1), END)


def button_add():
    global first_num
    global mathematics
    mathematics = "add"
    first_num = number_box.get()
    number_box.delete(0, END)


def button_div():
    global first_num
    global mathematics
    mathematics = "div"
    first_num = number_box.get()
    number_box.delete(0, END)


def button_min():
    global first_num
    global mathematics
    mathematics = "min"
    first_num = number_box.get()
    number_box.delete(0, END)


def button_mlp():
    global first_num
    global mathematics
    mathematics = "mlp"
    first_num = number_box.get()
    number_box.delete(0, END)


def button_raise():
    global first_num
    global mathematics
    mathematics = "raise"
    first_num = number_box.get()
    number_box.delete(0, END)

def button_equal():
    second_num = number_box.get()
    number_box.delete(0, END)
    try:
        if mathematics == "add":
            result = int(first_num) + int(second_num)
            number_box.insert(0, result)

        elif mathematics == "min":
            result = int(first_num) - int(second_num)
            number_box.insert(0, result)

        elif mathematics == "mlp":
            result = int(first_num) * int(second_num)
            number_box.insert(0, result)

        elif mathematics == "div":
            result = int(first_num) / int(second_num)
            number_box.insert(0, result)

        elif mathematics == "raise":
            result = int(first_num) ** int(second_num)
            number_box.insert(0, result)
    except NameError:
        pass
    except ZeroDivisionError:
        number_box.insert(0, "ERR: Division by zero")


button1 = Button(root, text="1", padx=22, pady=7, command=lambda: button_click(1))
button2 = Button(root, text="2", padx=22, pady=7, command=lambda: button_click(2))
button3 = Button(root, text="3", padx=22, pady=7, command=lambda: button_click(3))
button4 = Button(root, text="4", padx=22, pady=7, command=lambda: button_click(4))
button5 = Button(root, text="5", padx=22, pady=7, command=lambda: button_click(5))
button6 = Button(root, text="6", padx=22, pady=7, command=lambda: button_click(6))
button7 = Button(root, text="7", padx=22, pady=7, command=lambda: button_click(7))
button8 = Button(root, text="8", padx=22, pady=7, command=lambda: button_click(8))
button9 = Button(root, text="9", padx=22, pady=7, command=lambda: button_click(9))
button0 = Button(root, text="0", padx=22, pady=7, command=lambda: button_click(0))
buttonclr = Button(root, text="Clear", padx=10, pady=28, command=button_clear)
buttondel = Button(root, text="Del", padx=15, pady=7, command=button_del)
buttonadd = Button(root, text="+", padx=21, pady=7, command=button_add)
buttonmin = Button(root, text="-", padx=22, pady=7, command=button_min)
buttonmlp = Button(root, text="*", padx=22, pady=7, command=button_mlp)
buttondiv = Button(root, text="/", padx=22, pady=7, command=button_div)
buttonraise = Button(root, text="^", padx=21, pady=7, command=button_raise)
buttoneq = Button(root, text="=", padx=19, pady=29, command=button_equal)

# Grid the buttons
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
button0.grid(row=4, column=1)
buttonclr.grid(row=1, column=3, rowspan=2)
buttondel.grid(row=3, column=3)
buttoneq.grid(row=4, column=3, rowspan=2)
buttonadd.grid(row=4, column=0)
buttonmin.grid(row=5, column=2)
buttonmlp.grid(row=4, column=2)
buttondiv.grid(row=5, column=0)
buttonraise.grid(row=5, column=1)

root.mainloop()
