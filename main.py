import tkinter
import math_ivs
import re
root = tkinter.Tk()
root.title("Calc")
canvas = tkinter.Canvas(height=500, width=400, bg= "darkgrey")
canvas.pack()
logo = tkinter.PhotoImage(file="logo.png")
root.iconphoto(True, logo)

display = tkinter.StringVar()

def press(value):
    display.set(display.get() + str(value))

def clear():
    display.set("")

def calculate():
    try:
        expression = display.get()
        expression = expression.replace("×", "*").replace("^", "**")
        expression = expression.replace("÷", "/")
        expression = re.sub(r'(\d+)!', r'math_ivs.factorial(int(\1))', expression) # makes factorial to not evaluate immedialtelly but wait for =
        result = eval(expression)
        result_str = str(result)

        if len(result_str.replace(".", "").replace("-", "")) > 16: # if number is longer than 16 digits it shortens it
            result_str = f"{result:.10g}"

        display.set(result_str)
    except:
        display.set("Error")

def square_root():
    try:
        result = round(math_ivs.sqrt(float(display.get())), 6) # rounds to 6 decimal places
        display.set(str(result))
    except:
        display.set("Error")

def factorial():
    display.set(display.get() + "!")
def percentage():
    try:
        result = float(display.get()) / 100
        display.set(str(result))
    except:
        display.set("Error")




# Display
tkinter.Entry(canvas, textvariable=display, font=("Arial", 30), justify="right",state="readonly",readonlybackground="lightblue").place(x=10, y=10, width=380, height=100)

# Clear button
tkinter.Button(canvas, text="C",bg= "gainsboro",font= "Arial 20", command=clear).place(x=10, y=120, width=380, height=70)

# Row 5
tkinter.Button(canvas, text="√",bg = "darkorange",font= "Arial 20", command=square_root).place(x=10, y=200, width=87.5, height=50)
tkinter.Button(canvas, text="^",bg = "darkorange",font= "Arial 20", command=lambda: press("^")).place(x=107.5, y=200, width=87.5, height=50)
tkinter.Button(canvas, text="!",bg = "darkorange",font= "Arial 20", command=factorial).place(x=205, y=200, width=87.5, height=50)
tkinter.Button(canvas, text="÷",bg = "darkorange",font= "Arial 20", command=lambda: press("÷")).place(x=302.5, y=200, width=87.5, height=50)

# Row 4
tkinter.Button(canvas, text="7",bg= "gainsboro",font= "Arial 20", command=lambda: press(7)).place(x=10, y=260, width=87.5, height=50)
tkinter.Button(canvas, text="8",bg= "gainsboro",font= "Arial 20", command=lambda: press(8)).place(x=107.5, y=260, width=87.5, height=50)
tkinter.Button(canvas, text="9",bg= "gainsboro",font= "Arial 20", command=lambda: press(9)).place(x=205, y=260, width=87.5, height=50)
tkinter.Button(canvas, text="×",bg = "darkorange",font= "Arial 20", command=lambda: press("×")).place(x=302.5, y=260, width=87.5, height=50)

# Row 3
tkinter.Button(canvas, text="4",bg= "gainsboro",font= "Arial 20", command=lambda: press(4)).place(x=10, y=320, width=87.5, height=50)
tkinter.Button(canvas, text="5",bg= "gainsboro",font= "Arial 20", command=lambda: press(5)).place(x=107.5, y=320, width=87.5, height=50)
tkinter.Button(canvas, text="6",bg= "gainsboro",font= "Arial 20", command=lambda: press(6)).place(x=205, y=320, width=87.5, height=50)
tkinter.Button(canvas, text="-",bg = "darkorange",font= "Arial 20", command=lambda: press("-")).place(x=302.5, y=320, width=87.5, height=50)

# Row 2
tkinter.Button(canvas, text="1",bg= "gainsboro",font= "Arial 20", command=lambda: press(1)).place(x=10, y=380, width=87.5, height=50)
tkinter.Button(canvas, text="2",bg= "gainsboro",font= "Arial 20", command=lambda: press(2)).place(x=107.5, y=380, width=87.5, height=50)
tkinter.Button(canvas, text="3",bg= "gainsboro",font= "Arial 20", command=lambda: press(3)).place(x=205, y=380, width=87.5, height=50)
tkinter.Button(canvas, text="+",bg = "darkorange",font= "Arial 20", command=lambda: press("+")).place(x=302.5, y=380, width=87.5, height=50)

# Row 1 (bottom)
tkinter.Button(canvas, text="%", bg="darkorange", font="Arial 20", command=percentage).place(x=10, y=440, width=87.5, height=50) # not sure what our additional functions gonna be so i left it blank
tkinter.Button(canvas, text="0",bg= "gainsboro",font= "Arial 20", command=lambda: press(0)).place(x=107.5, y=440, width=87.5, height=50)
tkinter.Button(canvas, text=".",bg = "darkorange",font= "Arial 20", command=lambda: press(".")).place(x=205, y=440, width=87.5, height=50)
tkinter.Button(canvas, text="=",bg= "darkorange",font= "Arial 20", command=calculate).place(x=302.5, y=440, width=87.5, height=50)

# makes also possible to use buttons on keyboard to calculate
canvas.bind_all("<Key>", lambda e: press(e.char) if e.char in "0123456789.+-*/" else None)
canvas.bind_all("<Return>", lambda e: calculate())
canvas.bind_all("<BackSpace>", lambda e: display.set(display.get()[:-1]))
canvas.bind_all("<Escape>", lambda e: clear())
root.mainloop()
