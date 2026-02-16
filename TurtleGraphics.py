#TurtleGraphics.py
#Name:Tori Gregory
#Date:2/15/26
#Assignment:Lab 4

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(Milly, sides):
    for s in range(sides):
        Milly.forward(50)
        Milly.right(360/sides)

def fillCorner(Maurice, corner):
    drawSquare(Maurice, 100)
    if corner == 1:
        Maurice.begin_fill()
        drawSquare(Maurice, 50)
        Maurice.end_fill()
    elif corner == 2:
        Maurice.forward(50)
        Maurice.begin_fill()
        drawSquare(Maurice, 50)
        Maurice.end_fill()
    elif corner == 4:
        Maurice.forward(100)
        Maurice.right(90)
        Maurice.forward(50)
        Maurice.begin_fill()
        drawSquare(Maurice, 50)
        Maurice.end_fill()
    else:
        Maurice.right(90)
        Maurice.forward(50)
        Maurice.left(90)
        Maurice.begin_fill()
        drawSquare(Maurice, 50)
        Maurice.end_fill()
        
def squaresInSquares(Rhea, num):
    size = 100
    offset = 10
    for i in range(num):
        Rhea.up()
        Rhea.forward(offset)
        Rhea.right(90)
        Rhea.forward(offset)
        Rhea.left(90)
        Rhea.down()
        drawSquare(Rhea, size)
        size -= 2 * offset
        
        
        

def main():
    myTurtle = turtle.Turtle()
    
    drawPolygon(myTurtle, 5)
    
    drawPolygon(myTurtle, 8)
   
    fillCorner(myTurtle, 2)
   
    fillCorner(myTurtle, 3)
    
    squaresInSquares(myTurtle, 5)
   
    squaresInSquares(myTurtle, 3)