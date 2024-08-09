"""FlyFood - Força Bruta"""


def ler_arquivo():
    """Coleta a matriz armazenada em uma lista de listas."""
    with open('dados.txt', 'r') as arquivo:
        linha, coluna = arquivo.readline().split()
        matriz = [[] for _ in range(int(linha))]
        for i, linha_dados in enumerate(arquivo):
            matriz[i] = linha_dados.split()

    return matriz


def obter_coordenadas(matriz):
    """Coleta as coordenadas dos pontos de interesse e as armazena em um dicionário."""
    coordenadas = {}
    for x, l in enumerate(matriz):
        for y, c in enumerate(l):
            if c != '0':
                coordenadas[f'{c}'] = (int(x), int(y))

    return coordenadas


def gerar_rotas(coordenadas):
    """Gera todas as combinações possíveis de rotas."""
    import itertools

    pontos = [ponto for ponto in coordenadas if ponto != 'R']
    # O ponto R é apagado.
    permutacoes = list(itertools.permutations(pontos))
    # A permutação é feita sem o ponto R.
    permutacoes_com_r = [('R',) + perm + ('R',) for perm in permutacoes]
    # O ponto R é adicionado no início e no fim de todas as permutações.

    return permutacoes_com_r


def calcular_rotas(coordenadas, rotas):
    """Calcula a distância total para cada uma das rotas possíveis."""
    menor_percurso = [(), float('inf')]
    for rota_atual in rotas:
        distancia = calcular_rota(coordenadas, rota_atual)
        if distancia < menor_percurso[1]:
            menor_percurso[0], menor_percurso[1] = rota_atual, distancia

    return menor_percurso


def calcular_rota(coordenadas, rota_atual):
    """Calcula a distância total de uma rota específica."""
    distancia = 0
    # len(rota_atual) - 1 porque, por exemplo, para calcular R A R é necessário fazer dois cálculos: de R A e A R.
    for i in range(len(rota_atual) - 1):
        distancia += calcular_distancia(coordenadas[rota_atual[i]], coordenadas[rota_atual[i + 1]])

    return distancia


def calcular_distancia(ponto_1, ponto_2):
    """Calcula a distância entre dois pontos."""
    return abs(ponto_2[0] - ponto_1[0]) + abs(ponto_2[1] - ponto_1[1])


def exibir_resultado(menor_percuso):
    """Formata a saída de dados."""
    rota = [x for x in menor_percuso[0] if x != 'R']
    # O ponto R inicial e final são retirados para exibição do resultado.
    print(f'Rota: {" ".join(rota)} - Percurso: {menor_percuso[1]} dronômetros.')


def funcao_central():
    """Função central que gerencia a chamada de todas as outras funções."""
    matriz = ler_arquivo()
    coordenadas = obter_coordenadas(matriz)
    rotas = gerar_rotas(coordenadas)
    menor_percuso = calcular_rotas(coordenadas, rotas)
    exibir_resultado(menor_percuso)


if __name__ == '__main__':
    """Cronometra o tempo necessário para a execução do algoritmo."""
    import timeit
    tempo_de_execucao = timeit.timeit(funcao_central, number=1)
    print(f'Tempo de execução: {tempo_de_execucao:.6f} segundos.')
