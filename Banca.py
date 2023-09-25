import random 
import time

#funcao menu do jogo
def menu():
    print("=====================================================")
    print("                       ---------                     ")
    print("                    Banca Francesa                   ")
    print("                  .-------.    ______")
    print("                 /   o   /|   /\     \\")
    print("                /_______/o|  /o \  o  \\")
    print("                | o     | | /   o\_____\\")
    print("                |   o   |o/ \o   /o    /")
    print("                |     o |/   \ o/  o  /")
    print("                '-------'     \/____o/")
    print("=====================================================")
    print("Bem vindo à Banca Francesa\n")
    print("----------------------------------------Regras----------------------------------------")
    print("Para sair grande a soma das pintas dos dados dados tem que ser 14,15 ou 16")
    print("Para sair pequeno a soma das pintas dos dados dados tem que ser 5,6 ou 7")
    print("Para sair ases a soma das pintas dos dados dados tem que ser 3")
    while 1:
        if input("Começar Novo Jogo? S=Sim N=Não\n").upper() == "S":
            jogo()
        else:
            break
             
#comeco do jogo - gere todas as outras funcoes
def jogo():
    aposta = input("Qual vai ser a sua aposta? grande, pequeno, ases\n")
    resultado = False
    while resultado == False:
        dadoSort=lancamentoDado()
        print(f"O soma dos dados é : {dadoSort[1]}")
        resultado = verifica_resultado(dadoSort[1])
    if resultado == aposta:
        print(f"Saíu : {resultado}")
        print("====================================================")
        print("                      ---------                     ")
        print("                       Ganhou!                      ")
        print("====================================================")
    else:
        print(f"Saíu : {resultado}")
        print("====================================================")
        print("                      ---------                     ")
        print("                       Perdeu!                      ")
        print("====================================================")
        
#sorteio dos dados
def lancamentoDado():
    soma=0
    dado=[]
    dadoG=[" _______\n|       |\n|   o   |\n|       |\n'-------'"," _______\n| o     |\n|       |\n|     o |\n'-------'"," _______\n| o     |\n|   o   |\n|     o |\n'-------'"," _______\n| o   o |\n|       |\n| o   o |\n'-------'"," _______\n| o   o |\n|   o   |\n| o   o |\n'-------'"," _______\n| o   o |\n| o   o |\n| o   o |\n'-------'"]
    for x in range(3):
        escolha=int(random.choice(range(1,6)))
        dado.append(escolha)
        soma+=dado[x]
        print(dadoG[escolha-1])
        time.sleep(1)
    return dado,soma

#verifica os resultados
def verifica_resultado(soma):
    if soma in range(14,17):
        return "grande"
    elif soma in range(5,8):
        return "pequeno"
    elif soma == 3:
        return "ases"
    else:
        return False
