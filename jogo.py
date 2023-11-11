# Importa o módulo random, que será usado para gerar números aleatórios (neste caso, simular o lançamento de um dado).
import random

#Define uma função jogar_dado() que retorna um número aleatório entre 1 e 6, simulando o resultado de lançar um dado.
def jogar_dado():
    return random.randint(1, 6)

# Define uma função criar_jogador(nome) que cria e retorna um dicionário representando um jogador. 
# O dicionário tem uma chave 'nome' para o nome do jogador e uma chave 'resultados' que é inicializada como uma lista vazia para armazenar os resultados dos lançamentos de dados.
def criar_jogador(nome):
    return {'nome': nome, 'resultados': []}

# Define a função principal main().
def main():
# Pergunta ao usuário quantas rodadas e jogadores participarão
    num_rodadas = int(input("Quantas rodadas você deseja jogar? "))
# armazenando essas informações nas variáveis num_rodadas e num_jogadores.
    num_jogadores = int(input("Quantos jogadores vão participar do jogo? "))

# Cria uma lista(array) para armazenar os jogadores
    jogadores = []

# Preenche a lista de jogadores com base no número inserido pelo usuário
    for i in range(num_jogadores):
# Em um loop, pergunta o nome de cada jogador e adiciona um dicionário representando esse jogador à lista jogadores usando a função criar_jogador().
        nome_jogador = input(f"Nome do jogador {i+1}: ")
        jogadores.append(criar_jogador(nome_jogador))

    # Realiza as rodadas do jogo
    for rodada in range(num_rodadas):
        print(f"\nRodada {rodada + 1}:")

# Cada jogador joga o dado e armazena o resultado
#Para cada rodada, percorre cada jogador na lista jogadores, faz com que cada jogador jogue o dado (jogar_dado()), armazena o resultado na lista de resultados do jogador e imprime o resultado.
        for jogador in jogadores:
            resultado = jogar_dado()
            jogador['resultados'].append(resultado)
            print(f"{jogador['nome']} jogou o dado e obteve: {resultado}")

# Ordena os jogadores pelo máximo tirado no dado (maior vitória)
#Isso é feito usando a função sort() com uma função lambda como chave.
    jogadores.sort(key=lambda x: max(x['resultados']), reverse=True)

    # Exibe o resultado final contando o número de vitórias para cada jogador e imprimindo essas informações.
    print("\nResultado final:")
    for jogador in jogadores:
        num_vitorias = jogador['resultados'].count(max(jogador['resultados']))
        print(f"{jogador['nome']} obteve {num_vitorias} vitórias.")

# Verifica se houve empate
# Se houver um empate, imprime uma mensagem indicando isso
# Ou vai declarar o jogador com o maior resultado máximo como o campeão
    if len(jogadores) > 1 and max(jogadores[0]['resultados']) == max(jogadores[1]['resultados']):
        print("Houve um empate entre os jogadores. Ninguem ganhou, mas pelo menos todos se divertiram né?!")
    else:
        print(f"\nO grande campeão é {jogadores[0]['nome']}!")

# Verifica se o script está sendo executado diretamente (__name__ == "__main__") e, nesse caso, chama a função principal main().
if __name__ == "__main__":
    main()
