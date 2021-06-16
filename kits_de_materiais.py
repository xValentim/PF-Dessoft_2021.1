'''
Kits de materiais
Devido às aulas remotas, os professores de uma disciplina montaram kits de materiais que serão enviados pelo correio. Foi solicitado aos professores que agrupassem os kits pela inicial do nome dos alunos, para facilitar a organização. Os professores possuem as listas dos alunos separados por turmas e gostariam de obter as listas dos alunos separados pelas iniciais.

Faça uma função que recebe um dicionário de turmas, cujas chaves são nomes de turmas e os valores são listas com os nomes dos alunos, e devolve um dicionário cujas chaves são as letras iniciais e os valores são listas contendo os nomes dos alunos com aquela inicial. Por exemplo:

Entrada:
{
    "Turma A": ["Ana", "Beatriz", "Jorge"],
    "Turma B": ["Cecília", "João"],
    "Turma C": ["Amanda", "Joana", "Lucas"],
}
Saída:
{
    "A": ["Ana", "Amanda"],
    "B": ["Beatriz"],
    "C": ["Cecília"],
    "J": ["Jorge", "João", "Joana"],
    "L": ["Lucas"],
}
Entrada:
{
    "Sala 1": ["Américo", "Yuri"],
    "Sala 2": ["Marcos"],
    "Sala 3": ["Enzo", "Olívia"],
    "Sala 4": ["Pedro", "Paulo", "Edson"],
}
Saída:
{
    "A": ["Américo"],
    "E": ["Enzo", "Edson"],
    "M": ["Marcos"],
    "O": ["Olívia"],
    "P": ["Pedro", "Paulo"],
    "Y": ["Yuri"],
}
Observação 1: você pode assumir que os nomes sempre começam com letra maiúscula.

Observação 2: as listas de nomes podem ser devolvidas em qualquer ordem.

Observação 3: o dicionário devolvido não pode conter iniciais sem nenhum nome.

Observação 4: não se preocupe com nomes repetidos.

O nome da sua função deve ser separa_por_inicial
'''

def separa_por_inicial(turmas):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'.upper()
    dc_com_iniciais = {}
    # Cria uma dicionario temporario com as letras em ordem alfábetica
    # OBS.: Algumas terão uma lista vazia como valor, porém isso será corrigido no final
    for letra in alfabeto:
        dc_com_iniciais[letra] = []
    # Agora a complexidade de tempo diminuiu devido ao menor numero de for's
    for turma in turmas:
        for aluno in turmas[turma]:
            inicial_do_aluno = aluno[0]
            dc_com_iniciais[inicial_do_aluno].append(aluno)
    # Output é a saida final, com os valores corrigidos (não haverão chaves que possuirão valores como listas vazias)
    output = {}
    for inicial in dc_com_iniciais:
        if dc_com_iniciais[inicial] != []:
            output[inicial] = dc_com_iniciais[inicial]
    return output   
    
'''def separa_por_inicial(turmas):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'.upper()
    dc_com_iniciais = {}
    lista_aux = []
    # Mantém a ordem alfabética
    # Porém, complexidade de tempo fica alta devido ao numero de for's
    for inicial in alfabeto:
        for turma in turmas:
            for aluno in turmas[turma]:
                if inicial == aluno[0]:
                    lista_aux.append(aluno)
        if lista_aux != []:
            dc_com_iniciais[inicial] = lista_aux
            lista_aux = []
    return dc_com_iniciais
'''

turmas = {
    "Turma A": ["Ana", "Beatriz", "Jorge"],
    "Turma B": ["Cecília", "João"],
    "Turma C": ["Amanda", "Joana", "Lucas"],
}
print(separa_por_inicial(turmas))