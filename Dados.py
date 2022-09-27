from os.path import expanduser
import pandas as pd
import sqlite3

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


class DadosClientes:
    def __init__(self):
        self.dados_clientes = {}

    @staticmethod
    def definir_nomes_e_tipos_colunas():
        formato = {
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
        novos_nomes_colunas = {}
        for key in formato.keys():
            dtype[key] = formato[key][1]
            novos_nomes_colunas[key] = formato[key][0]

        return dtype, novos_nomes_colunas, formato

    def carregar_dados_do_arquivo(self):
        dtype, novos_nomes_colunas, formato = self.definir_nomes_e_tipos_colunas()

        dados = pd.read_csv(fr'{file_path}\Exporta.csv', sep=';', encoding='utf-8', dtype=dtype, usecols=formato.keys())

        dados = dados.rename(columns=novos_nomes_colunas)  # renomeia colunas do dataframe
        dados = dados.reindex(columns=novos_nomes_colunas.values())  # ordena as colunas do df de acordo com a lista
        dados = dados.fillna('')
        dados = dados.to_dict('list')
        self.dados_clientes = dados
