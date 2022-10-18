from datetime import date, datetime  # pip install datetime


class InformacoesInternas:
    def __init__(self):
        self.a = None

    def calcula_historico_interno(self):
        # Busca informações do histórico interno do cliente:

        for i in range(0, len(self.clientes.dados_clientes['Código SAP do Cliente'])):
            self.session.findById("wnd[0]/tbar[0]/okcd").Text = "FD32"
            self.session.findById("wnd[0]").sendVKey(0)
            self.session.findById("wnd[0]/usr/ctxtRF02L-KUNNR").text = self.clientes.dados_clientes['Código SAP do Cliente'][i]
            self.session.findById("wnd[0]/usr/ctxtRF02L-KKBER").text = "acss"

            self.session.findById("wnd[0]/usr/chkRF02L-D0105").selected = False
            self.session.findById("wnd[0]/usr/chkRF02L-D0110").selected = False
            self.session.findById("wnd[0]/usr/chkRF02L-D0120").selected = False
            self.session.findById("wnd[0]/usr/chkRF02L-D0210").selected = False
            self.session.findById("wnd[0]/usr/chkRF02L-D0220").selected = True
            self.session.findById("wnd[0]").sendVKey(0)

            data_hoje = date.today()
            periodo = []  # data do histórico apuardo
            valores = []  # valores dos acúmulos no SAP
            historico = []
            pontualidade = []  # armazena somente o histórico em que o atraso for < 5
            tempo_decorrido = []  # diferença entre a data de hoje e data do histórico apurado

            for i in range(0, 16):  # o range 0-16 se dá devido ao histórico no SAP estar limitado a 16 linhas.

                atraso = self.session.findById(f"wnd[0]/usr/tblSAPMF02CZAHLV_CONTROL/txtRF42B-VZSXX[4,{i}]").text

                if '-' in str(atraso):  # subistitui valores negativos por zero para evitar erros.
                    atraso = 0

                if '___' in str(atraso):  # para a execução caso o histórico seja menor do que 12 meses.
                    break
                historico.append(atraso)

                data_referencia = '01/' + self.session.findById(
                    f"wnd[0]/usr/tblSAPMF02CZAHLV_CONTROL/txtRF42B-KMONA[0,{i}]").text + '/' + self.session.findById(
                    f"wnd[0]/usr/tblSAPMF02CZAHLV_CONTROL/txtRF42B-KJAHR[1,{i}]").text
                periodo.append(datetime.strptime(data_referencia, "%d/%m/%Y").date())

                tempo_decorrido.append(abs((data_hoje - datetime.strptime(data_referencia, "%d/%m/%Y").date()).days))
                valor = self.session.findById(
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

            if self.clientes.dados_clientes['Limite Anterior'][i] // 1000 < 50 and self.clientes.dados_clientes['Contas a Receber'][i] // 1000 < 50:
                texto_limite_e_ar = ''
            else:
                texto_limite_e_ar = f'''
                INFORMAÇÕES INTERNAS:
                    O cliente possui atualmente limite de crédito de {self.clientes.dados_clientes['Limite Anterior'][i] // 1000} KBRL e
                    seu contas a receber é de {self.clientes.dados_clientes['Contas a Receber'][i] // 1000} KBRL.'''

            self.clientes.dados_clientes['historico_interno'][i] = texto_limite_e_ar + texto_pontualidade_12meses + texto_pontualidade

            # Volta para tela inicial do SAP
            self.session.findById("wnd[0]/tbar[0]/btn[15]").press()
            try:
                self.session.findById("wnd[1]/tbar[0]/btn[0]").press()
            except:
                pass

            print(self.clientes.dados_clientes['historico_interno'][i])

