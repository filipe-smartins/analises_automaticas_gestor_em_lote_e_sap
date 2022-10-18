
from easygui import enterbox
from datetime import datetime






for i in range(0, len(dados['Data de Constituição'])):

    tempo_de_mercado = calcular_tempo_de_mercado(dados['Tempo Fundação'][i])



    movimentacao_de_mercado = calcular_movimentacao_de_mercado(
        dados['Número de títulos'][i], dados['Número de fontes'][i]
    )

    pontualidade = calcular_pontualidade_de_mercado(dados['% de pontualidade'][i])

    maior_acumulo = calcular_maior_acumulo_mercado(dados['Valor do maior acumulo'][i])

    socios = identificar_socios_e_participacao(
        dados['Sócio 1'][i], dados['Sócio 2'][i], dados['Sócio 3'][i], dados['Sócio 4'][i],
        dados['Participação Sócio 1'][i], dados['Participação Sócio 2'][i],
        dados['Participação Sócio 3'][i], dados['Participação Sócio 4'][i],
    )

    ramo_atuacao = dados['Ramo de atuação'][i]

    texto_restricao, valor_restricao = calcular_restricoes(dados['Total de restrições'][i], capital_social, maior_acumulo)

    parecer = f'''
    Empresa com {tempo_de_mercado} com Capital Social de {capital_social} KBRL,
    com {movimentacao_de_mercado}, acúmulos de até {maior_acumulo} KBRL e {pontualidade}.
    {texto_restricao}
    
    Informações societárias: {socios}
    Ramo de atuação: {ramo_atuacao}
    
    
    Codigo Cliente: {dados['Codigo Cliente'][i]}
    Tempo Fundação: {dados['Tempo Fundação'][i]}
    Data de Constituição: {dados['Data de Constituição'][i]}
    Limite solicitado: {dados['Limite solicitado'][i]}
    Capital Social: {dados['Capital Social'][i]},00
    Cliente Novo: {dados['Cliente Novo'][i]}
    Alerta de Negócio: {dados['Alerta de Negócio'][i]} 
    Recomendacao gestor: {dados['Recomendacao gestor'][i]}
    Porte da empresa: {dados['Porte da empresa'][i]}
    Sócios: {socios}
    Ramo de atuação: {dados['Ramo de atuação'][i]}
    % de pontualidade: {dados['% de pontualidade'][i]}
    Número de títulos: {dados['Número de títulos'][i]}
    Número de fontes: {dados['Número de fontes'][i]}
    Valor do maior acumulo: {dados['Valor do maior acumulo'][i]} 
    Total de restrições: {dados['Total de restrições'][i]}
    
    '''
    print(parecer)


def calcular_compatibilidade_limite_solicitado(lc_solicitado, capital_social, acumulo_mercado):

    lc_solicitado / capital_social
    lc_solicitado / acumulo_mercado


    return 1


'''

DELIBERAÇÃO:


SOBRE O CLIENTE e GRUPO:
Cliente:

Grupo:


INFORMAÇÕES INTERNAS:


INFORMAÇÕES DE MERCADO:


SEGURADORAS:


INFORMAÇÕES FINANCEIRAS:


PARECER DE CRÉDITO:

'''