# importando bibliotecas
import pygame
import os

# inicia os modulos (Teclado, video e etc)
pygame.init()

# configuracoes da janela
window = pygame.display.set_mode((800,711))
pygame.display.set_caption("jogo da velha")
screen = pygame.display.get_surface()

# Carregando imagen do background
tabela = os.path.join(".","tabela_2.png")
fundo = pygame.image.load(tabela)

# Carregando imagen do X
img_x = os.path.join(".","X_2.png")
img_x_loaded = pygame.image.load(img_x)

# Carregando imagen do Y
img_y = os.path.join(".","O_2.png")
img_y_loaded = pygame.image.load(img_y)

# Carregando imagen do A
img_a = os.path.join(".","A_2.png")
img_a_loaded = pygame.image.load(img_a)

########################
# CORDENADAS DOS SLOTS #
########################
# (35, 21) #
# (35,255) #
# (35,490) #
########################

# Cordenadas para adicionar sprite
posicoes=[(35,24),(298,24),(562,24),
          (35,255),(295,255),(562,255),
          (35,490),(295,490),(562,490)]

# Cordenadas para salvar posicao das jogadas
tabela=[0,0,0,
        0,0,0,
        0,0,0]

# desenha na tela
screen.blit(fundo,(0,0))
screen.blit(img_x_loaded,(35,21))
screen.blit(img_y_loaded,(35,255))
screen.blit(img_a_loaded,(35,490))
pygame.display.update()

# Posicao atual do ponteiro
posi=7

# Padroniza velocidade do jogo em relacao a outros computadores
clock = pygame.time.Clock()
clock.tick(60)

# Variaveis booleanas
running = True
vez = True

# Variaveis inteiras
quant_zero = 0

# Capturar botoes
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            pygame.event.pump()
            key = pygame.key.get_pressed()

            # Seta para cima
            if (key[pygame.K_UP]):
                if(posi<4):
                    posi=posi+6
                else:
                    posi=posi-3

            # Seta para baixo
            elif (key[pygame.K_DOWN]):
                if(posi>6):
                    posi=posi-6
                else:
                    posi=posi+3

            # Seta para esquerda
            elif (key[pygame.K_LEFT]):
                if(posi>1):
                    posi=posi-1
                else:
                    posi=9

			# Seta para direita
            elif (key[pygame.K_RIGHT]):
                if(posi<9):
                    posi=posi+1
                else:
                    posi=1

			# Limpar tela
            elif (key[pygame.K_r]):
                         #1.2.3.4.5.6.7.8.9
				tabela = [0,0,0,0,0,0,0,0,0]
				print('reset')
		    # Funcao para fazer a jogada
            elif (key[pygame.K_e]):
                if(tabela[posi-1]==0):
                    if(vez):
                        tabela[posi-1] = 1
                        # DEBUG print ("X Atirou na posicao", posi-1)
                    else:
                        tabela[posi-1] = -1
                        # DEBUG print ("O Atirou na posicao", posi-1)

                    vez = not vez

    # IDENTIFICAR EM TABELA 0 , 1 , 2 - HORIZONTAL
    if (tabela[0] == 1 and tabela[1] == 1 and tabela[2] == 1):
            print ("X ganhou")
    if (tabela[0] == -1 and tabela[1] == -1 and tabela[2] == -1):
            print ("O ganhou")

    # IDENTIFICAR EM TABELA 3 , 4 , 5 - HORIZONTAL
    if (tabela[3] == 1 and tabela[4] == 1 and tabela[5] == 1):
            print ("X ganhou")
    if (tabela[3] == -1 and tabela[4] == -1 and tabela[5] == -1):
            print ("O ganhou")

    # IDENTIFICAR EM TABELA 6 , 7 , 8 - HORIZONTAL
    if (tabela[6] == 1 and tabela[7] == 1 and tabela[7] == 1):
            print ("X ganhou")
    if (tabela[6] == -1 and tabela[7] == -1 and tabela[7] == -1):
            print ("O ganhou")

    # IDENTIFICAR EM TABELA 0 , 3 , 6 - VERTICAL
    if (tabela[0] == 1 and tabela[3] == 1 and tabela[6] == 1):
            print ("X ganhou")
    if (tabela[0] == -1 and tabela[3] == -1 and tabela[2] == -1):
            print ("O ganhou")

    # IDENTIFICAR EM TABELA 1 , 4 , 7 - VERTICAL
    if (tabela[0] == 1 and tabela[3] == 1 and tabela[6] == 1):
            print ("X ganhou")
    if (tabela[0] == -1 and tabela[3] == -1 and tabela[6] == -1):
            print ("O ganhou")

    # IDENTIFICAR EM TABELA 2 , 5 , 8 - VERTICAL
    if (tabela[0] == 1 and tabela[3] == 1 and tabela[6] == 1):
            print ("X ganhou")
    if (tabela[0] == -1 and tabela[3] == -1 and tabela[6] == -1):
            print ("O ganhou")

    screen.blit(fundo,(0,0))
    for posicao, elemento in enumerate(tabela):
        if(elemento!=0):
            quant_zero = quant_zero + 1
        if (quant_zero == 9):
            print ("empate")
        if(elemento==-1):
            screen.blit(img_y_loaded,posicoes[posicao])
        elif(elemento==1):
            screen.blit(img_x_loaded,posicoes[posicao])
    quant_zero = 0
    # DEBUG print('Posicao',posi)
    screen.blit(img_a_loaded,posicoes[posi-1])
    pygame.display.update()
