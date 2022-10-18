from Dados import *
from Clientes import Clientes
from InformacoesExternas import InformacoesExternas
from InformacoesInternas import InformacoesInternas

dados = Dados()

lista_clientes = []

for i in range(0, len(dados.dados_clientes['Data de Constituição'])):

    info_internas = InformacoesInternas()
    info_externas = InformacoesExternas()

    cliente = Clientes(
        dados.dados_clientes['Data de Constituição'][i], dados.dados_clientes['Limite solicitado'][i],
        dados.dados_clientes['Capital Social'][i], dados.dados_clientes['Sócio 1'][i],
        dados.dados_clientes['Sócio 2'][i], dados.dados_clientes['Sócio 3'][i], dados.dados_clientes['Sócio 4'][i],
        dados.dados_clientes['Participação Sócio 1'][i], dados.dados_clientes['Participação Sócio 2'][i],
        dados.dados_clientes['Participação Sócio 3'][i], dados.dados_clientes['Participação Sócio 4'][i],
        dados.dados_clientes['Ramo de atuação'][i], dados.dados_clientes['% de pontualidade'][i],
        dados.dados_clientes['Número de títulos'][i], dados.dados_clientes['Número de fontes'][i],
        dados.dados_clientes['Valor do maior acumulo'][i], dados.dados_clientes['Total de restrições'][i],
        dados.dados_clientes['Cliente Novo'][i], dados.dados_clientes['Alerta de Negócio'][i],
        dados.dados_clientes['Recomendacao gestor'][i], dados.dados_clientes['Porte da empresa'][i],
        dados.dados_clientes['Tempo Fundação'][i], dados.dados_clientes['Código SAP do Cliente'][i],
        dados.dados_clientes['Limite Anterior'][i], dados.dados_clientes['Contas a Receber'][i],
        dados.dados_clientes['ano_historico_interno'][i], dados.dados_clientes['mes_historico_interno'][i],
        dados.dados_clientes['valores_historico_interno'][i], dados.dados_clientes['dias_atraso_interno'][i],
        dados.dados_clientes['meses_pontuais_internamente'][i], dados.dados_clientes['historico_interno_12meses'][i],
        dados.dados_clientes['valores_interno_12meses'][i],
        dados.dados_clientes['meses_pontuais_internamente_12meses'][i], info_internas, info_externas

    )

    cliente.info_externas.calcular_tempo_de_mercado(cliente.tempo_de_fundacao)
    cliente.info_externas.calcular_movimentacao_de_mercado(cliente.n_titulos, cliente.n_fontes)
    cliente.info_externas.calcular_nivel_de_pontualidade_de_mercado(cliente.pontualidade)
    cliente.info_externas.calcular_maior_acumulo_mercado(cliente.acumulo_mercado)
    cliente.info_externas.identificar_socios_e_participacao(
        cliente.socio1, cliente.socio2, cliente.socio3, cliente.socio4, cliente.participacao_socio1,
        cliente.participacao_socio2, cliente.participacao_socio3, cliente.participacao_socio4,
    )
    cliente.info_externas.calcular_nivel_de_restricoes(cliente.restricoes, cliente.capital_social)

    lista_clientes.append(cliente)


