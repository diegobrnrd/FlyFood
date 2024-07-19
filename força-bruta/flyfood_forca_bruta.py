# Coleta a quantidade de linha(s), coluna(s) e a matriz armazenada em uma lista
def abrir_arquivo():
    with open('dados.txt', 'r') as arquivo:
        lin, col = arquivo.readline().split()
        matr = [[] for _ in range(int(lin))]
        for i, linha_dados in enumerate(arquivo):
            matr[i] = linha_dados.split()

    return int(lin), int(col), matr


# Converte a matriz em dicionário com suas respectivas coordenadas
# Dois dicionários são criados, um sem o ponto R e o outro completo
def obter_coordenadas(matr):
    coord_1, coord_2 = {}, {}

    for x, l in enumerate(matr):
        for y, c in enumerate(l):
            if c == 'A' or c == 'B' or c == 'C' or c == 'D':
                coord_1[f'{c}'] = (int(x), int(y))
            elif c == 'R':
                coord_2[f'{c}'] = (int(x), int(y))

    coord_2.update(coord_1)

    return coord_1, coord_2


# Gera todas as rotas possíveis
def gerar_rotas(cord):
    import itertools

    pontos = [None for _ in range(len(cord))]
    for i, p in enumerate(cord):
        pontos[i] = p

    permutacoes = list(itertools.permutations(pontos))
    permutacoes_com_r = [('R',) + perm + ('R',) for perm in permutacoes]

    return permutacoes_com_r


# Cálcula a distância de todas as rotas | Função 1-3
def calcular_rotas(coord, rotass):
    resultado_final = {x: -1 for x in rotass}

    for rota_atual in rotass:
        resultado_final[rota_atual] = calcular_rota(coord, rota_atual)

    return resultado_final


# Cálcula a distância de uma rota | Função 2-3
def calcular_rota(coord, rota_atual):
    soma = 0

    for i in range(len(rota_atual) - 1):
        soma += calcular_distancia(coord[rota_atual[i]], coord[rota_atual[i + 1]])

    return soma


# Cálcula a distância entre dois pontos | Função 3-3
def calcular_distancia(ponto_1, ponto_2):

    return abs(ponto_2[0] - ponto_1[0]) + abs(ponto_2[1] - ponto_1[1])


# Encontra qual o menor percurso e sua distância em dronômetros
def obter_menor_percurso(dist):
    chave, menor = '', float('inf')

    for chav, valor in dist.items():
        if valor < menor:
            chave = chav
            menor = valor

    return chave, menor


# Formata a saída
def saida(chave, valor):
    rota = [x for x in chave if x != 'R']
    saida_formatada = f'Rota: {" ".join(rota)} | Percurso: {valor} dronômetros'
    return saida_formatada


# Função principal que chama todas as outras
def funcao_principal():
    linha, coluna, matriz = abrir_arquivo()
    coordenadas_sem_r, coordenadas_com_r = obter_coordenadas(matriz)
    rotas = gerar_rotas(coordenadas_sem_r)
    distancias = calcular_rotas(coordenadas_com_r, rotas)
    menor_percurso, menor_distancia = obter_menor_percurso(distancias)
    print(saida(menor_percurso, menor_distancia))


if __name__ == '__main__':
    import timeit
    tempo_de_execucao = timeit.timeit(funcao_principal, number=1)
    print(f"Tempo de execução: {tempo_de_execucao} segundos")
