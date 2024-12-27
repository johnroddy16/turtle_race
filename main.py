#!/usr/bin/env python3 

import turtle as t
import random 

screen = t.Screen()
screen.setup(width=500, height=400)  # set screen to be 500 x 400 pixels 
user_wager = screen.textinput(title='Place you wager', prompt='Which turtle will win the race? Enter a color: ')
colors = ['blue', 'red', 'orange', 'purple', 'yellow', 'green']
names = ['john', 'fred', 'tim', 'kevin', 'michael', 'ben']  # don't really need this but was trying it out 
all_turtles = []

race_on = False 

x = -240
y = -60 
for i in range(len(colors)):
    names[i] = t.Turtle(shape='turtle')  # could also write: new_turtle = ....
    names[i].penup() 
    names[i].color(colors[i])
    names[i].goto(x, y)
    all_turtles.append(names[i])
    y += 30  

if user_wager:
    race_on = True 
    
while race_on:
    for turtle in all_turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance) 
        if turtle.position()[0] >= 240:  # could also write: if turtle.xcor() >= 240:
            race_on = False 
            winning_color = turtle.pencolor()
            if winning_color == user_wager:
                print(f'you win! the winning turtle was the {winning_color} turtle!')
            else:
                print(f'you lost! the winning turtle was the {winning_color} turtle!')   
    



 
screen.exitonclick()   