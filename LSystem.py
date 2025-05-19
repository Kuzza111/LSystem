import turtle

angle = 90 # constants
length = 5

turtle.hideturtle() # turtle settings
turtle.tracer(0)
turtle.penup()
turtle.setposition(-300, -150)
turtle.pendown()


axiom = "F+F+F+F"
axiomTemp = ""
iterations = 4

transalte={'+':'+', '-':'-', 'F':"F+f-F-F+F", 'f':"f"} # setting commands
for i in range(iterations): # creating command line
    for ch in axiom:
        axiomTemp+=transalte[ch]
    axiom = axiomTemp
    axiomTemp = ""

for ch in axiom: # drawing commands
    if ch == 'F': turtle.forward(length)
    elif ch == '+': turtle.right(angle)
    elif ch == '-': turtle.left(angle)
    elif ch == 'f':
        for i in range(4):
            turtle.forward(length)
            turtle.right(angle)


turtle.update() # window not closing
turtle.mainloop()