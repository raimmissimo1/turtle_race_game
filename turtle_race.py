import turtle
import time
import random

COLORS = ["red", "blue", "green", "yellow", "purple", "magenta", "black","pink","cyan","orange"]

def get_num_of_turtles():
    racers = 0
    while True:
        racers = input("How many turtles do you want(2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Your input is not numeric...Try again!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Invalid input...Try again!")

def race(colors):
    turtles = create_turtle(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x,y = racer.pos()
            if y >= 600//2-10:
                return colors[turtles.index(racer)]

def create_turtle(colors):
    turtles = []
    spacingx = 600 // (len(colors) + 1)
    for i,color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-600//2 + (i+1) * spacingx , -600//2+20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.title("Race for Live")
    screen.bgcolor("silver")

def start_race():
    racers = get_num_of_turtles()
    init_turtle()
    random.shuffle(COLORS)
    colors = COLORS[:racers]

    winner = race(colors)
    print(f"The winner is: {winner}!!")
    time.sleep(5)

start_race()