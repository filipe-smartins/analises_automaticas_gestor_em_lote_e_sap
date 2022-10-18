from os.path import expanduser
import pandas as pd
import sqlite3
import win32com.client as win32  # pip install pywin32
from datetime import date, datetime  # pip install datetime
from pyautogui import alert

home = expanduser("~")
sharepoint_path = fr'{home}\ArcelorMittal\Dados da VP Corporativa de Finanças e TI - Crédito Corporativo'
file = fr'{home}\OneDrive - ArcelorMittal\Documents\Exporta.csv'


def alimentar_bd_em_massa():
    try:
        dados = pd.read_csv(file, sep=';', encoding='utf-8')
    except UnicodeDecodeError:
        dados = pd.read_csv(file, sep=';', encoding='latin-1')

    dados.rename(columns={'LOGON': 'LOGON SERASA'}, inplace=True)
    dados = dados.drop(columns=['DATA FUNDACAO', 'RECEITA - RAZAO SOCIAL'])  # del(dados['DATA FUNDACAO'])

    conn = sqlite3.connect(fr'{sharepoint_path}\Automações\Banco de Dados\database.db')
    dados.to_sql(name=f'gestor', con=conn, if_exists='append', index=True)
    conn.commit()  # comando para gravar os dados no Banco de Dados
    conn.close()  # fecha a conecção com o banco de dados


class Dados:
    def __init__(self):
        self.dados_clientes = {}
        self.definir_nomes_e_tipos_colunas()
        self.carregar_dados_do_arquivo()
        self.conectar_no_sap()
        self.buscar_lc_e_ar_sap()
        self.buscar_historico_interno_sap()

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
            '- D) DU_CODIGO_DO_CLIENTE -': ['Código SAP do Cliente', str],
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

        dados = pd.read_csv(file, sep=';', encoding='utf-8', dtype=dtype, usecols=formato.keys())

        dados = dados.rename(columns=novos_nomes_colunas)  # renomeia colunas do dataframe
        dados = dados.reindex(columns=novos_nomes_colunas.values())  # ordena as colunas do df de acordo com a lista
        dados = dados.fillna('')
        dados = dados.to_dict('list')
        self.dados_clientes = dados

    def conectar_no_sap(self):
        sapgui = win32.GetObject("SAPGUI").GetScriptingEngine

        try:
            self.session = sapgui.FindById("ses[0]")
            self.session.createSession()
        except BaseException:  # pywintypes.com_error
            alert("ERRO AO CONECTAR AO SAP. Certifique-se que o SAP esteja aberto, com a sessão 0 na tela inicial. "
                  "Caso o erro persista, feche e reabra o SAP com uma janela única.")
            self.conecta_no_sap()

    def buscar_lc_e_ar_sap(self):
        self.session.findById("wnd[0]/tbar[0]/okcd").Text = "ZBMFI313"
        self.session.findById("wnd[0]").sendVKey(0)
        limite_total = []
        contas_a_receber = []
        for i in range(0, len(self.dados_clientes['Código SAP do Cliente'])):
            self.session.findById("wnd[0]/usr/ctxtP_KUNNR").text = \
                self.dados_clientes['Código SAP do Cliente'][i]
            self.session.findById("wnd[0]/tbar[1]/btn[8]").press()

            linha = int(self.session.findById("wnd[0]/usr/cntlPAINEL/shellcont/shell/shellcont[1]/shell").RowCount) - 1
            valor = self.session.findById("wnd[0]/usr/cntlPAINEL/shellcont/shell/shellcont[1]/shell").getcellvalue(
                linha, "KLIMK").strip().replace('.', '').replace(',', '.')

            if valor == '0.00' or valor == '':
                valor = 0
            else:
                valor = int(float(valor))

            limite_total.append(valor)

            valor_ar = self.session.findById("wnd[0]/usr/cntlPAINEL/shellcont/shell/shellcont[1]/shell").getcellvalue(
                linha, "DIVIDA").strip().replace('.', '').replace(',', '.')

            if valor_ar == '0.00' or valor_ar == '':
                valor_ar = 0
            elif '-' in valor_ar:  # subistitui valores negativos por zero para evitar erros.
                valor_ar = 0
            else:
                valor_ar = int(float(valor_ar))

            contas_a_receber.append(valor_ar)

            self.session.findById("wnd[0]/tbar[0]/btn[3]").press()
        self.session.findById("wnd[0]/tbar[0]/btn[3]").press()
        self.dados_clientes['Limite Anterior'] = limite_total
        self.dados_clientes['Contas a Receber'] = contas_a_receber

    def buscar_historico_interno_sap(self):
        # Busca informações do histórico interno do cliente:

        data_hoje = date.today()
        ano_historico_interno = []  # data do histórico apuardo
        mes_historico_interno = []  # data do histórico apuardo
        valores_historico_interno = []  # valores dos acúmulos no SAP
        dias_atraso_interno = []
        meses_pontuais_internamente = []  # armazena somente o histórico em que o atraso for < 5

        historico_interno_12meses = []
        valores_interno_12meses = []
        meses_pontuais_internamente_12meses = []

        for i in range(0, len(self.dados_clientes['Código SAP do Cliente'])):
            self.session.findById("wnd[0]/tbar[0]/okcd").Text = "FD32"
            self.session.findById("wnd[0]").sendVKey(0)
            self.session.findById("wnd[0]/usr/ctxtRF02L-KUNNR").text = self.dados_clientes['Código SAP do Cliente'][i]
            self.session.findById("wnd[0]/usr/ctxtRF02L-KKBER").text = "acss"

            self.session.findById("wnd[0]/usr/chkRF02L-D0105").selected = False
            self.session.findById("wnd[0]/usr/chkRF02L-D0110").selected = False
            self.session.findById("wnd[0]/usr/chkRF02L-D0120").selected = False
            self.session.findById("wnd[0]/usr/chkRF02L-D0210").selected = False
            self.session.findById("wnd[0]/usr/chkRF02L-D0220").selected = True
            self.session.findById("wnd[0]").sendVKey(0)

            ano_historico = []  # data do histórico apuardo
            mes_historico = []  # data do histórico apuardo
            valores_historico = []  # valores dos acúmulos no SAP
            dias_atraso = []
            meses_pontuais = []  # armazena somente o histórico em que o atraso for < 5
            tempo_decorrido_historico = []  # diferença entre a data de hoje e data do histórico apurado

            for i in range(0, 16):  # o range 0-16 se dá devido ao histórico no SAP estar limitado a 16 linhas.

                atraso = self.session.findById(f"wnd[0]/usr/tblSAPMF02CZAHLV_CONTROL/txtRF42B-VZSXX[4,{i}]").text

                if '-' in str(atraso):  # subistitui valores negativos por zero para evitar erros.
                    atraso = 0

                if '___' in str(atraso):  # para a execução caso o histórico seja menor do que 12 meses.
                    break
                dias_atraso.append(atraso)

                data_referencia = '01/' + self.session.findById(
                    f"wnd[0]/usr/tblSAPMF02CZAHLV_CONTROL/txtRF42B-KMONA[0,{i}]").text + '/' + self.session.findById(
                    f"wnd[0]/usr/tblSAPMF02CZAHLV_CONTROL/txtRF42B-KJAHR[1,{i}]").text
                ano_historico.append(datetime.strptime(data_referencia, "%d/%m/%Y").year)
                mes_historico.append(datetime.strptime(data_referencia, "%d/%m/%Y").month)

                tempo_decorrido_historico.append(
                    abs((data_hoje - datetime.strptime(data_referencia, "%d/%m/%Y").date()).days))
                valor = self.session.findById(
                    f"wnd[0]/usr/tblSAPMF02CZAHLV_CONTROL/txtRF42B-AGSXX[3,{i}]").text.strip().replace('.', '').replace(
                    ',', '.')
                valores_historico.append(int(float(valor) / 1000))

                if int(atraso) <= 5:  # insere na lista o histórico com atraso <5 para cálculo do índice de pontualidade
                    meses_pontuais.append(atraso)

            ano_historico_interno.append(ano_historico)
            mes_historico_interno.append(mes_historico)
            valores_historico_interno.append(valores_historico)
            dias_atraso_interno.append(dias_atraso)
            meses_pontuais_internamente.append(meses_pontuais)

            historico_12meses = []
            valores_12meses = []
            meses_pontuais_12meses = []

            for i in range(0, len(ano_historico)):
                if tempo_decorrido_historico[i] <= 365:
                    historico_12meses.append(dias_atraso[i])
                    valores_12meses.append(valores_historico[i])
                    if int(dias_atraso[i]) <= 5:
                        meses_pontuais_12meses.append(dias_atraso[i])

            historico_interno_12meses.append(historico_12meses)
            valores_interno_12meses.append(valores_12meses)
            meses_pontuais_internamente_12meses.append(meses_pontuais_12meses)

            # Volta para tela inicial do SAP
            self.session.findById("wnd[0]/tbar[0]/btn[15]").press()
            try:
                self.session.findById("wnd[1]/tbar[0]/btn[0]").press()
            except:
                pass

        self.dados_clientes['ano_historico_interno'] = ano_historico_interno
        self.dados_clientes['mes_historico_interno'] = mes_historico_interno
        self.dados_clientes['valores_historico_interno'] = valores_historico_interno
        self.dados_clientes['dias_atraso_interno'] = dias_atraso_interno
        self.dados_clientes['meses_pontuais_internamente'] = meses_pontuais_internamente

        self.dados_clientes['historico_interno_12meses'] = historico_interno_12meses
        self.dados_clientes['valores_interno_12meses'] = valores_interno_12meses
        self.dados_clientes['meses_pontuais_internamente_12meses'] = meses_pontuais_internamente_12meses
