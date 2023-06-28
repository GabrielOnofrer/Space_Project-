import pygame
from tkinter import simpledialog
import json
import os

pygame.init()
tamanho = (800, 500)
branco = (255, 255, 255)
preto = (0, 0, 0)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Projeto Space")
fonte = pygame.font.Font(None, 20)
texto_salvar = fonte.render("F10 para salvar", True, branco)
texto_carregar = fonte.render("F11 para carregar", True, branco)
texto_limpar = fonte.render("F12 para limpar", True, branco)
running = True
icone = pygame.image.load("space.png")
pygame.display.set_icon(icone)
fundo = pygame.image.load("bg.jpg")
pygame.display.set_icon(icone)
pygame.mixer.music.load("Space_Machine_Power.mp3")
pygame.mixer.music.play(-1)
circles = []
lines = []
estrelas = {}

def salvar_dados():
    with open("dados.json", "w") as file:
        json.dump(estrelas, file)

def carregar_dados():
    global estrelas
    estrelas.clear()
    circles.clear()
    lines.clear()
    if os.path.isfile("dados.json") and os.path.getsize("dados.json") > 0:
        with open("dados.json", "r") as file:
            estrelas = json.load(file)

def limpar_dados():
    global estrelas
    estrelas.clear()
    circles.clear()
    lines.clear()
    if os.path.isfile("dados.json"):
        os.remove("dados.json")

carregar_dados()

while running:
    tela.blit(fundo, (0, 0))
    tela.blit(texto_salvar, (10, 10))
    tela.blit(texto_carregar, (10, 30))
    tela.blit(texto_limpar, (10, 50))
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
        text = font.render(item, True, branco)
        tela.blit(text, (x + 25, y - 10))

    if len(circles) >= 2:
        lines = [(circles[i][:2], circles[i+1][:2]) for i in range(len(circles) - 1)]

    for line in lines:
        pygame.draw.line(tela, branco, line[0], line[1], 2)

    pygame.display.update()
    clock.tick(40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_F10]:
        salvar_dados()
    elif keys[pygame.K_F11]:
        carregar_dados()
        for item, (x, y) in estrelas.items():
            circles.append((x, y, item))
    elif keys[pygame.K_F12]:
        limpar_dados()

pygame.quit()
