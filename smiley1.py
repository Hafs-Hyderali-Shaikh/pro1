import turtle

def draw_circle(x,y,radius,fill_color):
    t=turtle.Turtle()
    t.up()
    t.goto(x,y - radius)
    t.down()
    t.begin_fill()
    t.circle(radius)
    t.fillcolor(fill_color)
    t.end_fill()
    t.up()

def draw_centered_circle(x,y,radius,fill_color):
    t=turtle.Turtle()
    t.up()
    t.goto(x, y - radius)
    t.down()

    t.begin_fill()
    t.circle(radius)
    t.fillcolor(fill_color)
    t.end_fill()

    t.up()

def tweek(speed,trac):
    turtle.speed(speed)
    turtle.tracer(trac)
    
def draw_eye(x,y,radius,iris_color):
    #eyeball
    draw_circle(x, y, radius, "white")
    iris_radius = radius / 2
    draw_circle(x, y, iris_radius, iris_color)
    pupil_radius = radius / 4
    draw_circle(x, y, pupil_radius, "black")


def draw_mouth(x,y,radius,fill_color):
    t=turtle.Turtle()
    t.up()
    t.goto(x,y)
    t.down()
    t.right(90)
    t.begin_fill()
    t.circle(radius/2,180)
    t.fillcolor(fill_color)
    t.end_fill()

    t.up()
    

    
def Main():
    tweek(0,False)
    draw_circle(0,0,200,"yellow")
    draw_centered_circle(0,0,20,"pink")
    draw_eye(70,70,50,"blue")
    draw_eye(-70,70,50,"blue")
    draw_mouth(-80,-50,160,"black")
    input("please enter to continue...")
    
Main()