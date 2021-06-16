'''
Cifra de substituição
Uma cifra de substituição é um método básico de criptografia no qual aplica-se um sistema de troca de caracteres pré-definidos para ocultar o seu conteúdo. Por exemplo, se a regra do sistema é trocar o caractere pelo próximo, ao codificar a string 'abacate' obteríamos 'bcbdbuf'. Para decodificar a string (recuperar o seu conteúdo original), aplica-se a troca inversa.

Faça uma função que recebe uma string codificada e um dicionário definindo o sistema de trocas e devolve a string decodificada. Por exemplo:

Exemplo 1

Entrada:
String codificada: '*b*c*t&'
Sistema de trocas: {'a': '*', 'e': '&'}
Saída: 'abacate'
Exemplo 2

Entrada:
String codificada: 'eznznz'
Sistema de trocas:
{
    'a': 'z',
    'b': 'e',
    'z': '!',
    'e': '*',
}
Saída: 'banana'
O nome da sua função deve ser decodifica
'''


def decodifica(codificado, coder):
    decoder = {}
    # inverte os papeis
    keys_decoder = list(coder.values())
    values_decoder = list(coder.keys())
    print(keys_decoder, values_decoder)
    # forma o dicionario de decodificação (inverso do de codificação)
    for i in range(len(coder)):
        decoder[keys_decoder[i]] = values_decoder[i]
    decodificado = ''
    for caracter in codificado:
        if caracter in decoder.keys():
            decodificado += decoder[caracter]
        else:
            decodificado += caracter
    return decodificado

string = '*b*c*t&'
trocas = {'a': '*', 'e': '&'}

print(decodifica(string, trocas))