import tkinter as tk
import random

def jogar_dado():
    return random.randint(1, 6)

def criar_jogador(nome):
    return {'nome': nome, 'resultados': []}

def main(num_rodadas, jogadores):
    lista_jogadores = []
    for nome_jogador in jogadores:
        lista_jogadores.append(criar_jogador(nome_jogador))

    for rodada in range(num_rodadas):
        print(f"\nRodada {rodada + 1}:")
        for jogador in lista_jogadores:
            resultado = jogar_dado()
            jogador['resultados'].append(resultado)
            print(f"{jogador['nome']} jogou o dado e obteve: {resultado}")

    max_resultado_global = max(max(jogador['resultados']) for jogador in lista_jogadores)

    for jogador in lista_jogadores:
        num_vitorias = jogador['resultados'].count(max_resultado_global)
        jogador['num_vitorias'] = num_vitorias

    lista_jogadores.sort(key=lambda x: x['num_vitorias'], reverse=True)

    resultado_final = "\nResultado final:\n"
    for jogador in lista_jogadores:
        resultado_final += f"{jogador['nome']} obteve {jogador['num_vitorias']} vitórias.\n"

    if len(lista_jogadores) > 1 and lista_jogadores[0]['num_vitorias'] == lista_jogadores[1]['num_vitorias']:
        resultado_final += "Houve um empate entre os jogadores. Não há um único campeão."
    else:
        resultado_final += f"\nO grande campeão é {lista_jogadores[0]['nome']}!"

    return resultado_final

def atualizar_resultado():
    num_rodadas = int(entry_rodadas.get())
    num_jogadores = int(entry_num_jogadores.get())
    nomes_jogadores = [entry_nomes[i].get() for i in range(num_jogadores)]
    resultado_final = main(num_rodadas, nomes_jogadores)
    resultado_label.config(text=resultado_final)

def criar_caixas_nomes():
    num_jogadores = int(entry_num_jogadores.get())
    for i in range(num_jogadores):
        label_nome = tk.Label(janela, text=f"Nome do Jogador {i + 1}:")
        label_nome.pack(pady=5)
        entry_nome = tk.Entry(janela)
        entry_nome.pack(pady=5)
        entry_nomes.append(entry_nome)

janela = tk.Tk()
janela.title("Jogo de Dados")

label_rodadas = tk.Label(janela, text="Quantas rodadas você deseja jogar?")
label_rodadas.pack(pady=5)
entry_rodadas = tk.Entry(janela)
entry_rodadas.pack(pady=5)

label_num_jogadores = tk.Label(janela, text="Quantos jogadores vão participar do jogo?")
label_num_jogadores.pack(pady=5)
entry_num_jogadores = tk.Entry(janela)
entry_num_jogadores.pack(pady=5)

botao_criar_caixas = tk.Button(janela, text="Criar Caixas de Nomes", command=criar_caixas_nomes)
botao_criar_caixas.pack(pady=10)

entry_nomes = []

botao_jogar = tk.Button(janela, text="Jogar Dados", command=atualizar_resultado)
botao_jogar.pack(pady=10)

resultado_label = tk.Label(janela, text="Resultado do jogo: ")
resultado_label.pack(pady=10)

janela.mainloop()
