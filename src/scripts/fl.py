import random
import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Moving Stars")
screen.tracer(0)

class Star:
    def __init__(self):
        self.x = random.uniform(-screen.window_width() / 2, screen.window_width() / 2)
        self.y = random.uniform(-screen.window_height() / 2, screen.window_height() / 2)
        self.speed = random.uniform(0.5, 2)
        self.size = random.randint(10, 20)
        self.brightness = random.uniform(0.5, 1.5)
        self.color = (1, 1, 0)
        self.direction = 1
        self.trail_length = 5
        self.trail = []

    def update(self):
        self.trail.append((self.x, self.y))
        if len(self.trail) > self.trail_length:
            self.trail.pop(0)
        self.x += self.direction * self.speed
        self.y -= random.uniform(-0.5, 0.5)
        if self.x > screen.window_width() / 2:
            self.x = random.uniform(-screen.window_width() / 2, screen.window_width() / 2)
            self.y = random.uniform(screen.window_height() / 2, screen.window_height() / 2 + 100)
            self.trail = []

    def draw(self, pen):
        pen.penup()
        pen.goto(self.x, self.y)
        pen.pendown()
        pen.fillcolor(self.color_to_string(self.color))
        pen.begin_fill()
        for _ in range(5):
            pen.forward(self.size)
            pen.right(144)
        pen.end_fill()
        pen.penup()
        pen.color(self.color)
        pen.width(self.size / 10)
        for pos in self.trail:
            pen.goto(pos)
            pen.pendown()
            pen.dot()

    def color_to_string(self, color):
        r = int(color[0] * 255)
        g = int(color[1] * 255)
        b = int(color[2] * 255)
        return "#{:02x}{:02x}{:02x}".format(r, g, b)


stars = []
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

for _ in range(30):
    stars.append(Star())
    stars[-1].draw(pen)

def update():
    screen.update()
    for star in stars:
        star.update()
    for star in stars:
        if star.y < -screen.window_height() / 2:
            stars.remove(star)
            del star
    if random.random() < 0.05:
        stars.append(Star())
    pen.clear()
    for star in stars:
        star.draw(pen)
    screen.ontimer(update, 16)

screen.listen()
update()
screen.mainloop()
