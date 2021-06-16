'''Senha forte
Faça uma função que decide se uma senha é forte ou fraca. A função deve devolver True se for forte e False se for fraca.

Para uma senha ser considerada forte ela deve satisfazer os 3 requisitos a seguir:

Possuir pelo menos 2 caracteres especiais diferentes entre '?', '!', '@', '#', '$', '%', '&', '*';
Ser composta por pelo menos 8 caracteres;
Não pode possuir caracteres repetidos em sequência. Por exemplo: 'abbc', NÃO PODE, possui 2 'b' repetidos em sequência. Já, 'abcb' pode, pois os 'b' não estão em sequência.
Exemplos de senhas fortes:

'abcdef?!'
'@abcdefgh@#'
'$%abcdcba%$'
'aAbBcCdD*123&'
Exemplos de senhas fracas:

'abcde?!' (possui apenas 7 caracteres)
'!abcdef!' (possui apenas 1 caractere especial)
'?abcdeef!' (possui o caractere 'e' repetido em sequência)
'abba' (não satisfaz nenhum dos requisitos)
O nome da sua função deve ser valida_senha'''

def valida_senha(senha):
    # fura o requisito 2
    if len(senha) < 8:
        return False
    for i in range(len(senha) - 1):
        # fura o requisito 3
        if senha[i] == senha[i + 1]:
            return False
    carac_especiais = ['?', '!', '@', '#', '$', '%', '&', '*']
    # lista que guarda os caracteres especiais utilizados e sem repetição
    aux = []
    for caracter in senha:
        if caracter in carac_especiais and caracter not in aux:
            aux.append(caracter)
    # Checa se possui ao menos dois caracteres especiais (sem contar repetições)
    if len(aux) > 1:
        # passa em todos os requisitos
        return True
    # fura o requisito 1
    return False