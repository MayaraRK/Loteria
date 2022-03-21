import numpy as np
import random

print('\n\nBem vindo!!!!!\n\n')
print('------------JOGO DA LOTERIA------------\n\n')

jogo = int(
    input('Deseja jogar qual modalidade: \n(1) Mega-Sena\n(2) Quina\n(3) Sair\n\nDigite qual a sua opção de jogo: \n'))

if jogo == 1:
    print('Você está apostando na Mega-Sena!!\n')

    sorteados_mega = random.sample(range(1, 61), 6)
    sorteados_mega = sorted(sorteados_mega)
    # print(sorteados_mega)

    palpite = []

    for i in range(1, 7):
        num = 0
        while num < 1 or num > 60 or num in palpite:
            num = int(input(f' {i}º número - Digite um número de 1 á 60: \n'))
        palpite.append(num)

    palpite = sorted(palpite)
    print('\n\n Sua aposta é: ', palpite)

    resultado = np.in1d(palpite, sorteados_mega)
    acertos = len(np.intersect1d(palpite, sorteados_mega))

    print('\n\nVocê ganhou na Mega-Sena!!!') if resultado.all() else print(
        f'\n\nVocê perdeu e acertou {acertos} numeros(s).')

    print('Sorteados: ', sorteados_mega)
    print('Sua aposta: ', palpite)


elif jogo == 2:
    print('Você está apostando na Quina!!\n')

    sorteados_quina = random.sample(range(1, 81), 5)
    sorteados_quina = sorted(sorteados_quina)
    # print(sorteados_quina)

    palpite = []

    for i in range(1, 6):
        num = 0
        while num < 1 or num > 80 or num in palpite:
            num = int(input(f' {i}º número - Digite um número de 1 á 80: \n'))
        palpite.append(num)

    palpite = sorted(palpite)
    print('\n\n Sua aposta é: ', palpite)

    resultado = np.in1d(palpite, sorteados_quina)
    acertos = len(np.intersect1d(palpite, sorteados_quina))

    print('\n\nVocê ganhou na Quina!!!') if resultado.all() else print(
        f'\n\nVocê perdeu e acertou {acertos} numeros(s).')

    print('Sorteados: ', sorteados_quina)
    print('Sua aposta: ', palpite)


elif jogo == 3:
    print('Volte sempre!!\n')
else:
    print('Opção inválida. Digite uma opção válida!')