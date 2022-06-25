'''
Aluno: Manuel Alejandro Gonzalez Valdes
Curso: Análise e Desenvolvimento de Sistemas
Entrega da ATP - jogo Zombie Dice completo
'''

#Importando o módulo random para sortear os dados e as faces

import random
from random import shuffle
from collections import namedtuple

#Criação das principais funções para o funcionamento do jogo
#Função que estabelece a cor dos dados e suas respectivas faces:

def copo_dados():
    dado = namedtuple("Dado", ["cor", "faces"])
    dado_verde = dado("verde", ["C","P","C","T","P","C"])
    dado_amarelo = dado("amarelo", ["C","P","T","C","P","T"])
    dado_vermelho = dado("vermelho", ["T","P","T","C","P","T"])
    lista_dados = [dado_verde, dado_verde, dado_verde, dado_verde, dado_verde, dado_verde,
                   dado_amarelo, dado_amarelo, dado_amarelo, dado_amarelo,
                   dado_vermelho, dado_vermelho, dado_vermelho]
    shuffle(lista_dados)
    return lista_dados

#Função de registro e contagem dos jogadores:

def registro_jogadores():
    jogadores = []
    registro = True
    while registro:
        try:
            num_jogadores = int(input("\nQuantos jogadores participarão desta partida? "))
            if num_jogadores >= 2:
                break
            else:
                print("\nPrecisamos de mais zumbis para iniciar a rodada! ")
        except ValueError:
            print("Você precisa informar um número inteiro. ")
    for i in range (num_jogadores):
        nome = input("Digite o nome do "+str(i+1)+" jogador: ")
        zumbi = {"nome": nome, "score": 0}
        jogadores.append(zumbi)
    shuffle(jogadores)
    print("\n*** Os zumbis jogarão na seguinte ordem ***\n")
    i = 1
    for zumbi in jogadores:
        print('{:^40}'.format(f"{i}.{zumbi['nome']}"))
        i += 1
    return jogadores

#Função que define o turno do jogador e randomiza os dados e suas faces:

def turno(zumbi):
    print(f"\n{zumbi['nome']} é o próximo zumbi a jogar!\n")
    lista_dados = copo_dados()
    pontuacao = {"cérebros": 0, "tiros": 0}
    dados_temp = []
    while True:
        while len(dados_temp) <= 3:
            dados_temp.append(lista_dados.pop())
        i = 1
        for dado in dados_temp:
            print(f"Jogando dado {i}")
            i += 1
            cor = dado.cor
            shuffle(dado.faces)
            face_sorteada = random.choice(dado.faces)
            print(f"Dado: {cor} | Face: {face_sorteada}\n")
            if face_sorteada == "C":
                pontuacao["cérebros"] += 1
                lista_dados.append(dados_temp.pop(dados_temp.index(dado)))
            elif face_sorteada == "T":
                pontuacao["tiros"] += 1
                lista_dados.append(dados_temp.pop(dados_temp.index(dado)))
            shuffle(lista_dados)
        print(f"Pontuação atual:\nCérebros: {pontuacao['cérebros']} | Tiros: {pontuacao['tiros']}")
        if pontuacao["tiros"] < 3:
            continuar = input("\nQuer continuar tentando a sorte? (s/n) ")
            print()
            if continuar == 'n':
                print(f"Você escolheu parar de jogar. Sua pontuação foi de {pontuacao['cérebros']}")
                zumbi['score'] += pontuacao['cérebros']
                break
        else:
            print(f"\nVocê tomou três tiros! Sua rodada acaba por aqui. Pontuação: {pontuacao['cérebros']} cérebros")
            break

#Função placar:

def marcador(jogadores):
    print("*** PLACAR ***")
    for zumbi in jogadores:
        print(f"{zumbi['nome']}: {zumbi['score']} pontos. ")

#Jogo rodando:

print("\nSeja bem-vindo ao Zombie Dice! Quantos cérebros você será capaz de comer?")

jogadores = registro_jogadores()

fim_de_jogo = False
while not fim_de_jogo:
    for zumbi in jogadores:
        turno(zumbi)
        if zumbi['score'] >= 13:
            lider_zumbi = zumbi['nome']
            fim_de_jogo = True
    if not fim_de_jogo:
        marcador(jogadores)
    else:
        print(f"Vocês devoraram todos os cérebros da região. {lider_zumbi} é o líder dos zumbis!")
        marcador(jogadores)