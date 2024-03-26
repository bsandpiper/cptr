import turtle as t

t.tracer(0)
t.hideturtle()

turn = "X" #initial turn????

def line(start,end):
    t.penup()
    t.goto(start)
    t.pendown()
    t.goto(end)

def circle(radius, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(radius)

def grid():
    #horizontal
    line((-300, 100), (300, 100))
    line((-300, -100), (300, -100))

   #vertical
    line((-100, 300), (-100, -300))
    line((100, -300), (100, 300))

def point_to_square(x:float, y:float):
    if x == -250 and y == 250:
        return 'Northwest'
    elif x == 0 and y == 250:
        return 'North'
    elif x == 250 and y == 250:
        return 'Northeast'
    elif x == -250 and y == 0:
        return 'West'
    elif x == 0 and y == 0:
        return 'Center'
    elif x == 250 and y == 0:
        return 'East'
    elif x == -250 and y == -250:
        return 'Southwest'
    elif x == 0 and y == -250:
        return 'South'
    elif x == 250 and y == -250:
        return 'Southeast'
    else:
        return None

def square_to_point(sq: str):
    if sq =='Northwest':
        return (-250, 250)
    elif sq == 'North':
        return (0, 250)
    elif sq == 'Northeast':
        return (250, 250)
    elif sq == 'West':
        return (-250, 0)
    elif sq == 'Center':
        return (0, 0)
    elif sq == 'East':
        return (250, 0)
    elif sq == 'Southwest':
        return (-250, -250)
    elif sq == 'South':
        return (0,-250)
    elif sq == 'Southeast':
        return (250, -250)
    else:
        return None
    

def hit(x:float, y:float):
    square = None
    if -300<x<-100 and 100<y<300:
        square = 'Northwest'
    elif -100<x<100 and 100<y<300:
        square = 'North'
    elif 100<x<300 and 100<y<300:
        square = 'Northeast'
    elif -300<x<-100 and -100<y<100:
        square = 'West'
    elif -100<x<100 and -100<y<100:
        square = 'Center'
    elif 100<x<300 and -100<y<100:
        square = 'East'
    elif -300<x<-100 and -300<y<-100:
        square = 'Southwest'
    elif -100<x<100 and 300<y<-100:
        square = 'South'
    elif 100<x<300 and -300<y<-100:
        square = 'Southeast'
    return square
    

def drawX (sq:str):
    t.color('blue')
    t.pensize(10)
    x,y=square_to_point(sq)
    line(x - 50, y- 50, x + 50, y + 50)
    line(x- 50, y + 50, x + 50, y- 50)

def drawO (sq:str):
    t.color('red')
    t.pensize(10)
    x,y = square_to_point(sq)
    circle(50, x, y)


def turnX():
    if turn == "X":
        t.getcanvas().config(cursor="X_cursor")

def turnO():
    if turn == "O":
        t.getcanvas().config(cursor="circle")

def mouseclick(x:float,y:float):
    what_square = point_to_square(x,y)
    # if what_square is not None:
        # draw_shape()

    
    


grid()

t.update()
t.mainloop()
