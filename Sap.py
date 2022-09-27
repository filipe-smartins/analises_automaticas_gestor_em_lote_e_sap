import win32com.client as win32  # pip install pywin32
from datetime import date, timedelta, datetime  # pip install datetime


def sap_cnpj():

    def conecta_no_sap():
        SapGuiAuto = win32.GetObject("SAPGUI")
        if not type(SapGuiAuto) == win32.CDispatch:
            return

        application = SapGuiAuto.GetScriptingEngine
        if not type(application) == win32.CDispatch:
            SapGuiAuto = None
            return

        connection = application.Children(0)
        if not type(connection) == win32.CDispatch:
            application = None
            SapGuiAuto = None
            return

        global session
        session = connection.Children(0)
        if not type(session) == win32.CDispatch:
            connection = None
            application = None
            SapGuiAuto = None
            return

    def pega_lc_e_ar(clientes):
        session.findById("wnd[0]/tbar[0]/okcd").Text = "ZBMFI313"
        session.findById("wnd[0]").sendVKey(0)
        limite_total = []
        contas_a_receber = []
        for indice in range(0, len(clientes['Código SAP do Cliente'])):

            if clientes['enviar_para_seguradoras'][indice] == 'nao':
                continue

            session.findById("wnd[0]/usr/ctxtP_KUNNR").text = clientes['Código SAP do Cliente'][indice]
            session.findById("wnd[0]/tbar[1]/btn[8]").press()

            linha = int(session.findById("wnd[0]/usr/cntlPAINEL/shellcont/shell/shellcont[1]/shell").RowCount) - 1
            valor = session.findById("wnd[0]/usr/cntlPAINEL/shellcont/shell/shellcont[1]/shell").getcellvalue(
                    linha,"KLIMK").strip().replace('.', '').replace(',', '.')

            if valor == '0.00' or valor == '':
                valor = 0
            else:
                valor = int(float(valor))

            limite_total.append(valor)

            valor_ar = session.findById("wnd[0]/usr/cntlPAINEL/shellcont/shell/shellcont[1]/shell").getcellvalue(
                    linha,"DIVIDA").strip().replace('.', '').replace(',', '.')

            if valor_ar == '0.00' or valor_ar == '':
                valor_ar = 0
            elif '-' in valor_ar:  # subistitui valores negativos por zero para evitar erros.
                valor_ar = 0
            else:
                valor_ar = int(float(valor_ar))

            contas_a_receber.append(valor_ar)

            session.findById("wnd[0]/tbar[0]/btn[3]").press()
        session.findById("wnd[0]/tbar[0]/btn[3]").press()
        clientes['Limite Anterior'] = limite_total
        clientes['Contas a Receber'] = contas_a_receber

    def calcula_historico_interno(clientes):
        # Busca informações do histórico interno do cliente:
        historico_cliente = {}

        for indice in range(0, len(clientes['Código SAP do Cliente'])):
            session.findById("wnd[0]/tbar[0]/okcd").Text = "FD32"
            session.findById("wnd[0]").sendVKey(0)
            session.findById("wnd[0]/usr/ctxtRF02L-KUNNR").text = clientes['Código SAP do Cliente'][indice]
            session.findById("wnd[0]/usr/ctxtRF02L-KKBER").text = "acss"

            session.findById("wnd[0]/usr/chkRF02L-D0105").selected = False
            session.findById("wnd[0]/usr/chkRF02L-D0110").selected = False
            session.findById("wnd[0]/usr/chkRF02L-D0120").selected = False
            session.findById("wnd[0]/usr/chkRF02L-D0210").selected = False
            session.findById("wnd[0]/usr/chkRF02L-D0220").selected = True
            session.findById("wnd[0]").sendVKey(0)

            data_hoje = date.today()
            periodo = []  # data do histórico apuardo
            valores = []  # valores dos acúmulos no SAP
            historico = []
            pontualidade = []  # armazena somente o histórico em que o atraso for < 5
            tempo_decorrido = []  # diferença entre a data de hoje e data do histórico apurado

            for i in range(0, 16):  # o range 0-16 se dá devido ao histórico no SAP estar limitado a 16 linhas.

                atraso = session.findById(f"wnd[0]/usr/tblSAPMF02CZAHLV_CONTROL/txtRF42B-VZSXX[4,{i}]").text

                if '-' in str(atraso):  # subistitui valores negativos por zero para evitar erros.
                    atraso = 0

                if '___' in str(atraso):  # para a execução caso o histórico seja menor do que 12 meses.
                    break
                historico.append(atraso)

                data_referencia = '01/' + session.findById(
                    f"wnd[0]/usr/tblSAPMF02CZAHLV_CONTROL/txtRF42B-KMONA[0,{i}]").text + '/' + session.findById(
                    f"wnd[0]/usr/tblSAPMF02CZAHLV_CONTROL/txtRF42B-KJAHR[1,{i}]").text
                periodo.append(datetime.strptime(data_referencia, "%d/%m/%Y").date())

                tempo_decorrido.append(abs((data_hoje - datetime.strptime(data_referencia, "%d/%m/%Y").date()).days))
                valor = session.findById(
                    f"wnd[0]/usr/tblSAPMF02CZAHLV_CONTROL/txtRF42B-AGSXX[3,{i}]").text.strip().replace('.', '').replace(
                    ',', '.')
                valores.append(int(float(valor) / 1000))

                if int(atraso) <= 5:  # insere na lista o histórico com atraso <5 para cálculo do índice de pontualidade
                    pontualidade.append(atraso)

            if len(periodo) == 0:
                texto_pontualidade = 'Cliente sem histórico interno.'
            elif sum(valores) < 100:  # soma dos acúmulos mensais menor do que 100KBRL
                texto_pontualidade = 'Cliente sem histórico interno relevante.'
            else:
                indice_pontualidade = int(len(pontualidade) / len(periodo) * 100)  # calcula o índice de pontualidade
                texto_pontualidade = f'''
                    HISTÓRICO GERAL:
                        O período do histórico contemplado é de {periodo[-1].year} até {periodo[0].year}.
                        O cliente apresentou pontualidade de {indice_pontualidade}%, tendo efetuado {len(periodo)} pagamentos 
                        no período e ficado pontual em {len(pontualidade)} deles.
                        O maior acúmulo foi de {max(valores, key=int)} KBRL ({round(max(valores, key=int) / 1000, 1)} milhões).
                        O valor total dos pagamentos neste período foi de {sum(valores)} KBRL ({round(sum(valores) / 1000, 1)} milhões). 
                    
                        Obs: Este cálculo considera como atraso somente o histórico mensal cuja média ficou acima de 5 dias.
                '''

            # CÁLCULOS PARA HISTÓRICO DE 12 MESES:

            historico_12meses = []
            valores_12meses = []
            pontualidade_12meses = []

            for i in range(0, len(periodo)):
                if tempo_decorrido[i] <= 365:
                    historico_12meses.append(historico[i])
                    valores_12meses.append(valores[i])
                    if int(historico[i]) <= 5:
                        pontualidade_12meses.append(historico[i])

            if len(historico_12meses) == 0:
                texto_pontualidade_12meses = 'Cliente sem histórico nos últimos 12 meses.'
            elif sum(valores_12meses) < 100:  # soma dos acúmulos mensais menor do que 100KBRL
                texto_pontualidade_12meses = 'Cliente sem histórico interno relevante nos últimos 12 meses.'
            else:
                indice_pontualidade_12meses = int(len(pontualidade_12meses) / len(historico_12meses) * 100)
                texto_pontualidade_12meses = f'''
                HISTÓRICO DOS ÚLTIMOS 12 MESES:
                    Nos últimos 12 meses o cliente apresentou pontualidade de {indice_pontualidade_12meses}%, sendo que 
                    efetuou {len(historico_12meses)} pagamentos e esteve pontual em {len(pontualidade_12meses)} deles.
                    O maior acúmulo foi de {max(valores_12meses, key=int)} KBRL ({round(max(valores_12meses, key=int) / 1000, 1)} milhões).
                    O valor total dos pagamentos neste período foi de {sum(valores_12meses)} KBRL ({round(sum(valores_12meses) / 1000, 1)} milhões).'''

            if clientes['Limite Anterior'][indice] // 1000 < 50 and clientes['Contas a Receber'][indice] // 1000 < 50:
                texto_limite_e_ar = ''
            else:
                texto_limite_e_ar = f'''
                INFORMAÇÕES INTERNAS:
                    O cliente possui atualmente limite de crédito de {clientes['Limite Anterior'][indice] // 1000} KBRL e
                    seu contas a receber é de {clientes['Contas a Receber'][indice] // 1000} KBRL.'''

            historico_cliente[clientes['Código SAP do Cliente'][indice]] = texto_limite_e_ar + texto_pontualidade_12meses + texto_pontualidade

            # Volta para tela inicial do SAP
            session.findById("wnd[0]/tbar[0]/btn[15]").press()
            try:
                session.findById("wnd[1]/tbar[0]/btn[0]").press()
            except:
                pass

        for cliente in historico_cliente[clientes['Código SAP do Cliente'][indice]]:
            print(cliente)

    conecta_no_sap()
    pega_lc_e_ar()
    calcula_historico_interno()
