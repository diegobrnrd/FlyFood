"""FlyFood - Força Bruta"""


def abrir_arquivo():
    """Obtém a quantidade de linhas e colunas, além da matriz armazenada em uma lista."""
    with open('dados.txt', 'r') as arquivo:
        lin, col = arquivo.readline().split()
        matr = [[] for _ in range(int(lin))]
        for i, linha_dados in enumerate(arquivo):
            matr[i] = linha_dados.split()

    return int(lin), int(col), matr


def obter_coordenadas(matr):
    """Coleta as coordenadas dos pontos de interesse e as armazena em um dicionário."""
    coord_1, coord_2 = {}, {}
    # Dois dicionários são criados: um sem o ponto R e o outro completo.
    for x, l in enumerate(matr):
        for y, c in enumerate(l):
            if c == 'A' or c == 'B' or c == 'C' or c == 'D':
                coord_1[f'{c}'] = (int(x), int(y))
            elif c == 'R':
                coord_2[f'{c}'] = (int(x), int(y))

    coord_2.update(coord_1)

    return coord_1, coord_2


def gerar_rotas(coord):
    """Gera todas as combinações possíveis de rotas."""
    import itertools

    pontos = [None for _ in range(len(coord))]
    for i, p in enumerate(coord):
        pontos[i] = p

    permutacoes = list(itertools.permutations(pontos))
    # A permutação é feita sem o ponto R.
    permutacoes_com_r = [('R',) + perm + ('R',) for perm in permutacoes]
    # O ponto R é adicionado no início e no fim de todas as permutações.

    return permutacoes_com_r


def calcular_rotas(coord, rotass):
    """Calcula a distância total para cada uma das rotas possíveis."""
    resultado_final = {x: -1 for x in rotass}
    # Inicialmente, as distâncias são inicializadas com o valor -1.
    for rota_atual in rotass:
        resultado_final[rota_atual] = calcular_rota(coord, rota_atual)
        # A rota será a chave e a distância será o valor associado.

    return resultado_final


def calcular_rota(coord, rota_atual):
    """Calcula a distância total de uma rota específica."""
    soma = 0
    for i in range(len(rota_atual) - 1):
        soma += calcular_distancia(coord[rota_atual[i]], coord[rota_atual[i + 1]])

    return soma


def calcular_distancia(ponto_1, ponto_2):
    """Calcula a distância entre dois pontos."""
    return abs(ponto_2[0] - ponto_1[0]) + abs(ponto_2[1] - ponto_1[1])


def obter_menor_percurso(dist):
    """Encontra o menor percurso e sua distância em dronômetros."""
    chave, menor = '', float('inf')

    for chav, valor in dist.items():
        if valor < menor:
            chave = chav
            menor = valor

    return chave, menor


def saida(chave, valor):
    """Formata a saída de dados."""
    rota = [x for x in chave if x != 'R']
    saida_formatada = f'Rota: {" ".join(rota)} - Percurso: {valor} dronômetros'
    return saida_formatada


def funcao_principal():
    """Função principal que gerencia a chamada de todas as outras funções."""
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
