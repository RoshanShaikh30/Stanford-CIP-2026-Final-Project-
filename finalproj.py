import turtle
import time
delay = 0.1
sn = turtle.Screen()
sn.title("Snake Game!")
sn.bgcolor("blue")
sn.setup(width=600, height=600)
sn.tracer(0)

#head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

while True:
    sn.update()
    move()
    time.sleep(delay)



sn.mainloop()