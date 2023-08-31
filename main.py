
import turtle
drawing_board = turtle.Screen()
drawing_board.bgcolor("cyan")
drawing_board.title("geometric obejects on turtle")

#square
'''
turtle_instance = turtle.Turtle()
for i in range (4):
    turtle_instance.forward(100)
    turtle_instance.right(90)
'''
#star
'''
turtle_instance3=turtle.Turtle()
for i in range(5):
    turtle_instance3.right(144)
    turtle_instance3.forward(300)
'''
'''
turtle_instance3=turtle.Turtle()
for i in range(5):
    turtle_instance3.right(144)
    turtle_instance3.forward(300)
'''
'''
#polygon-altıgen
turtle_instance = turtle.Turtle()
num_sides = 6
angle = 360.0/num_sides
side_length = 100
for i in range(num_sides):
    turtle_instance.right(angle)
    turtle_instance.forward(side_length)
'''
turtle.done()