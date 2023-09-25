#funcao menu do jogo
import random
import time

def jogoP():
    #desenho das maos  0 = PEDRA  \\ 1 = PAPEL \\  2 = TESOURA
    desenho =["---'   ____)\n      (_____)\n      (_____)\n      (____)\n---.__(___)","    _______\n---'   ____)____\n          ______)\n          _______)\n         _______)\n---.__________)","    _______\n---'   ____)____\n          ______)\n       __________)\n      (____)\n---.__(___)"]
    # o utilizador escolhe a mao
    while True:
        opcao=int(input("Escolha uma opcão:1 = Pedra, 2 = Papel, 3 = Tesoura\n"))
        if opcao in range(1, 4):
            opcao=opcao-1
            break
        else:
            print("Opção errada. Escolha novamente\n")

    for i in desenho: # faz o print das 3 maos
        print(i)
        time.sleep(1) # faz pausa no programa de 1 segundo
    
    escolhaC = int((random.randrange(0,3)))  #sorteia a mao escolhida pela computador
    print("====================================================")
    time.sleep(1)
    # faz a comparacao das maos jogadas e define quem ganha,perde,empata
    if opcao== escolhaC:
        print("Empate")
    elif escolhaC == 0 and opcao==1:  
        print ("O Jogador ganhou")
    elif escolhaC == 0 and opcao==2:
        print("O Computador ganhou")
    elif escolhaC == 1 and opcao==0:
        print("O Computador ganhou")
    elif escolhaC == 1 and opcao==2:
        print("O Jogador ganhou")
    elif escolhaC == 2 and opcao==0:
        print("O Jogador ganhou")
    elif escolhaC == 2 and opcao==1:
        print("O Computador ganhou")
    else:
        print("\n Escolha não válida.\n Tente outra vez.")
    
    print(f"O Computador escolheu \n{desenho[escolhaC]}\n\ne o jogador \n{desenho[opcao]}") #imprime o desenho da mao

#Funcao que inicia o jogo \\ menu do jogo
def menu():
    print("====================================================")
    print("                      ---------                     ")
    print("               Pedra, Papel, Tesoura                ")
    print("====================================================")
    menu1=1
    while menu1!=0:
        menu1=int(input("Começar novo jogo? 1-Sim \\ 0-Menu inicial\n"))
        if menu1==0:
            print("A sair...")
            time.sleep(0.5)
        elif menu1==1:
            jogoP()
        else:
            print("Insira uma opção válida")

