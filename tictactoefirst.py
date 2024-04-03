import turtle as t

t.tracer(0)
t.hideturtle()

current_turn = "X" #initial turn????
t.getcanvas().config(cursor="X_cursor")

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


def square_to_point(point_to_square): #changed this to take in the previous function as a parameter
    if point_to_square =='Northwest':
        return (-200, 200)
    elif point_to_square == 'North':
        return (0, 200)
    elif point_to_square == 'Northeast':
        return (200, 200)
    elif point_to_square == 'West':
        return (-200, 0)
    elif point_to_square == 'Center':
        return (0, 0)
    elif point_to_square == 'East':
        return (200, 0)
    elif point_to_square == 'Southwest':
        return (-200, -200)
    elif point_to_square == 'South':
        return (0,-200)
    elif point_to_square == 'Southeast':
        return (200, -200)
    else:
        return None
    

def point_to_square(x:float, y:float):
    square = None
    if -300<x<-100 and 100<y<300:
        square = 'Northwest'
        x,y = -200,200
    elif -100<x<100 and 100<y<300:
        square = 'North'
        x,y = 0,200
    elif 100<x<300 and 100<y<300:
        square = 'Northeast'
        x,y= 200,200
    elif -300<x<-100 and -100<y<100:
        square = 'West'
        x,y = -200,0
    elif -100<x<100 and -100<y<100:
        square = 'Center'
        x,y=0,0
    elif 100<x<300 and -100<y<100:
        square = 'East'
        x,y=200,0
    elif -300<x<-100 and -300<y<-100:
        square = 'Southwest'
        x,y = -200,-200
    elif -100<x<100 and -300<y<-100:
        square = 'South'
        x,y = 0,-200
    elif 100<x<300 and -300<y<-100:
        square = 'Southeast'
        x,y=200,-200
    return square
    
size = 75
def drawX(location, size): #changed the size to ex:75
    size = 75
    x,y = square_to_point(location)
    print(x,y)
    t.color('blue')
    t.pensize(10)
    t.shapesize(size)
    line((x - 50, y- 50), (x + 50, y + 50))
    line((x- 50, y + 50), (x + 50, y- 50))

    t.update()

radius = 50
def drawO(location, radius):
    x,y  = square_to_point(location)
    print(x,y)
    radius = 50
    t.color('red')
    t.pensize(10)
    circle(radius, x, y-50)
    t.update()

def turnX():
    square = square_to_point()
    size = 75
    print(size)
    square = square_to_point()
    drawX(square, size)
    t.getcanvas().config(cursor="X_cursor")


def turnO():
    square = square_to_point()
    drawO(square, radius )
    t.getcanvas().config(cursor="circle")

def mouseclick(x:float,y:float):
    if current_turn == "X":
        drawX(point_to_square(x,y),size)
    elif current_turn == "O":
        drawO(point_to_square(x,y), radius)
    else:
        return None

#idea: functions turnX and turnO need to be in one function called changeturn, where I keep track of the turns and also keep track of the "t.onkeyrelease" function 
def changeturn(): #refer to long comment about putting turnX and turnO into it
    global current_turn
    
    if current_turn == "X":
        t.getcanvas().config(cursor="circle")
        current_turn ="O"
        t.title(titlestring ="Current player: O")
    elif current_turn == "O":
        t.getcanvas().config(cursor="X_cursor")
        current_turn = "X"
        t.title(titlestring ="Current player: X")
    print(current_turn)

grid()
t.onscreenclick(mouseclick)
t.onkeypress(changeturn, "space")

t.listen()
t.update()
t.mainloop()
