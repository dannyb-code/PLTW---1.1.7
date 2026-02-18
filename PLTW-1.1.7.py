import turtle as trtl
my_turtles = []

turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for i in range(len(turtle_shapes)):
    t = trtl.Turtle()
    t.shape(turtle_shapes[i])
    t.color(turtle_colors[i])
    my_turtles.append(t)

positions = [
    (0, -110),
    (120, -80),
    (130, 0),
    (90, 90),
    (0, 120),
    (-50, 100)
]

for i in range(len(my_turtles)):
    my_turtles[i].penup()
    my_turtles[i].goto(positions[i])

for i in range(len(my_turtles)-1):
    my_turtles[i].pendown()
    my_turtles[i].goto(positions[i+1])

wn = trtl.Screen()
wn.mainloop()
