'''
Entregador mais próximo
Para desenvolver um aplicativo de entrega de comida, é útil saber qual entregador está mais próximo do restaurante. Faça uma função que recebe as coordenadas de um restaurante e uma lista de coordenadas (posições) de entregadores. Sua função deve devolver o índice do entregador mais próximo do restaurante.

Uma coordenada é representada por uma lista que contém 2 elementos. O primeiro representa o valor da coordenada x e o segundo o valor da coordenada y.

Exemplo 1:

Entrada:
Restaurante: [3, 4]
Entregadores:
[
    [10, 20],
    [4, 2],
    [100, 74],
    [23, 63]
]
Saída: 1 (o entregador mais próximo está no índice 1 da lista, ou seja, é o segundo entregador).
Exemplo 2:

Entrada:
Restaurante: [15, 20]
Entregadores:
[
    [28, 4],
    [63, 87],
    [192, 643],
    [16, 19],
    [523, 32],
]
Saída: 3
Observação 1: a distância de um ponto a outro ponto é:
((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5

Observação 2: o índice inicia em ZERO. Ou seja, o primeiro é o índice 0, o segundo é o índice 1 e assim por diante.

O nome da sua função deve ser entregador_mais_proximo
'''

# Funcao auxiliar para calcular distancia entre pontos (recebe duas listas de coordenadas x,y)
def distancia(xy1, xy2):
    x1, y1, x2, y2 = xy1[0], xy1[1], xy2[0], xy2[1]
    return ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5

def entregador_mais_proximo(xyr, xye):
    distancias = []
    for xyi in xye:
        distancia_i = distancia(xyr, xyi)
        distancias.append(distancia_i)
    # Utiliza uma lista auxiliar chamada distancias que guarda os valores das distancias para cada entregador
    # Em seguida, basta encontrar o valor minimo e depois utilizar o index para retornar o indice do valor minimo, que é o mesmo indice do entregador
    return distancias.index(min(distancias))