
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
personagem_o = fonte_quadrinhos.render('O', True, 'red')

jogador_atual = personagem_x #inicializa o jogo com o X

rodadas = 0
tabuleiro_desenhado = False
coordenada_x = 0
coordenada_y = 0

def desenha_tabuleiro(espessura, cor):
    #Desenha tabuleiro
    #                                  origem      destino    
    #                                ( x , y)   ( x , y ) 
    pygame.draw.line(screen, cor ,(200, 0), (200, 600), espessura)
    pygame.draw.line(screen, cor ,(400, 0), (400, 600), espessura)
    pygame.draw.line(screen, cor ,(0, 200), (600, 200), espessura)
    pygame.draw.line(screen, cor ,(0, 400), (600, 400), espessura)

def faz_jogada():
    if coordenada_x > 0 and coordenada_x < 200 and coordenada_y< 200:
        screen.blit(jogador_atual,(60,30))  #primeiro

    elif coordenada_x >= 200 and coordenada_x < 400 and coordenada_y< 200:
        screen.blit(jogador_atual,(260,30)) #segundo
    
    elif coordenada_x >= 400 and coordenada_y< 200:
        screen.blit(jogador_atual,(460,30)) #terceiro
    
    elif coordenada_x < 200 and coordenada_y>= 200 and coordenada_y< 400:
        screen.blit(jogador_atual,(60,230))  #quarto
    
    elif coordenada_x >= 200 and coordenada_x < 400 and coordenada_y>= 200 and coordenada_y< 400:
        screen.blit(jogador_atual,(260,230)) #quinto
    
    elif coordenada_x >= 400 and coordenada_y>= 200 and coordenada_y< 400:
        screen.blit(jogador_atual,(460,230)) #secoordenada_xto
    
    elif coordenada_x < 200 and coordenada_y>= 400:
        screen.blit(jogador_atual,(60,430))  #setimo
    
    elif coordenada_x >= 200 and coordenada_x < 400 and coordenada_y>= 400:
        screen.blit(jogador_atual,(260,430)) #oitavo
    
    elif coordenada_x >= 400 and coordenada_y>= 400:
        screen.blit(jogador_atual,(460,430)) #nono

def verificar_vencedor():
    combinaçao =[() () () #linhas
                 () () () #colunas
                 () () ()] #diagonais
    for a , b and c in combinaçao:
        if self.tabuleiro[a] == self.tabuleiro[b] == self.tabuleiro[c] != "":
            return True

    return False        

while running:
    # controle de enventos no jgo
    for event in pygame.event.get():
        # pygame.QUIT significa que quando usuário clicar em X a tela fechará
        if event.type == pygame.QUIT:
            running = False
        # pygame.MOUSEBUTTONDOWN significa evento de click do mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('Clicou')
            click_pos = pygame.mouse.get_pos() # a posição do mouse quando houve o evento de click
            print('eixo X:', click_pos[0])
            print('eixo Y:', click_pos[1])
            coordenada_x = click_pos[0]
            coordenada_y = click_pos[1]
            rodadas = rodadas + 1
            if rodadas >= 10:
                screen.fill('black') 
                rodadas = 0
                coordenada_x = 0
                coordenada_y = 0
                tabuleiro_desenhado = False
            if rodadas != 1:
                if jogador_atual == personagem_x:
                    jogador_atual = personagem_o
                else:
                    jogador_atual = personagem_x
            else:
                jogador_atual = personagem_x

            faz_jogada()

    if tabuleiro_desenhado == False:
        desenha_tabuleiro(10, 'purple')
        tabuleiro_desenhado = True
   
    

    # flip() o display para atualizar a página
    pygame.display.flip()

    clock.tick(60)  # limita o fps para 60

pygame.quit()