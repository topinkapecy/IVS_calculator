import tkinter
import math

canvas = tkinter.Canvas(height=500, width=400)
canvas.pack()

display = tkinter.StringVar()

def press(value):
    display.set(display.get() + str(value))

def clear():
    display.set("")

def calculate():
    try:
        expression = display.get().replace("X", "*").replace("^", "**")
        result = eval(expression)
        display.set(result)
    except:
        display.set("Error")

def square_root():
    try:
        result = math.sqrt(float(display.get()))
        display.set(str(result))
    except:
        display.set("Error")

def factorial():
    try:
        result = math.factorial(int(display.get()))
        display.set(str(result))
    except:
        display.set("Error")

# for frontend modify anything below (except already preset values)



# Display
tkinter.Entry(canvas, textvariable=display, font=("Arial", 20), justify="right").place(x=10, y=10, width=380, height=100)

# Clear button
tkinter.Button(canvas, text="C", command=clear).place(x=10, y=120, width=380, height=70)

# Row 5
tkinter.Button(canvas, text="sqrt()", command=square_root).place(x=10, y=200, width=87.5, height=50)
tkinter.Button(canvas, text="^", command=lambda: press("^")).place(x=107.5, y=200, width=87.5, height=50)
tkinter.Button(canvas, text="!", command=factorial).place(x=205, y=200, width=87.5, height=50)
tkinter.Button(canvas, text="/", command=lambda: press("/")).place(x=302.5, y=200, width=87.5, height=50)

# Row 4
tkinter.Button(canvas, text="7", command=lambda: press(7)).place(x=10, y=260, width=87.5, height=50)
tkinter.Button(canvas, text="8", command=lambda: press(8)).place(x=107.5, y=260, width=87.5, height=50)
tkinter.Button(canvas, text="9", command=lambda: press(9)).place(x=205, y=260, width=87.5, height=50)
tkinter.Button(canvas, text="X", command=lambda: press("X")).place(x=302.5, y=260, width=87.5, height=50)

# Row 3
tkinter.Button(canvas, text="4", command=lambda: press(4)).place(x=10, y=320, width=87.5, height=50)
tkinter.Button(canvas, text="5", command=lambda: press(5)).place(x=107.5, y=320, width=87.5, height=50)
tkinter.Button(canvas, text="6", command=lambda: press(6)).place(x=205, y=320, width=87.5, height=50)
tkinter.Button(canvas, text="-", command=lambda: press("-")).place(x=302.5, y=320, width=87.5, height=50)

# Row 2
tkinter.Button(canvas, text="1", command=lambda: press(1)).place(x=10, y=380, width=87.5, height=50)
tkinter.Button(canvas, text="2", command=lambda: press(2)).place(x=107.5, y=380, width=87.5, height=50)
tkinter.Button(canvas, text="3", command=lambda: press(3)).place(x=205, y=380, width=87.5, height=50)
tkinter.Button(canvas, text="+", command=lambda: press("+")).place(x=302.5, y=380, width=87.5, height=50)

# Row 1 (bottom)
tkinter.Button(canvas, text="", command=None).place(x=10, y=440, width=87.5, height=50) # not sure what our additional functions gonna be so i left it blank
tkinter.Button(canvas, text="0", command=lambda: press(0)).place(x=107.5, y=440, width=87.5, height=50)
tkinter.Button(canvas, text=".", command=lambda: press(".")).place(x=205, y=440, width=87.5, height=50)
tkinter.Button(canvas, text="=", command=calculate).place(x=302.5, y=440, width=87.5, height=50)

canvas.mainloop()