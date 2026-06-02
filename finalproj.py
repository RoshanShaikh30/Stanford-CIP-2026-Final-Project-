import turtle
sn = turtle.Screen()
sn.title("Snake Game!")
sn.bgcolor("blue")
sn.setup(width=600, height=600)
sn.tracer(0)

#head ig
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

while True:
    sn.update()

sn.mainloop()