import pygame
from tkinter import simpledialog

pygame.init()
tamanho = (800, 500)
branco = (255, 255, 255)
preto = (0, 0, 0)
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
estrelas = {}

while running:
    tela.blit(fundo, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space", "Nome da Estrela")
            if item is None or item.strip() == "":
                item = "desconhecido" + str((x, y))
            circles.append((x, y, item))
            estrelas[item] = (x, y)
            print(item)

    for circle in circles:
        x, y, item = circle
        pygame.draw.circle(tela, branco, (x, y), 20)
        font = pygame.font.Font(None, 20)
        text = font.render(item, True, preto)
        tela.blit(text, (x + 25, y - 10))

    if len(circles) >= 2:
        lines = [(circles[i][:2], circles[i+1][:2]) for i in range(len(circles) - 1)]

    for line in lines:
        pygame.draw.line(tela, branco, line[0], line[1], 2)

    pygame.display.update()
    clock.tick(40)

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_F10]:
        
        with open("dados.txt", "w") as file:
            file.write("Estrelas:\n")
            for estrela, coordenadas in estrelas.items():
                file.write(f"Nome: {estrela}, Coordenadas: {coordenadas}\n")

pygame.quit()
