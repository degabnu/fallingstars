import random
import turtle
import math

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Falling Stars")
screen.tracer(0)  # Turn off animation for faster drawing

# Star class
class Star:
    def __init__(self):
        self.x = random.uniform(-200, 200)  # Adjust for screen size
        self.y = random.randint(200, screen.window_height() // 2)  # Start at top half
        self.speed = random.uniform(0.5, 2)  # Adjust speed range
        self.size = random.randint(10, 20)  # Adjust star size
        self.brightness = random.uniform(0.5, 1.5)  # Adjust brightness
        self.color = (self.brightness, self.brightness, self.brightness)  # Create a white-ish color range
        self.rotation = random.randint(-5, 5)  # Random rotation

    def update(self):
        self.x += random.uniform(-0.5, 0.5)  # Simulate turbulence
        self.y -= self.speed
        if self.y < -screen.window_height() // 2:  # Disappear below screen
            self.reset_star()

    def reset_star(self):
        self.x = random.uniform(-200, 200)
        self.y = random.randint(200, screen.window_height() // 2)
        self.speed = random.uniform(0.5, 2)
        self.size = random.randint(10, 20)
        self.brightness = random.uniform(0.5, 1.5)
        self.color = (self.brightness, self.brightness, self.brightness)
        self.rotation = random.randint(-5, 5)

    def draw(self, pen):
        pen.penup()
        pen.goto(self.x, self.y)
        pen.pendown()
        pen.fillcolor(self.color_to_string(self.color))
        pen.begin_fill()
        # Draw a star
        for _ in range(5):
            pen.forward(self.size)
            pen.right(144)
        pen.end_fill()

    def color_to_string(self, color):
        r = int(color[0] * 255)
        g = int(color[1] * 255)
        b = int(color[2] * 255)
        return "#{:02x}{:02x}{:02x}".format(r, g, b)


# Create stars and pen
stars = []
pen = turtle.Turtle()
pen.speed(0)  # Set drawing speed to fastest
pen.hideturtle()  # Hide the turtle

# Create and draw stars
for _ in range(30):
    stars.append(Star())
    stars[-1].draw(pen)

# Update and redraw stars
def update():
    screen.update()  # Update the screen

    for star in stars:
        star.update()

    pen.clear()  # Clear previous stars
    for star in stars:
        star.draw(pen)

    screen.ontimer(update, 16)  # Call update every 16 milliseconds (adjust for animation speed)

screen.listen()
screen.ontimer(update, 16)  # Start the animation
screen.exitonclick()
