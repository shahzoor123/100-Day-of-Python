from turtle import Turtle, Screen

tummy = Turtle()

tummy.shape('turtle')
tummy.color('black')
# for _ in range(4):
#     tummy.forward(100)
#     tummy.left(90)

for _ in range(5):
    tummy.forward(30)
    tummy.penup()
    tummy.forward(30)
    tummy.pendown()


screen = Screen()
screen.exitonclick()
