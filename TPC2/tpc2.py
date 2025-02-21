import sys
import re

padrao_nome = r'[^;]+;"'
padrao_ano = r';\d{4};'
padrao_periodo = r';[A-ZÀ-Ö][a-zØ-öø-ÿ]{2,}(\s[A-Z]+)?;'
padrao_compositor = r';[A-Za-z]+,?\s[A-Za-z\s]+;'
padrao_duracao = r';\d{2}:\d{2}:\d{2};'
padrao_id = r';O\d+'
 
def ler_dataset(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        nome = []
        ano = []
        periodo = []
        compositor = []
        duracao = []
        _id = []
        for line in linhas[1:]:  # Ignora o cabeçalho
        	nome += re.findall(padrao_nome, line)
        	ano += re.findall(padrao_ano, line)
        	periodo += re.findall(padrao_periodo, line)
        	compositor += re.findall(padrao_compositor,line)
        	duracao += re.findall(padrao_duracao, line)
        	_id += re.findall(padrao_id, line)
    return nome, compositor, ano, periodo, duracao, _id

def print_ord(l):
	for word in l:
		print (word)


def main():
    caminho = 'obras.csv'
    nome, compositor, ano, periodo, duracao, _id = ler_dataset(caminho)
    nome_limpo = [s.replace('"', '').replace(';', '') for s in nome]
    ano_limpo = [s.replace(';', '') for s in ano]
    periodo_limpo = [s.replace(';', '') for s in periodo]
    compositor_limpo = [s.replace(';', '') for s in compositor]
    duracao_limpo = [s.replace(';', '') for s in duracao]
    id_limpo = [s.replace(';', '') for s in _id]

    # Comentários para debug (opcional)
    # print(f"nome = {nome_limpo}")
    # print(f"ano = {ano_limpo}")
    print(f"periodo = {periodo_limpo}")
    # print(f"duracao = {duracao_limpo}")
    # print(f"compositor = {compositor_limpo}")
    # print(f"ID = {id_limpo}")
    print("Lista ordenada por ordem alfabética de compositores")
    print_ord(sorted(compositor_limpo))
    print(len(nome_limpo),len(ano_limpo), len(periodo_limpo), len(compositor_limpo), len(duracao_limpo), len(id_limpo))

if __name__ == '__main__':
	main()