from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Murga Snake")

s1 = Turtle()
s2 = Turtle()
s3 = Turtle()

s1.shape("square")
s2.shape("square")
s3.shape("square")

s1.penup()
s2.penup()
s3.penup()

s1.color("white")
s2.color("white")
s2.setx(-20)
s3.color("white")
s3.setx(-40)

screen.exitonclick()
