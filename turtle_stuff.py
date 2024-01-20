import turtle

def test_drive():
    t=turtle.Turtle()
    t.down()
    t.forward(100)
    t.left(87)
    t.setheading(127)
    t.up()
    t.down()
    t.goto(50,50)
    t.home()
    t.circle(25)
    
    
def turtle_state():
    print("Pen is down:", turtle.isdown())
    print("Heading angle:", turtle.heading())
    print("Current coordinates (X, Y):", turtle.xcor(), turtle.ycor())
    
    
    
def Main():
    turtle_state()
    test_drive()
    print("Turtle state after test_drive:")
    turtle_state()
    input("please enter to continue...")
    
Main()