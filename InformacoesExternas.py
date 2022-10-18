class InformacoesExternas:
    def __init__(self):
        self.tempo_de_mercado = None
        self.movimentacao_de_mercado = None
        self.nivel_de_pontualidade_de_mercado = None
        self.maior_acumulo_mercado = None
        self.socios_e_participacao = None
        self.nivel_de_restricoes = None

    def calcular_tempo_de_mercado(self, tempo_de_fundacao):
        anos_constituicao = int(tempo_de_fundacao.split(',')[0])
        meses_constituicao = int((int(tempo_de_fundacao.split(',')[1]) / 100) * 12)

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

        self.tempo_de_mercado = lv_tempo_de_mercado

    def calcular_movimentacao_de_mercado(self, qtde_titulos, qtde_fontes):
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

        self.movimentacao_de_mercado = lv_movimentacao_de_mercado

    def calcular_nivel_de_pontualidade_de_mercado(self, indice_pontualidade):
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

        self.nivel_de_pontualidade_de_mercado = lv_pontualidade

    def calcular_maior_acumulo_mercado(self, acumulo_mercado):
        acumulo = float(acumulo_mercado.replace('#', '0').split("à")[1].strip().split()[0])
        expressao = acumulo_mercado.replace('#', '0').split("à")[1].strip().split()[1]

        if expressao == 'Mil':
            multiplicador = 1
        elif expressao == 'Mi':
            multiplicador = 1000

        acumulo = int(acumulo * multiplicador)

        self.maior_acumulo_mercado = acumulo

    def identificar_socios_e_participacao(self, socio1, socio2, socio3, socio4, partic1, partic2, partic3, partic4):

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

        self.socios_e_participacao = socio

    def calcular_nivel_de_restricoes(self, info_restricoes, valor_capital_social):
        lv_restricoes = int(float(info_restricoes.replace('#', '0').replace('.', '').replace(',', '.'))) // 1000
        lv_capital_social = int(valor_capital_social.replace('.', '')) // 1000
        lv_acumulo_mercado = self.maior_acumulo_mercado

        if lv_restricoes == 0:
            texto_restricoes = 'Sem restrições no mercado.'
        else:

            try:
                indice1 = lv_restricoes / lv_capital_social * 100
            except ZeroDivisionError:
                indice1 = 0
            try:
                indice2 = lv_restricoes / lv_acumulo_mercado * 100
            except ZeroDivisionError:
                indice2 = 0

            if indice1 < 2 and indice2 < 10:
                texto_restricoes = f'Apresenta restrições de {lv_restricoes} KBRL, IRRELEVANTES no mercado ' \
                                   f'em comparação ao Capital Social ({indice1}%) e acúmulos de mercado ({indice2}%).'
            elif indice1 < 5 and indice2 < 15:
                texto_restricoes = f'Apresenta restrições de {lv_restricoes} KBRL, nível ACEITÁVEL ' \
                                   f'em comparação ao Capital Social ({indice1}%) e acúmulos de mercado ({indice2}%).'
            elif indice1 < 10 and indice2 < 20:
                texto_restricoes = f'Apresenta restrições de {lv_restricoes} KBRL, nível PREOCUPANTE ' \
                                   f'em comparação ao Capital Social ({indice1}%) e acúmulos de mercado ({indice2}%).'
            elif indice1 < 15 and indice2 < 30:
                texto_restricoes = f'Apresenta restrições de {lv_restricoes} KBRL, nível MUITO PREOCUPANTE ' \
                                   f'em comparação ao Capital Social ({indice1}%) e acúmulos de mercado ({indice2}%).'
            elif indice1 < 20 and indice2 < 50:
                texto_restricoes = f'Apresenta restrições de {lv_restricoes} KBRL, nível ALTO ' \
                                   f'em comparação ao Capital Social ({indice1}%) e acúmulos de mercado ({indice2}%.).'
            elif indice1 < 30 and indice2 < 60:
                texto_restricoes = f'Apresenta restrições de {lv_restricoes} KBRL, nível MUITO ALTO ' \
                                   f'em comparação ao Capital Social ({indice1}%) e acúmulos de mercado ({indice2}%).'
            else:
                texto_restricoes = f'Apresenta restrições de {lv_restricoes} KBRL, nível ALTÍSSIMO ' \
                                   f'em comparação ao Capital Social ({indice1}%) e acúmulos de mercado ({indice2}%).'

        self.nivel_de_restricoes = texto_restricoes

