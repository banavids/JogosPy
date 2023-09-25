import time, os  #importa as bibliotecas e os ficheiros externos
import galo, Banca, Pedra #import dos ficheiros externos que estao na mesma pasta do ficheiro menu.py

#ficheiro principal
#contem o menu que irá fazer a chamada de tosos os jogos e gere quando fecha o programa

while True:
    os.system('cls')
    print("====================================================")
    print("                      ---------                     ")
    print("                   Projeto Python                   ")
    print("                      ---------                     ")
    print("                    Ângelo Veiga                    ")
    print("                  Armando Pinheiro                  ")
    print("                    Nuno Martins                    ")
    print("====================================================")

    menu=(int(input("Escolha uma opção\n1-Jogo do galo\n2-Banca Francesa\n3-Pedra, papel, tesoura\n0-Sair\n")))
    if menu==1:
        print("A iniciar jogo do galo...")
        time.sleep(1)
        os.system('cls')
        galo.menu()
    elif menu==2:
        print("A iniciar Banca Francesa...")
        time.sleep(1)
        os.system('cls')
        Banca.menu()
    elif menu==3:
        print("A iniciar Pedra, papel, tesoura...")
        time.sleep(1)
        os.system('cls')
        Pedra.menu()
    elif menu==0:
        print("A sair...")
        time.sleep(1)
        break
    else:
        print("Insira uma opção correcta")