"""!
@file main.py
@brief Graphical user interface for the calculator application.

@details This module provides a tkinter-based GUI for the calculator,
supporting basic and advanced mathematical operations including addition,
subtraction, multiplication, division, factorial, power, square root
and percentage. The calculator can be operated via both mouse and keyboard.

@author Samuel Cehlarik
@date 2026
@version 1.0

@copyright GNU GPL v3
"""

import tkinter
import math_ivs

# Initialize the main window
root = tkinter.Tk()
root.title("Calc")

# Create the main canvas with fixed dimensions
canvas = tkinter.Canvas(height=500, width=400, bg= "darkgrey")
canvas.pack()

# Set the application icon
logo = tkinter.PhotoImage(file="logo.png")
root.iconphoto(True, logo)

# Variable to hold the current display value
display = tkinter.StringVar()

def press(value):
    """!
    @brief Function that is called when button was pressed , shows it on display, prevents double operators and
    expression to start with operator except "-".
    @param value button with value that was pressed
    @return None
    """
    current = display.get()

    operators = "+-×÷^."

    # If input is an operator
    if str(value) in operators:
        # Prevent operator at start (except minus for negative numbers)
        if current == "":
            if value == "-":
                display.set(value)
            return

        # Prevent double operators (like ++, --, ×÷ etc.)
        if current[-1] in operators:
            return

    display.set(current + str(value))

def clear():
    """!
    @brief Clears display.
    @return None
    """
    display.set("")

def calculate():
    """!
    @brief Calculates the expression using math_ivs library, displays it on screen.
    @return None
    @throws Exception If the expression is invalid, displays "Error" on screen.
    """

    try:
        expression = display.get()  # gets the expression that is written on the display
        result = math_ivs.evaluate(expression)
        result_str = str(result)

        # if number is longer than 16 digits it shortens it
        if len(result_str.replace(".", "").replace("-", "")) > 16:
            result_str = f"{result:.10g}"

        display.set(result_str)
    except:
        display.set("Error")

def factorial():
    """!
    @brief Sets "!" on the display.
    @return None
    """
    display.set(display.get() + "!")
def percentage():
    """!
        @brief Sets decimal version of percentage on the display.
        @return None
        @throws ValueError If the display is empty or contains an invalid value.
    """
    try:
        result = float(display.get()) / 100
        display.set(str(result))
    except:
        display.set("Error")

def open_image_window():
    """!
    @brief Opens a new window displaying a hint image for the calculator.
    @return None
    """
    # Create a new popup window
    new_window = tkinter.Toplevel(root)
    new_window.title("Hint")
    new_window.geometry("587x448")

    # Load and scale down the hint image by half
    img = tkinter.PhotoImage(file="hintcalc.png").subsample(2, 2)

    # Display the image in a label
    label = tkinter.Label(new_window, image=img)
    label.image = img  # Keep reference to prevent garbage collection
    label.pack()

# Read-only display entry at the top of the calculator
tkinter.Entry(canvas, textvariable=display, font=("Arial", 30), justify="right",state="readonly",readonlybackground="lightblue").place(x=10, y=10, width=380, height=100)

# Clear button spanning most of the top row
tkinter.Button(canvas, text="C",bg= "gainsboro",font= "Arial 20", command=clear).place(x=10, y=120, width=262.5+20, height=70)

# Row 5 - advanced operations
tkinter.Button(canvas, text="√",bg = "darkorange",font= "Arial 20",command=lambda: press("√")).place(x=10, y=200, width=87.5, height=50)
tkinter.Button(canvas, text="^",bg = "darkorange",font= "Arial 20", command=lambda: press("^")).place(x=107.5, y=200, width=87.5, height=50)
tkinter.Button(canvas, text="!",bg = "darkorange",font= "Arial 20", command=factorial).place(x=205, y=200, width=87.5, height=50)
tkinter.Button(canvas, text="÷",bg = "darkorange",font= "Arial 20", command=lambda: press("÷")).place(x=302.5, y=200, width=87.5, height=50)

# Row 4 - numbers 7-9 and multiplication
tkinter.Button(canvas, text="7",bg= "gainsboro",font= "Arial 20", command=lambda: press(7)).place(x=10, y=260, width=87.5, height=50)
tkinter.Button(canvas, text="8",bg= "gainsboro",font= "Arial 20", command=lambda: press(8)).place(x=107.5, y=260, width=87.5, height=50)
tkinter.Button(canvas, text="9",bg= "gainsboro",font= "Arial 20", command=lambda: press(9)).place(x=205, y=260, width=87.5, height=50)
tkinter.Button(canvas, text="×",bg = "darkorange",font= "Arial 20", command=lambda: press("×")).place(x=302.5, y=260, width=87.5, height=50)

# Row 3 - numbers 4-6 and subtraction
tkinter.Button(canvas, text="4",bg= "gainsboro",font= "Arial 20", command=lambda: press(4)).place(x=10, y=320, width=87.5, height=50)
tkinter.Button(canvas, text="5",bg= "gainsboro",font= "Arial 20", command=lambda: press(5)).place(x=107.5, y=320, width=87.5, height=50)
tkinter.Button(canvas, text="6",bg= "gainsboro",font= "Arial 20", command=lambda: press(6)).place(x=205, y=320, width=87.5, height=50)
tkinter.Button(canvas, text="-",bg = "darkorange",font= "Arial 20", command=lambda: press("-")).place(x=302.5, y=320, width=87.5, height=50)

# Row 2 - numbers 1-3 and addition
tkinter.Button(canvas, text="1",bg= "gainsboro",font= "Arial 20", command=lambda: press(1)).place(x=10, y=380, width=87.5, height=50)
tkinter.Button(canvas, text="2",bg= "gainsboro",font= "Arial 20", command=lambda: press(2)).place(x=107.5, y=380, width=87.5, height=50)
tkinter.Button(canvas, text="3",bg= "gainsboro",font= "Arial 20", command=lambda: press(3)).place(x=205, y=380, width=87.5, height=50)
tkinter.Button(canvas, text="+",bg = "darkorange",font= "Arial 20", command=lambda: press("+")).place(x=302.5, y=380, width=87.5, height=50)

# Row 1 - percentage, 0, decimal point and equals
tkinter.Button(canvas, text="%", bg="darkorange", font="Arial 20", command=percentage).place(x=10, y=440, width=87.5, height=50)
tkinter.Button(canvas, text="0",bg= "gainsboro",font= "Arial 20", command=lambda: press(0)).place(x=107.5, y=440, width=87.5, height=50)
tkinter.Button(canvas, text=".",bg = "darkorange",font= "Arial 20", command=lambda: press(".")).place(x=205, y=440, width=87.5, height=50)
tkinter.Button(canvas, text="=",bg= "darkorange",font= "Arial 20", command=calculate).place(x=302.5, y=440, width=87.5, height=50)


#hint button
tkinter.Button(canvas, text="?",bg="gainsboro", font="Arial 20", command=open_image_window).place(x=302.5, y=120, width=87.5, height=70)
# Keyboard bindings for calculator operation
canvas.bind_all("<Key>", lambda e: press(e.char) if e.char in "0123456789.+-*/" else None)  # number and operator keys
canvas.bind_all("<Return>", lambda e: calculate())    # Enter key to calculate
canvas.bind_all("<BackSpace>", lambda e: display.set(display.get()[:-1]))  # Backspace to delete last character
canvas.bind_all("<Escape>", lambda e: clear())        # Escape to clear display

# Start the main event loop
root.mainloop()