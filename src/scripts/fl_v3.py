import random
import turtle

# Configuração da tela
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Moving Stars")
screen.tracer(0)  # Desativa a animação para desenho mais rápido

# Classe Star
class Star:
    def __init__(self):
        self.x = random.uniform(-200, 200)  # Ajusta para o tamanho da tela
        self.y = random.uniform(-200, 200)  # Ajusta para o tamanho da tela
        self.speed = random.uniform(0.5, 2)  # Ajusta a faixa de velocidade
        self.size = random.randint(10, 20)  # Ajusta o tamanho da estrela
        self.brightness = random.uniform(0.5, 1.5)  # Ajusta o brilho
        self.color = (1, 1, 0)  # Cor amarela
        self.rotation = random.randint(-5, 5)  # Rotação aleatória
        self.direction = 1  # Movimento para a direita
        self.trail_length = 5  # Comprimento do rastro
        self.trail = []  # Lista para armazenar as posições anteriores

    def update(self):
        self.trail.append((self.x, self.y))  # Adiciona a posição atual à lista de trilha
        if len(self.trail) > self.trail_length:  # Remove a posição mais antiga se a trilha for muito longa
            self.trail.pop(0)
        self.x += self.direction * self.speed  # Movimento horizontal
        self.y -= random.uniform(-0.5, 0.5)  # Simula turbulência
        # Envolve na tela
        if self.x > screen.window_width() / 2:
            self.reset_star()

    def reset_star(self):
        self.x = random.uniform(-200, 200)  # Ajusta para o tamanho da tela
        self.y = random.uniform(screen.window_height() / 2, screen.window_height() / 2 + 100)  # Ajusta para o tamanho da tela
        self.speed = random.uniform(0.5, 2)  # Ajusta a faixa de velocidade
        self.size = random.randint(10, 20)  # Ajusta o tamanho da estrela
        self.brightness = random.uniform(0.5, 1.5)  # Ajusta o brilho
        self.color = (1, 1, 0)  # Cor amarela
        self.rotation = random.randint(-5, 5)  # Rotação aleatória
        self.direction = 1  # Movimento para a direita
        self.trail = []  # Reinicia a trilha ao reiniciar a estrela

    def draw(self, pen):
        pen.penup()
        pen.goto(self.x, self.y)
        pen.pendown()
        pen.fillcolor(self.color_to_string(self.color))
        pen.begin_fill()
        # Desenha uma estrela
        for _ in range(5):
            pen.forward(self.size)
            pen.right(144)
        pen.end_fill()
        self.draw_trail(pen)

    def draw_trail(self, pen):
        pen.penup()
        pen.color(self.color)  # Define a cor do rastro para a mesma cor da estrela
        pen.width(self.size / 10)  # Define a largura do rastro proporcional ao tamanho da estrela
        for pos in self.trail:
            pen.goto(pos)
            pen.pendown()
            pen.dot()

    def color_to_string(self, color):
        r = int(color[0] * 255)
        g = int(color[1] * 255)
        b = int(color[2] * 255)
        return "#{:02x}{:02x}{:02x}".format(r, g, b)


# Cria as estrelas e a caneta
stars = []
pen = turtle.Turtle()
pen.speed(0)  # Define a velocidade de desenho como a mais rápida
pen.hideturtle()  # Esconde a tartaruga

# Cria e desenha as estrelas
for _ in range(30):
    stars.append(Star())
    stars[-1].draw(pen)

# Atualiza e redesenha as estrelas
def update():
    screen.update()  # Atualiza a tela

    for star in stars:
        star.update()

    # Limpa as estrelas que saíram da tela
    for star in stars:
        if star.y < -screen.window_height() / 2:
            stars.remove(star)
            del star

    # Adiciona novas estrelas cadentes
    if random.random() < 0.05:  # Ajuste esse valor para controlar a frequência de estrelas cadentes
        stars.append(Star())

    pen.clear()  # Limpa as estrelas anteriores
    for star in stars:
        star.draw(pen)

    screen.ontimer(update, 16)  # Chama a atualização a cada 16 milissegundos (ajusta para a velocidade da animação)

screen.listen()
update()  # Inicia a animação
screen.mainloop()
