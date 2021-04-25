from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for color_index in range(0, len(colors)-1):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[color_index])
    new_turtle.penup()
    new_turtle.goto(-230, -100 + color_index * 50)
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lose! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()