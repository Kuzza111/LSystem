import turtle
import random

def main(axiom, rules, iterations, length, angle, randOffset, width=1000, height=1000, turtleOffsetX=0, turtleOffsetY=0, thick=16, isRandomRules=False, randomRulesLength=7):
    window = turtle.Screen() # screen settings
    window.setup(width, height)

    turtle.hideturtle() # turtle settings
    turtle.tracer(0)
    turtle.penup()
    turtle.setposition(turtleOffsetX, turtleOffsetY)
    turtle.left(90)
    turtle.pendown()
    turtle.pensize(thick)

    if isRandomRules: rules = randomRules(randomRulesLength)
    drawCommands(setCommands(axiom, rules, iterations), length, angle, randOffset, thick) # calculate and draw

    turtle.update() # window not closing
    turtle.mainloop()

def setCommands(axiom, rules, iterations):
    axiomTemporary = ""
    for i in range(iterations):
        for ch in axiom: 
            if ch in rules: axiomTemporary+=rules[ch]
            else: axiomTemporary+=ch
        axiom = axiomTemporary
        axiomTemporary = ""
    return axiom

def drawCommands(axiom, length, angle, randOffset, thick):
    stack = []
    for ch in axiom:
        if ch == '0': turtle.forward(length)
        elif ch == '1': 
            if random.randint(0,10)>4: turtle.forward(length) # also semi random height
        elif ch == '2': 
            if random.randint(0,10)>4: turtle.forward(length * 1.5) # semi random height of trees!
        elif ch == '+': turtle.right(angle + random.randint(-randOffset, randOffset))
        elif ch == '-': turtle.left(angle + random.randint(-randOffset, randOffset))
        elif ch == '[': 
            thick = thick*0.75
            turtle.pensize(thick)
            stack.append(thick)
            stack.append(turtle.xcor())
            stack.append(turtle.ycor())
            stack.append(turtle.heading())
        elif ch == ']': 
            turtle.penup()
            turtle.setheading(stack.pop())
            turtle.sety(stack.pop())
            turtle.setx(stack.pop())
            thick = stack.pop()
            turtle.pensize(thick)
            turtle.pendown()

def randomRules(randomRulesLength): # not recommended for use, only usable with some kind of neuro or genetic algorithms
    rules = {}
    for i in range(randomRulesLength):
        rules[i] = random.randint(0, 6)
        if rules[i] == 3: rules[i] = '+'
        elif rules[i] == 4: rules[i] = '-'
        elif rules[i] == 5: rules[i] = '['
        elif rules[i] == 6: rules[i] = ']'
    return rules

main(axiom="0", rules={'1':"21", '0':'1[-0]+0'}, iterations=14, length=7, angle=25, randOffset=20,turtleOffsetY=-300, )
# maybe ill do it better later, more colors and branches

