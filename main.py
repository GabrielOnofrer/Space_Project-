import pygame
pygame.init()
tamanho = (800,500)
branco = (255,255,255)
clock = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho )
pygame.display.set_caption("Projeto Space")
running = True
icone = pygame.image.load("space.png")
fundo = pygame.image.load("bg.jpg")
pygame.display.set_icon( icone )
pygame.mixer.music.load("Space_Machine_Power.mp3")
pygame.mixer.music.play(-1)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        

        



    
    
    tela.blit(fundo, (0,0))




    pygame.display.update()
    clock.tick(40)
    

pygame.quit()
