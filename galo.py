import time #importa a biblioteca

#dicionario com todas as posicoes no jogo com valores vazios
posicoes = {
    '1': '',
    '2': '',
    '3': '',
    '4': '',
    '5': '',
    '6': '',
    '7': '',
    '8': '',
    '9': ''
}

#imprime o galo e chama start
def menu():
    print('-=-'*16)
    print("                            ~-.")
    print("          ,,,;            ~-.~-.~-")
    print("         (.../           ~-.~-.~-.~-.~-.")
    print("         } o~`,         ~-.~-.~-.~-.~-.~-.")
    print("         (/    \      ~-.~-.~-.~-.~-.~-.~-.")
    print("          ;    \    ~-.~-.~-.~-.~-.~-.~-.")
    print("         ;     {_.~-.~-.~-.~-.~-.~-.~")
    print("        ;:  .-~`    ~-.~-.~-.~-.~-.")
    print("       ;.: :'    ._   ~-.~-.~-.~-.~-")
    print("        ;::`-.    '-._  ~-.~-.~-.~-")
    print("         ;::. `-.    '-,~-.~-.~-.")
    print("          ';::::.`''-.-'")
    print("            ';::;;:,:'")
    print("               '||\"")
    print("               / |")
    print("             ~` ~\"'")
    print("Bem vindo ao jogo do galo")
    print('-=-'*16)
    start()

#funcao para comecar novo jogo ou sair
def start(): 
    while 1:
        char = input("Começar Novo Jogo? S=Sim N=Não\n").upper()
        if char.isalpha() == True and char == "S":
            for x in range(1,10):
                posicoes[str(x)] = x
            jogo()
        elif char.isalpha() == True and char == "N":
            print("O jogo vai terminar")
            break
        else:
            print("Insira uma opção válida")

#funcao que controla o jogo
def jogo():
    mostra_tabuleiro()
    while True:
        print('-=-'*15)
        while True:
            opcao1 = input("Jogador 1 qual vai ser a sua escolha?")
            if opcao1.isnumeric():
                if valida_jogada(opcao1, "X") == True:
                    break
            else:
                print("Opção invalida")    
        print('-=-'*15)
        mostra_tabuleiro()
        if verifica_vencedor() == True:
            time.sleep(1)
            print("====================================================")
            print("                      ---------                     ")
            print("               O jogador 1 VENCEU!!!                ")
            print("====================================================")
            break
        elif verifica_vencedor() == 'empate':
            print("====================================================")
            print("                      ---------                     ")
            print("                      EMPATE!!!                     ")
            print("====================================================")
            break
        print('-=-'*15)
        while True:
            opcao2 = input("Jogador 2 qual vai ser a sua escolha?")
            if opcao2.isdigit():
                if valida_jogada(opcao2, "O") == True:
                    break
            else:
                print("Opção invalida")    
        print('-=-'*15)
        mostra_tabuleiro()
        if verifica_vencedor() == True:
            time.sleep(1)
            print("====================================================")
            print("                      ---------                     ")
            print("               O jogador 2 VENCEU!!!                ")
            print("====================================================")
            break
        elif verifica_vencedor() == 'empate':
            print("====================================================")
            print("                      ---------                     ")
            print("                      EMPATE!!!                     ")
            print("====================================================")
            break

# imprime o tabuleireiro
def mostra_tabuleiro():
    print('       |       |       ')
    print(f'  {posicoes["1"]}    |   {posicoes["2"]}   |   {posicoes["3"]}   ')
    print('       |       |       ')
    print('-------|-------|-------')
    print('       |       |       ')
    print(f'  {posicoes["4"]}    |   {posicoes["5"]}   |   {posicoes["6"]}   ')
    print('       |       |       ')
    print('-------|-------|-------')
    print('       |       |       ')
    print(f'  {posicoes["7"]}    |   {posicoes["8"]}   |   {posicoes["9"]}   ')
    print('       |       |       ')

#verifica se a jogada e possivel e coloca no tabuleireiro
def valida_jogada(opcao, simbolo): 
    if 1<=int(opcao)<=9:
        if posicoes.get(opcao) != "X" and posicoes.get(opcao) != "O":
            posicoes[opcao] = str(simbolo)
            return True
        else:
            print("Posicao ocupada jogue novamente")
            return False
    else:
        print("Opção invalida")

# funcao que verifica as possibilidades  e trona o resultado 
def verifica_vencedor(): 
    if (posicoes["1"] == "X" and posicoes["2"] == "X" and posicoes["3"] == "X") or (posicoes["1"] == 'O' and posicoes["2"] == 'O' and posicoes["3"] == 'O'):
        return True
    elif (posicoes["4"] == "X" and posicoes["5"] == "X" and posicoes["6"] == "X") or (posicoes["4"] == 'O'and posicoes["5"] == 'O' and posicoes["6"] == 'O'):
        return True
    elif (posicoes["7"] == "X" and posicoes["8"] == "X" and posicoes["9"] == "X") or (posicoes["7"] == 'O'  and posicoes["8"] == 'O' and posicoes["9"] == 'O'):
        return True
    elif (posicoes["1"] == "X" and posicoes["4"] == "X" and posicoes["7"] == "X") or (posicoes["1"] == 'O'  and posicoes["4"] == 'O'  and posicoes["7"] == 'O'):
        return True
    elif (posicoes["2"] == "X" and posicoes["5"] == "X" and posicoes["8"] == "X") or (posicoes["2"] == 'O'  and posicoes["5"] == 'O'  and posicoes["8"] == 'O'):
        return True
    elif (posicoes["3"] == "X" and posicoes["6"] == "X" and posicoes["9"] == "X") or (posicoes["3"] == 'O'  and posicoes["6"] == 'O'  and posicoes["9"] == 'O'):
        return True
    elif (posicoes["1"] == "X" and posicoes["5"] == "X" and posicoes["9"] == "X") or (posicoes["1"] == 'O'  and posicoes["5"] == 'O'  and posicoes["9"] == 'O'):
        return True
    elif (posicoes["3"] == "X" and posicoes["5"] == "X" and posicoes["7"] == "X") or (posicoes["3"] == 'O'  and posicoes["5"] == 'O'  and posicoes["7"] == 'O'):
        return True
    elif (posicoes["1"] == "X" or posicoes["1"] == 'O') and (posicoes["2"] == "X" or posicoes["2"] == 'O') and (posicoes["3"] == "X" or posicoes["3"] == 'O') and (posicoes["4"] == "X" or posicoes["4"] == 'O') and (posicoes["5"] == "X" or posicoes["5"] == 'O') and (posicoes["6"] == "X" or posicoes["6"] == 'O') and (posicoes["7"] == "X" or posicoes["7"] == 'O') and (posicoes["8"] == "X" or posicoes["8"] == 'O') and( posicoes["9"] == "X" or posicoes["9"] == 'O'):
        return 'empate'
    


