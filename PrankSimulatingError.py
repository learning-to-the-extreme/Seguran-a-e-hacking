import os

def prank():
    os.system("color 0c") # muda a cor do fundo para vermelho
    os.system("cls") # limpa a tela

    print("\n\n\n")
    print("*********************************************")
    print("*                                           *")
    print("*            ERROR 0x0000005D               *")
    print("*        SYSTEM CRITICAL FAILURE            *")
    print("*                                           *")
    print("*********************************************")
    print("\n\n\n")
    print("Press any key to continue...")
    input() # espera a entrada do usuário antes de sair
    os.system("color 07") # muda a cor de volta para o padrão

prank()
