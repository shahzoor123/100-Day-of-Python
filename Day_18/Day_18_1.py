from turtle import Turtle, Screen

tummy = Turtle()

tummy.shape('turtle')
tummy.color('brown')

# for _ in range(4):
#     tummy.forward(100)
#     tummy.left(90)
#
# for _ in range(5):
#     tummy.forward(30)
#     tummy.penup()
#     tummy.forward(30)
#     tummy.pendown()


# Triangle
for _ in range(3):
    tummy.forward(100)
    tummy.right(120)


# Square

for _ in range(4):
    tummy.color('pink')

    tummy.forward(100)
    tummy.right(-90)
#
# # Pentagon
for _ in range(5):
    tummy.forward(100)
    tummy.left(72)


# Hexagon
#
for _ in range(6):
    tummy.forward(100)
    tummy.left(60)

# octagon
#
for _ in range(8):
    tummy.forward(100)
    tummy.left(45)


# Decagon
for _ in range(9):
    tummy.forward(100)
    tummy.left(40)

screen = Screen()
screen.exitonclick()
