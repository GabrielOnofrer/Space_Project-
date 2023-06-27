import pygame
from tkinter import simpledialog

pygame.init()
tamanho = (800, 500)
branco = (255, 255, 255)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Projeto Space")

running = True
icone = pygame.image.load("space.png")
fundo = pygame.image.load("bg.jpg")
pygame.display.set_icon(icone)
pygame.mixer.music.load("Space_Machine_Power.mp3")
pygame.mixer.music.play(-1)
circles = []
lines = []

while running:
    tela.blit(fundo, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            circles.append((x, y))
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space", "Nome da Estrela")
            if item is None or item.strip() == "":
                item = "desconhecido" + str(pos)
            print(item)

    for circle in circles:
        pygame.draw.circle(tela, branco, circle, 20)

    if len(circles) >= 2:
        lines = list(zip(circles[:-1], circles[1:]))  # Cria uma lista de pares de coordenadas consecutivas

    for line in lines:
        pygame.draw.line(tela, branco, line[0], line[1], 2)

    pygame.display.update()
    clock.tick(40)

pygame.quit()
