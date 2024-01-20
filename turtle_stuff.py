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
    
def Main():
    test_drive()
    input("please enter to continue...")
    
Main()