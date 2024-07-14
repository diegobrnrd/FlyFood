# Registra a entrada em um arquivo e cria as variáveis linha e coluna no escopo global.
def entrada():
    with open('dados.txt', 'w') as arquivo:
        primeira_linha = input()
        arquivo.write(primeira_linha)
        lin, col = primeira_linha.split()

        for _ in range(int(lin)):
            arquivo.write(f'\n{input()}')

        return int(lin), int(col)


# Ler o arquivo e cria no escopo global uma matriz em formato de lista
def ler_dados(lin):
    matr = [[] for _ in range(lin)]
    with open('dados.txt', 'r') as arquivo:
        arquivo.readline()
        for i, linha_dados in enumerate(arquivo):
            matr[i] = linha_dados.split()

    return matr


# Converte a matriz em dicionário com suas respectivas coordenadas
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


# Obtém todas as rotas possíveis
def obter_rotas(cord):
    pontos = [None for _ in range(len(cord))]
    for i, p in enumerate(cord):
        pontos[i] = p

    permutacoes = list(itertools.permutations(pontos))
    permutacoes_com_r = [('R',) + perm + ('R',) for perm in permutacoes]

    return permutacoes_com_r


# Cálcula a distância de todas as rotas
def calcular_rotas(coord, rots):
    resultado_final = {x: -1 for x in rots}

    for rota_atual in rots:
        resultado_final[rota_atual] = somar_distancias(coord, rota_atual)

    return resultado_final


# Cálcula a distância de uma rota
def somar_distancias(coord, rota_atual):
    soma = 0
    for i in range(len(rota_atual) - 1):
        soma += calcular_distancia(coord[rota_atual[i]], coord[rota_atual[i + 1]])

    return soma


# Cálcula a distância entre dois pontos
def calcular_distancia(ponto_1, ponto_2):
    return abs(ponto_2[0] - ponto_1[0]) + abs(ponto_2[1] - ponto_1[1])


# Encontra qual o menor percurso e sua distância
def obter_menor_percurso(dist):
    chave, valor, menor = '', -1, float('inf')
    for k, v in dist.items():
        if v < menor:
            chave = k
            valor = v
            menor = v

    return chave, valor


# Formata a saída
def saida(chave, valor):
    rota = [x for x in chave if x != 'R']
    s = f'Rota: {" ".join(rota)} | Percurso: {valor} dronômetros'
    return s


if __name__ == '__main__':
    linha, coluna = entrada()
    matriz = ler_dados(linha)
    coordenadas_sem_r, coordenadas_com_r = obter_coordenadas(matriz)
    import itertools
    rotas = obter_rotas(coordenadas_sem_r)
    distancias = calcular_rotas(coordenadas_com_r, rotas)
    menor_percurso, menor_distancia = obter_menor_percurso(distancias)
    print(saida(menor_percurso, menor_distancia))
