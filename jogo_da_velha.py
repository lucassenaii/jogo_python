
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

q1 =''
q2 =''
q3 =''
q4 =''
q5 =''
q6 =''
q7 =''
q8 =''
q9 ='' 

def desenha_tabuleiro(espessura, cor):
    #Desenha tabuleiro
    #                                  origem      destino    
    #                                ( x , y)   ( x , y ) 
    pygame.draw.line(screen, cor ,(200, 0), (200, 600), espessura)
    pygame.draw.line(screen, cor ,(400, 0), (400, 600), espessura)
    pygame.draw.line(screen, cor ,(0, 200), (600, 200), espessura)
    pygame.draw.line(screen, cor ,(0, 400), (600, 400), espessura)

def faz_jogada():
    global q1, q2 , q3 , q4 , q5 , q6 , q7 , q8 , q9
    status = True
    if q1 == '' and coordenada_x > 0 and coordenada_x < 200 and coordenada_y< 200:
        screen.blit(jogador_atual,(60,30))  #primeiro
        q1 = jogador_atual
    elif q2 == '' and coordenada_x >= 200 and coordenada_x < 400 and coordenada_y< 200:
        screen.blit(jogador_atual,(260,30)) #segundo
        q2 = jogador_atual
    elif q3 == '' and coordenada_x >= 400 and coordenada_y< 200:
        screen.blit(jogador_atual,(460,30)) #terceiro
        q3 = jogador_atual
    elif q4 == '' and coordenada_x < 200 and coordenada_y>= 200 and coordenada_y< 400:
        screen.blit(jogador_atual,(60,230))  #quarto
        q4 = jogador_atual
    elif q5 == '' and coordenada_x >= 200 and coordenada_x < 400 and coordenada_y>= 200 and coordenada_y< 400:
        screen.blit(jogador_atual,(260,230)) #quinto
        q5  = jogador_atual
    elif q6 == '' and coordenada_x >= 400 and coordenada_y>= 200 and coordenada_y< 400:
        screen.blit(jogador_atual,(460,230)) #secoordenada_xto
        q6 = jogador_atual
    elif q7 == '' and coordenada_x < 200 and coordenada_y>= 400:
        screen.blit(jogador_atual,(60,430))  #setimo
        q7 = jogador_atual
    elif q8 == '' and coordenada_x >= 200 and coordenada_x < 400 and coordenada_y>= 400:
        screen.blit(jogador_atual,(260,430)) #oitavo
        q8 = jogador_atual
    elif q9 == '' and coordenada_x >= 400 and coordenada_y>= 400:
        screen.blit(jogador_atual,(460,430)) #nono
        q9 = jogador_atual
    else:
        status = False
    
    return status
def check_vencedor():
    status = False
    # linhas
    if q1 == q2 == q3 !='':
        pygame.draw.line(screen, 'orange' ,(50, 100), (550, 100), 10)
        status = True
    elif q4 == q5 == q6!='':
        pygame.draw.line(screen, 'orange' ,(50, 300), (550, 300), 10)
        status = True
    elif q7 == q8 == q9!='':
        pygame.draw.line(screen, 'orange' ,(50, 500), (550, 500), 10)
        status = True
    # colunas
    elif q1 == q4 == q7!='':
        pygame.draw.line(screen, 'orange' ,(100, 50), (100, 600), 10)
        status = True
    elif q2  == q5 == q8!='':
        pygame.draw.line(screen, 'orange' ,(300, 100), (600, 600), 10)
        status = True
    elif q3 == q6 == q9!='':
       status = True
    #diagonais
    elif q1 == q5 == q9!='':
        pygame.draw.line(screen, 'orange' ,(50, 100), (550, 500), 10)
        status = True
    elif q3 == q5 == q7!='':
        status = True
    
    return status
    

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
            if(rodadas >= 9):
                screen.fill('black') 
                rodadas = 0
                coordenada_x = 0
                coordenada_y = 0
                jogador_atual = personagem_x
                tabuleiro_desenhado = False
                break
            if(faz_jogada()):
                rodadas = rodadas + 1
                if jogador_atual == personagem_x:
                    jogador_atual = personagem_o
                else:
                    jogador_atual = personagem_x
                if(check_vencedor()):
                    rodadas = 9 

           
    if tabuleiro_desenhado == False:
        desenha_tabuleiro(10, 'purple')
        q1 =''
        q2 =''
        q3 =''
        q4 =''
        q5 =''
        q6 =''
        q7 =''
        q8 =''
        q9 ='' 
        tabuleiro_desenhado = True
   
    

    # flip() o display para atualizar a página
    pygame.display.flip()
    clock.tick(60)  # limita o fps para 60

pygame.quit()