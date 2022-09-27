import sqlite3
from easygui import enterbox
from datetime import datetime
from os.path import expanduser
import pandas as pd


home = expanduser("~")
sharepoint_path = fr'{home}\ArcelorMittal\Dados da VP Corporativa de Finanças e TI - Crédito Corporativo'
file_path = fr'{home}\OneDrive - ArcelorMittal\Documents'


def alimentar_bd_em_massa():
    try:
        dados = pd.read_csv(fr'{file_path}\Exporta.csv', sep=';', encoding='utf-8')
    except UnicodeDecodeError:
        dados = pd.read_csv(fr'{file_path}\Exporta.csv', sep=';', encoding='latin-1')

    dados.rename(columns={'LOGON': 'LOGON SERASA'}, inplace=True)
    dados = dados.drop(columns=['DATA FUNDACAO', 'RECEITA - RAZAO SOCIAL'])  # del(dados['DATA FUNDACAO'])

    conn = sqlite3.connect(fr'{sharepoint_path}\Automações\Banco de Dados\database.db')
    dados.to_sql(name=f'gestor', con=conn, if_exists='append', index=True)
    conn.commit()  # comando para gravar os dados no Banco de Dados
    conn.close()  # fecha a conecção com o banco de dados


nomes_colunas = {
    'DATA DA FUNDACAO': ['Data de Constituição', str],
    '- A) DU_CREDITO SOLICITADO -': ['Limite solicitado', str],
    'CAPITAL SOCIAL': ['Capital Social', str],
    'NOME DO SOCIO/ACIONISTA 1': ['Sócio 1', str],
    'NOME DO SOCIO/ACIONISTA 2': ['Sócio 2', str],
    'NOME DO SOCIO/ACIONISTA 3': ['Sócio 3', str],
    'NOME DO SOCIO/ACIONISTA 4': ['Sócio 4', str],
    '% CAP TOTAL SOCIO/ACIONISTA 1': ['Participação Sócio 1', str],
    '% CAP TOTAL SOCIO/ACIONISTA 2': ['Participação Sócio 2', str],
    '% CAP TOTAL SOCIO/ACIONISTA 3': ['Participação Sócio 3', str],
    '% CAP TOTAL SOCIO/ACIONISTA 4': ['Participação Sócio 4', str],
    'RAMO DE ATIVIDADE': ['Ramo de atuação', str],
    '% PAGTOS PONTUAIS': ['% de pontualidade', str],
    '** QTDE DE TÍTULOS **': ['Número de títulos', str],
    'FONTES CONSULTADAS': ['Número de fontes', str],
    'VALOR DO MAIOR ACUMULO': ['Valor do maior acumulo', str],
    '** FF_TOTAL RESTRIÇÃO **': ['Total de restrições', str],
    '- E) DU_CLIENTE_NOVO? -': ['Cliente Novo', str],
    'ALERTA (S / N)': ['Alerta de Negócio', str],
    'RECOMENDACAO': ['Recomendacao gestor', str],
    'PORTE DA EMPRESA': ['Porte da empresa', str],
    '- D) DU_CODIGO_DO_CLIENTE -': ['Codigo Cliente', str],
    '** IDADE_FUNDAÇÃO **': ['Tempo Fundação', str]
}

dtype = {}
rename = {}
for key in nomes_colunas.keys():
    dtype[key] = nomes_colunas[key][1]
    rename[key] = nomes_colunas[key][0]


dados = pd.read_csv(fr'{file_path}\Exporta.csv', sep=';', encoding='utf-8', dtype=dtype, usecols=nomes_colunas.keys())

dados = dados.rename(columns=rename)  # renomeia colunas do dataframe
dados = dados.reindex(columns=rename.values())  # ordena as colunas do dataframe de acordo com a lista
dados = dados.fillna('')
dados = dados.to_dict('list')


def calcular_tempo_de_mercado(tempo_fundacao):
    anos_constituicao = int(tempo_fundacao.split(',')[0])
    meses_constituicao = int((int(tempo_fundacao.split(',')[1])/100)*12)

    if meses_constituicao == 0:
        texto_meses_constituicao = 'menos de uma mês de fundação'
    elif meses_constituicao == 1:
        texto_meses_constituicao = '1 mês'
    else:
        texto_meses_constituicao = f'{meses_constituicao} meses'

    if anos_constituicao == 0 and meses_constituicao == 0:
        lv_tempo_de_mercado = f"constituição MUITO recente com {texto_meses_constituicao}"
    elif anos_constituicao == 0:
        lv_tempo_de_mercado = f"constituição MUITO recente com {texto_meses_constituicao} de fundação"
    elif anos_constituicao < 2 and meses_constituicao == 0:
        lv_tempo_de_mercado = f"constituição recente com apenas {anos_constituicao} ano de fundação"
    elif anos_constituicao < 2:
        lv_tempo_de_mercado = f"constituição recente com apenas {anos_constituicao} ano e {texto_meses_constituicao} de fundação"
    elif anos_constituicao >= 2 and meses_constituicao == 0:
        lv_tempo_de_mercado = f"{anos_constituicao} anos de fundação"
    elif 2 <= anos_constituicao < 3:
        lv_tempo_de_mercado = f"{anos_constituicao} anos e {texto_meses_constituicao} de fundação"
    else:
        lv_tempo_de_mercado = f"{anos_constituicao} anos de fundação"

    return lv_tempo_de_mercado


def calcular_movimentacao_de_mercado(qtde_titulos, qtde_fontes):
    try:
        titulos = int(qtde_titulos.replace(',00', '').replace('.', ''))
    except ValueError:
        titulos = 0

    try:
        fontes = int(qtde_fontes.replace(',00', '').replace('.', ''))
    except ValueError:
        fontes = 0

    titulos_x_fontes = titulos * fontes

    if titulos_x_fontes == 0:
        lv_movimentacao_de_mercado = f'SEM movimentação no mercado ({fontes} fontes e {titulos} titulos)'
    elif titulos_x_fontes < 250:
        lv_movimentacao_de_mercado = f'BAIXA movimentação no mercado ({fontes} fontes e {titulos} titulos)'
    elif titulos_x_fontes < 800:
        lv_movimentacao_de_mercado = f'movimentação MEDIANA no mercado ({fontes} fontes e {titulos} titulos)'
    elif titulos_x_fontes < 2000:
        lv_movimentacao_de_mercado = f'movimentação SATISFATÓRIA no mercado ({fontes} fontes e {titulos} titulos)'
    elif titulos_x_fontes < 6000:
        lv_movimentacao_de_mercado = f'BOA movimentação no mercado ({fontes} fontes e {titulos} titulos)'
    elif titulos_x_fontes < 15000:
        lv_movimentacao_de_mercado = f'GRANDE movimentação no mercado ({fontes} fontes e {titulos} titulos)'
    else:
        lv_movimentacao_de_mercado = f'ALTÍSSIMA movimentação no mercado ({fontes} fontes e {titulos} titulos)'

    return lv_movimentacao_de_mercado


def calcular_pontualidade(indice_pontualidade):
    indice_formatado = int(indice_pontualidade.replace('#', 'à 0%').split("à")[1].strip().replace("%", ""))

    if indice_formatado == 0:
        lv_pontualidade = f'SEM informações de pontualidade ({indice_pontualidade})'
    elif indice_formatado < 30:
        lv_pontualidade = f'BAIXÍSSIMA pontualidade ({indice_pontualidade}%)'
    elif indice_formatado < 70:
        lv_pontualidade = f'BAIXA pontualidade ({indice_pontualidade}%)'
    elif indice_formatado < 80:
        lv_pontualidade = f'pontualidade ACEITÁVEL ({indice_pontualidade}%)'
    elif indice_formatado < 90:
        lv_pontualidade = f'BOA pontualidade ({indice_pontualidade}%)'
    else:
        lv_pontualidade = f'ALTA pontualidade ({indice_pontualidade}%)'

    return lv_pontualidade


def calcular_maior_acumulo_mercado(acumulo_mercado):
    acumulo = float(acumulo_mercado.replace('#', '0').split("à")[1].strip().split()[0])
    expressao = acumulo_mercado.replace('#', '0').split("à")[1].strip().split()[1]

    if expressao == 'Mil':
        multiplicador = 1
    elif expressao == 'Mi':
        multiplicador = 1000

    acumulo = int(acumulo * multiplicador)

    return acumulo


def identificar_socios_e_participacao(socio1, socio2, socio3, socio4, partic1, partic2, partic3, partic4):

    p1 = int(float(partic1.replace('#', '0').replace(',', '.')))
    p2 = int(float(partic2.replace('#', '0').replace(',', '.')))
    p3 = int(float(partic3.replace('#', '0').replace(',', '.')))
    p4 = int(float(partic4.replace('#', '0').replace(',', '.')))

    if p1 + p2 + p3 + p4 == 0:
        socio = f'Participação dos sócios não disponível no Serasa. Nomes: {socio1}; {socio2}; {socio3}; {socio4};'
    else:
        s1 = f"{socio1} com participação de {p1}%; "
        s2 = f"{socio2} com participação de {p2}%; "
        s3 = f"{socio3} com participação de {p3}%; "
        s4 = f"{socio4} com participação de {p4}%; "

        if p1 == 0:
            s1 = ''
        if p2 == 0:
            s2 = ''
        if p3 == 0:
            s3 = ''
        if p4 == 0:
            s4 = ''

        socio = f'{s1}{s2}{s3}{s4}'.strip()

    return socio


def calcular_restricoes(info_restricoes, valor_capital_social, acumulos_mercado):
    lv_restricoes = int(float(info_restricoes.replace('#', '0').replace('.', '').replace(',', '.')))//1000

    indice1 = lv_restricoes / valor_capital_social * 100
    indice2 = lv_restricoes / acumulos_mercado * 100

    if lv_restricoes == 0:
        texto_restricoes = 'Sem restrições no mercado.'
    elif indice1 < 2 and indice2 < 10:
        texto_restricoes = f'Apresenta restrições de {lv_restricoes} KBRL, IRRELEVANTES no mercado em comparação ao ' \
                           f'Capital Social ({indice1}%) e acúmulos de mercado ({indice2}%).'
    elif indice1 < 5 and indice2 < 15:
        texto_restricoes = f'Apresenta restrições de {lv_restricoes} KBRL, nível ACEITÁVEL em comparação ao ' \
                           f'Capital Social ({indice1}%) e acúmulos de mercado ({indice2}%).'
    elif indice1 < 10 and indice2 < 20:
        texto_restricoes = f'Apresenta restrições de {lv_restricoes} KBRL, nível PREOCUPANTE em comparação ao ' \
                           f'Capital Social ({indice1}%) e acúmulos de mercado ({indice2}%).'
    elif indice1 < 15 and indice2 < 30:
        texto_restricoes = f'Apresenta restrições de {lv_restricoes} KBRL, nível MUITO PREOCUPANTE em comparação ao ' \
                           f'Capital Social ({indice1}%) e acúmulos de mercado ({indice2}%).'
    elif indice1 < 20 and indice2 < 50:
        texto_restricoes = f'Apresenta restrições de {lv_restricoes} KBRL, nível ALTO em comparação ao ' \
                           f'Capital Social ({indice1}%) e acúmulos de mercado ({indice2}%.).'
    elif indice1 < 30 and indice2 < 60:
        texto_restricoes = f'Apresenta restrições de {lv_restricoes} KBRL, nível MUITO ALTO em comparação ao ' \
                           f'Capital Social ({indice1}%) e acúmulos de mercado ({indice2}%).'
    else:
        texto_restricoes = f'Apresenta restrições de {lv_restricoes} KBRL, nível ALTÍSSIMO em comparação ao ' \
                           f'Capital Social ({indice1}%) e acúmulos de mercado ({indice2}%).'
    return texto_restricoes, lv_restricoes


for i in range(0, len(dados['Data de Constituição'])):

    tempo_de_mercado = calcular_tempo_de_mercado(dados['Tempo Fundação'][i])

    capital_social = int(dados['Capital Social'][i].replace('.', ''))//1000

    movimentacao_de_mercado = calcular_movimentacao_de_mercado(
        dados['Número de títulos'][i], dados['Número de fontes'][i]
    )

    pontualidade = calcular_pontualidade(dados['% de pontualidade'][i])

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