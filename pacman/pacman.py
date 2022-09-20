import pygame
amarelo = (255,255,0)
preto = (0,0,0)
raio = 30
pygame.init()
tela = pygame.display.set_mode((640, 480), 0)
x = 10
y = 10
velocidade = 0.1
vel_x = velocidade
vel_y = velocidade

while True:

    x = x + vel_x
    y = y + vel_y

    if x + raio > 640:
        vel_x = -velocidade
    if x - raio < 0:
        vel_x = velocidade
    if y + raio > 480:
        vel_y = -velocidade
    if y - raio < 0:
        vel_y = velocidade

    tela.fill(preto)
    pygame.draw.circle(tela, amarelo, (int(x), int(y)), raio, 0)
    pygame.display.update()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
