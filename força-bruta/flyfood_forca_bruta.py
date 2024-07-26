"""FlyFood - Força Bruta"""


def abrir_arquivo():
    """Obtém a quantidade de linhas e colunas, além da matriz armazenada em uma lista."""
    with open('dados.txt', 'r') as arquivo:
        linha, coluna = arquivo.readline().split()
        matriz = [[] for _ in range(int(linha))]
        for i, linha_dados in enumerate(arquivo):
            matriz[i] = linha_dados.split()

    return int(linha), int(coluna), matriz


def obter_coordenadas(matriz):
    """Coleta as coordenadas dos pontos de interesse e as armazena em um dicionário."""
    coordenadas_com_r = {}
    # Dicionário com o ponto R.
    for x, l in enumerate(matriz):
        for y, c in enumerate(l):
            if c != '0':
                coordenadas_com_r[f'{c}'] = (int(x), int(y))

    coordenadas_sem_r = coordenadas_com_r.copy()
    del coordenadas_sem_r['R']
    # Dicionário sem o ponto R.

    return coordenadas_com_r, coordenadas_sem_r


def gerar_rotas(coordenadas):
    """Gera todas as combinações possíveis de rotas."""
    import itertools

    pontos = [None for _ in range(len(coordenadas))]
    for i, p in enumerate(coordenadas):
        pontos[i] = p

    permutacoes = list(itertools.permutations(pontos))
    # A permutação é feita sem o ponto R.
    permutacoes_com_r = [('R',) + perm + ('R',) for perm in permutacoes]
    # O ponto R é adicionado no início e no fim de todas as permutações.

    return permutacoes_com_r


def calcular_rotas(coordenadas, rotas):
    """Calcula a distância total para cada uma das rotas possíveis."""
    distancias = {x: -1 for x in rotas}
    # Inicialmente, as distâncias são inicializadas com o valor -1.
    # As rotas são as chaves.
    for rota_atual in rotas:
        distancias[rota_atual] = calcular_rota(coordenadas, rota_atual)
        # É atribuído o valor de cada rota atual.

    return distancias


def calcular_rota(coordenadas, rota_atual):
    """Calcula a distância total de uma rota específica."""
    soma = 0
    for i in range(len(rota_atual) - 1):
        soma += calcular_distancia(coordenadas[rota_atual[i]], coordenadas[rota_atual[i + 1]])

    return soma


def calcular_distancia(ponto_1, ponto_2):
    """Calcula a distância entre dois pontos."""
    return abs(ponto_2[0] - ponto_1[0]) + abs(ponto_2[1] - ponto_1[1])


def obter_menor_percurso(distancias):
    """Encontra o menor percurso e sua distância em dronômetros."""
    percurso, menor_distancia = '', float('inf')

    for chave, valor in distancias.items():
        if valor < menor_distancia:
            percurso = chave
            menor_distancia = valor

    return percurso, menor_distancia


def saida(chave, valor):
    """Formata a saída de dados."""
    rota = [x for x in chave if x != 'R']
    # O ponto R inicial e final são retirados para exibição do resultado.
    saida_formatada = f'Rota: {" ".join(rota)} - Percurso: {valor} dronômetros'
    return saida_formatada


def central():
    """Função principal que gerencia a chamada de todas as outras funções."""
    linha, coluna, matriz = abrir_arquivo()
    coordenadas_com_r, coordenadas_sem_r = obter_coordenadas(matriz)
    rotas = gerar_rotas(coordenadas_sem_r)
    distancias = calcular_rotas(coordenadas_com_r, rotas)
    percurso, menor_distancia = obter_menor_percurso(distancias)
    print(saida(percurso, menor_distancia))


if __name__ == '__main__':
    import timeit
    tempo_de_execucao = timeit.timeit(central, number=1)
    print(f'Tempo de execução: {tempo_de_execucao} segundos')
