import turtle

def main(axiom, rules, iterations, length, angle, width=1000, height=1000, turtleOffsetX=0, turtleOffsetY=0):
    window = turtle.Screen() # screen settings
    window.setup(width, height)

    turtle.hideturtle() # turtle settings
    turtle.tracer(0)
    turtle.penup()
    turtle.setposition(turtleOffsetX, turtleOffsetY)
    turtle.pendown()

    drawCommands(setCommands(axiom, rules, iterations), length, angle)

    turtle.update() # window not closing
    turtle.mainloop()

def setCommands(axiom, rules, iterations):
    axiomTemporary = ""
    for i in range(iterations):
        for ch in axiom: axiomTemporary+=rules[ch]
        axiom = axiomTemporary
        axiomTemporary = ""
    return axiom

def drawCommands(axiom, length, angle):
    for ch in axiom:
        if ch == 'F': turtle.forward(length)
        elif ch == '+': turtle.right(angle)
        elif ch == '-': turtle.left(angle)
        elif ch == 'f':
            for i in range(4):
                turtle.forward(length)
                turtle.right(angle)

if __name__ == "__main__":
    main(axiom="F+F+F+F", rules={'+':'+', '-':'-', 'F':"F+f-F-F+F", 'f':"f"}, iterations=4, length=5, angle=90)


