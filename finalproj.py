import turtle
import time
import random 

delay = 0.2
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

        
def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"
def go_left():
    head.direction = "left"
def go_right():
    head.direction = "right"

sn.listen()
sn.onkeypress(go_up, "w")
sn.onkeypress(go_down, "s")
sn.onkeypress(go_left, "a")
sn.onkeypress(go_right, "d")

#food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("brown")
food.penup()
food.goto(0, 100)


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
    #moving food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        
    move()
    time.sleep(delay)



sn.mainloop()
