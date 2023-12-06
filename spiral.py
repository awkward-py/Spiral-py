import turtle
import colorsys

# Set up the turtle
turtle.speed(0)
turtle.bgcolor("black")
turtle.hideturtle()

# Function to draw a colorful spiral
def draw_spiral():
    for i in range(360):
        hue = i / 360.0
        color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        turtle.color(color)
        turtle.forward(i)
        turtle.right(45)

# Draw the colorful spiral
draw_spiral()

# Close the window on click
turtle.exitonclick()
