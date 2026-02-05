import turtle
import time
import random

COLORS = ["red", "blue", "brown", "yellow", "purple", "magenta",
          "black", "pink", "cyan", "orange"]

def get_num_of_turtles():
    while True:
        racers = input("How many turtles do you want (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 10:
                return racers
        print("Invalid input...Try again!")

def countdown(screen, seconds):
    counter = turtle.Turtle()
    counter.hideturtle()
    counter.penup()
    counter.color("white")
    counter.goto(0, 0)

    screen.tracer(0)
    for i in range(seconds, 0, -1):
        counter.clear()
        counter.write(f"Race starts in {i}", align="center",
                      font=("Arial", 30, "bold"))
        screen.update()
        time.sleep(1)

    counter.clear()
    counter.write("GO!!!", align="center",
                  font=("Arial", 40, "bold"))
    screen.update()
    time.sleep(1)
    counter.clear()
    screen.tracer(1)

def create_turtles(colors):
    turtles = []
    spacingx = 600 // (len(colors) + 1)

    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-600//2 + (i+1) * spacingx, -600//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def race(turtles, colors):
    while True:
        for racer in turtles:
            racer.forward(random.randrange(1, 20))
            _, y = racer.pos()
            if y >= 600//2 - 10:
                return colors[turtles.index(racer)]

def init_turtle():
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.title("Race for Live")
    screen.bgcolor("green")
    return screen

def start_race():
    racers = get_num_of_turtles()
    screen = init_turtle()

    random.shuffle(COLORS)
    colors = COLORS[:racers]

    turtles = create_turtles(colors)   # 🐢 встали на линию
    countdown(screen, 10)               # ⏱️ потом отсчёт

    winner = race(turtles, colors)     # 🏁 старт
    print(f"The winner is: {winner}!!")

    screen.exitonclick()

start_race()
