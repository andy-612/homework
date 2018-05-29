#Question 1
"""
Add some new key bindings to the first sample program:
    -Pressing keys R, G or B should change tess’ color to Red, Green or Blue.
    -Pressing keys + or - should increase or decrease the width of tess’ pen.
        Ensure that the pen size stays between 1 and 20 (inclusive).
    -Handle some other keys to change some attributes of tess, or attributes
    of the window, or to give her new behaviour that can be controlled from the keyboard."""


"""
import turtle
turtle.setup(400,500)                # Determine the window size
wn = turtle.Screen()                 # Get a reference to the window
wn.title("Handling keypresses!")     # Change the window title
wn.bgcolor("lightgreen")             # Set the background color
tess = turtle.Turtle()    # Create our favorite turtle
# The next four functions are our "event handlers".
def h1():
   tess.forward(30)
def h2():
   tess.left(45)
def h3():
   tess.right(45)
def h4():
    wn.bye()
def h5():
    tess.color("red")
def h6():
    tess.color("green")
def h7():
    tess.color("blue")
sz = 1
def h8():
    global sz
    sz +=  1
    if sz > 20:
        sz = 20
    tess.pensize(sz)
def h9():
    global sz
    sz -= 1
    if sz<1:
        sz=1
def h10():
    tess.circle(20)
# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")
wn.onkey(h5, "r")
wn.onkey(h6, "g")
wn.onkey(h7, "b")
wn.onkey(h8, "=")
wn.onkey(h9, "-")
wn.onkey(h10, "c")
wn.listen()
wn.mainloop()
"""



#Question 3

"In an earlier chapter we saw two turtle methods, hideturtle and showturtle  "
"that can hide or show a turtle. This suggests that we could take a different "
"approach to the traffic lights program. Add to your program above as follows: "
"draw a second housing for another set of traffic lights. Create three separate "
"turtles to represent each of the green, orange and red lights, and position "
"them appropriately within your new housing. As your state changes occur, "
"just make one of the three turtles visible at any time. Once you’ve made the "
"changes, sit back and ponder some deep thoughts: you’ve now got two different "
"ways to use turtles to simulate the traffic lights, and both seem to work. Is "
"one approach somehow preferable to the other? Which one more closely resembles "
"reality — i.e. the traffic lights in your town?"


import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
bobgreen = turtle.Turtle()
boborange= turtle.Turtle()
bobred = turtle.Turtle()

def draw_housing():
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

draw_housing()

def green():
    bobgreen.home()
    bobgreen.penup()
    bobgreen.forward(40)
    bobgreen.left(90)
    bobgreen.forward(50)
    bobgreen.pendown()
    bobgreen.shape("circle")
    bobgreen.shapesize(3)
    bobgreen.fillcolor("green")
    bobgreen.penup()


def orange():
    boborange.home()
    boborange.penup()
    boborange.forward(40)
    boborange.left(90)
    boborange.forward(120)
    boborange.pendown()
    boborange.shape("circle")
    boborange.shapesize(3)
    boborange.fillcolor("orange")

def red():
    bobred.home()
    bobred.penup()
    bobred.forward(40)
    bobred.left(90)
    bobred.forward(190)
    bobred.pendown()
    bobred.shape("circle")
    bobred.shapesize(3)
    bobred.fillcolor("red")
green()
red()
orange()

tess.penup()
tess.forward(-150)

draw_housing()

tess.penup()

# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)

tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1:     # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
    else:                    # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0

def newmachine():
    global state_num
    if state_num == 0:  # Transition from state 0 to state 1
        bobgreen.st()
        bobred.ht()
        boborange.ht()
        #green()

        state_num = 1
    elif state_num == 1:  # Transition from state 1 to state 2
        boborange.st()
        bobred.ht()
        bobgreen.ht()
        #orange()
        state_num = 2
    else:  # Transition from state 2 to state 0
        bobred.st()
        boborange.ht()
        bobgreen.ht()
        #red()
        state_num = 0

wn.onkey(advance_state_machine, "space")
wn.onkey(newmachine, "Up")

wn.listen()
wn.mainloop()

#the new approach (with three turtles) most closely resembles reality
#in reality, lights do not change gradually instead they are instantaneous so it would
#make more sense to use the second approach where individual turtles are responsible for their
#own light