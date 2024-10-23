
import pygame #importa a biblioteca pygame para o script


# pygame configuração
pygame.init() #inicialização do pygame
pygame.font.init() #inicialização do pacote de fontes no pygame

screen = pygame.display.set_mode((600, 600)) #definição do tamanho da tela
pygame.display.set_caption('Jogo da Velha') #nome da janela do jogo
clock = pygame.time.Clock() #biblioteca de tempo

fonte_quadrinhos = pygame.font.SysFont('Comic Sans Ms', 100, True, True) #importar fonte
running = True #variável de controle do status do jogo

personagem_x = fonte_quadrinhos.render('X', True, 'red')
personagem_y = fonte_quadrinhos.render('O', True, 'red')
apresenta_personagem = 0
x = 0
y = 0

while running:
    # controle de enventos no jgo
    for event in pygame.event.get():
        # pygame.QUIT significa que quando usuário clicar em X a tela fechará
        if event.type == pygame.QUIT:
            running = False
        # pygame.MOUSEBUTTONDOWN significa evento de click do mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('Clicou')
            click_pos = pygame.mouse.get_pos() #a posiçao do mouse quando houver evento de clique
            print('eixo x:', click_pos[0])
            print('eixo y:', click_pos[1])
            x = click_pos[0]
            y = click_pos[1]
            apresenta_personagem = apresenta_personagem + 1
            if(apresenta_personagem >= 10):
                screen.fill('black')
                apresenta_personagem = 0
    
    #Desenha tabuleiro
    #                                 origem      destino    
    #                                ( x , y)   ( x , y ) 
    pygame.draw.line(screen, 'blue',(200, 0), (200, 600), 10)
    pygame.draw.line(screen, 'blue',(400, 0), (400, 600), 10)
    pygame.draw.line(screen, 'blue',(0, 200), (600, 200), 10)
    pygame.draw.line(screen, 'blue',(0, 400), (600, 400), 10)

    # primeira linha 
    #                          x  y
    if  x > 0 and x < 200 and y < 200:
        screen.blit(personagem_x,(60,30)) #primeiro
    elif x >= 200 and x < 400 and y <200:
        screen.blit(personagem_y,(260,30)) #segundo
    elif x >= 400 and y < 200:
        screen.blit(personagem_y,(460,30)) #terceiro

    # segunda linha 
    #                          x  y
    if x < 200 and y >= 200 and y < 400:
        screen.blit(personagem_x,(60,230)) #quarto
    elif x >= 200 and x < 400 and y >= 200 and y < 400:
        screen.blit(personagem_y,(260,230)) #quinto
    elif x >= 400 and y >= 200 and y < 400:
        screen.blit(personagem_y,(460,230)) #sexto

    # terceira linha 
    #                          x  y
    if x < 200 and y >= 400 :
        screen.blit(personagem_x,(60,430)) #setimo
    elif x >= 200 and x < 400 and y >= 400:
        screen.blit(personagem_y,(260,430)) #oitava
    elif x >= 400 and y >+ 400:
        screen.blit(personagem_y,(460,430)) #nono
    

    # flip() o display para atualizar a página
    pygame.display.flip()

    clock.tick(60)  # limita o fps para 60

pygame.quit()