class Clientes:

    def __init__(
            self, data_constitucao, limite_solicitado, capital_social, socio1, socio2, socio3, socio4,
            participacao_socio1, participacao_socio2, participacao_socio3, participacao_socio4,
            ramo, pontualidade, n_titulos, n_fontes, acumulo_mercado, restricoes, cliente_novo,
            alerta_negocios, recomendacao_gestor, porte, tempo_de_fundacao,
            codigo, limite_anterior, contas_a_receber, ano_historico_interno, mes_historico_interno,
            valores_historico_interno, dias_atraso_interno, meses_pontuais_internamente, historico_interno_12meses,
            valores_interno_12meses, meses_pontuais_internamente_12meses, info_internas, info_externas
    ):

        self.data_constitucao = data_constitucao
        self.limite_solicitado = limite_solicitado
        self.capital_social = capital_social
        self.socio1 = socio1
        self.socio2 = socio2
        self.socio3 = socio3
        self.socio4 = socio4
        self.participacao_socio1 = participacao_socio1
        self.participacao_socio2 = participacao_socio2
        self.participacao_socio3 = participacao_socio3
        self.participacao_socio4 = participacao_socio4
        self.ramo = ramo
        self.pontualidade = pontualidade
        self.n_titulos = n_titulos
        self.n_fontes = n_fontes
        self.acumulo_mercado = acumulo_mercado
        self.restricoes = restricoes
        self.cliente_novo = cliente_novo
        self.alerta_negocios = alerta_negocios
        self.recomendacao_gestor = recomendacao_gestor
        self.porte = porte
        self.tempo_de_fundacao = tempo_de_fundacao

        self.codigo = codigo
        self.limite_anterior = limite_anterior
        self.contas_a_receber = contas_a_receber
        self.ano_historico_interno = ano_historico_interno
        self.mes_historico_interno = mes_historico_interno
        self.valores_historico_interno = valores_historico_interno
        self.dias_atraso_interno = dias_atraso_interno
        self.meses_pontuais_internamente = meses_pontuais_internamente
        self.historico_interno_12meses = historico_interno_12meses
        self.valores_interno_12meses = valores_interno_12meses
        self.meses_pontuais_internamente_12meses = meses_pontuais_internamente_12meses

        self.info_internas = info_internas
        self.info_externas = info_externas

        # self.informacoes_internas = ''
        # self.informacoes_mercado = ''






list = ['Data de Constituição', 'Limite solicitado', 'Capital Social', 'Sócio 1', 'Sócio 2', 'Sócio 3', 'Sócio 4',
        'Participação Sócio 1', 'Participação Sócio 2', 'Participação Sócio 3', 'Participação Sócio 4', 'Ramo de atuação',
        '% de pontualidade', 'Número de títulos', 'Número de fontes', 'Valor do maior acumulo', 'Total de restrições',
        'Cliente Novo', 'Alerta de Negócio', 'Recomendacao gestor', 'Porte da empresa', 'Código SAP do Cliente',
        'Tempo Fundação', 'Limite Anterior', 'Contas a Receber', 'ano_historico_interno', 'valores_historico_interno',
        'dias_atraso_interno', 'meses_pontuais_internamente', 'historico_interno_12meses', 'valores_interno_12meses',
        'meses_pontuais_internamente_12meses']


data = {'Data de Constituição': ['07/10/2019', '23/04/1999', '04/11/1997', '10/02/2020', '07/08/2012', '01/10/2002',
                                 '20/09/2012', '24/09/2021', '25/08/2015', '15/01/2011', '05/09/2019', '10/04/2006',
                                 '09/11/2016', '18/01/2022', '03/05/2018', '29/01/2021', '15/03/1974', '23/07/2008',
                                 '21/07/2005', '25/10/1988', '10/09/2020', '15/03/2000', '26/08/2003', '25/06/1996',
                                 '12/07/2004', '29/06/2001', '17/03/2021', '28/06/2021', '04/02/1993', '22/10/2007',
                                 '04/11/2015', '31/10/1997', '10/07/2002', '25/01/2000', '22/03/2012', '13/02/2007'],
        'Limite solicitado': ['80.000,00', '170.000,00', '500.000,00', '500.000,00', '300.000,00', '110.000,00',
                              '50.000,00', '300.000,00', '130.000,00', '490.000,00', '300.000,00', '120.000,00',
                              '450.000,00', '250.000,00', '250.000,00', '250.000,00', '200.000,00', '150.000,00',
                              '155.000,00', '140.000,00', '800.000,00', '320.000,00', '650.000,00', '159.000,00',
                              '30.000,00', '450.000,00', '80.000,00', '110.000,00', '300.000,00', '250.000,00',
                              '175.000,00', '88.000,00', '250.000,00', '2.000.000,00', '200.000,00', '150.000,00'],
        'Capital Social': ['10.000', '900.000', '60.000', '1.000', '4.000.000', '1.000.000', '170.000', '10.000',
                           '40.000', '210.000', '50.000', '250.000', '88.000', '1', '600.000', '200.000', '15.000',
                           '2.400.000', '70.000', '120.000', '9.000.000', '900.000', '350.000', '150.000', '400.000',
                           '200.000', '10.000', '110.000', '2', '15.000', '300.000', '21.000', '1.850.000',
                           '119.895.000', '152.720.397', '150.000'],
        'Sócio 1': ['HUGO ENGENHARIA LTDA', 'DENI DE OLIVEIRA BASGAL', 'ARLINDO LAZZARETTI',
                    'ROTTAS CONSTRUTORA E INCORPORADORA LTDA', 'DARIO MAGALHAES FILHO', 'JOSE ROBERTO BRANCO RAMOS',
                    'RODRIGO BURIGO NIERO', 'SANTA HELENA S A INCORPORACOES E CONSTRUCOES',
                    'RAIMUNDO NONATO SILVA DE SOUSA', 'FABRICIO MANOEL DE CARVALHO', 'TIAGO LEAO DA SILVA',
                    'MARIA MADALENA DE SOUSA DOURADO', 'PEDRO RIBEIRO DE CASTRO', 'CONSTRUTORA AUGUSTO VELLOSO S/A',
                    'GENESIO MENICHETTI', 'CARLOS RAPHAEL DE OLIVEIRA REIS', 'NARSON DE SOUZA E SILVA',
                    'NILSON JOSE GOEDERT', 'ERISVALDO PEREIRA DE SOUZA', 'EDILSON MALCHER MUNIZ', 'NAZCA LTDA',
                    'GIOVANI OLINTO MILANESI', 'MARIA SILVIA FRANCO PEREIRA', 'SEBASTIAO RAIMUNDO BRANCHES DA GAMA',
                    'MARIA AMELIA ARAUJO DA SILVA', 'ERNESTO CESAR GIANTOMASSI', 'PACAEMBU CONSTRUTORA S/A',
                    'VALDINEI DA SILVA ALMEIDA', '#', 'JAQUELINE MARIA SCHMITZ MILANESI',
                    'ELZA MARIA DOS SANTOS TAVARES', 'VANTOIR ROBERTO GAIO', 'JIVAGO DE CASTRO RAMALHO',
                    'A 5 ADMINISTRADORA DE PARTICIPACOES S/A', 'ETERNIT S A EM RECUPERACAO JUDICIAL',
                    'FABIULA FLORIANO DA SILVA ROCHA'],
        'Sócio 2': ['MARCELO CHIBENI', 'DANILO DE OLIVEIRA BASGAL', 'LUCIANE LAZZARETTI', '#', 'DARIO MAGALHAES NETO',
                    'FELIPE RODRIGUES BRANCO', 'LILIANE MATIOLA REDIVO', '#', '#', 'DEIVID MANOEL CARVALHO DIEL', '#',
                    'CHARLITON CORREA', 'SAULO RODRIGUES MIRANDA', 'VAD ENGENHARIA E EMPREENDIMENTOS LTDA',
                    'LUIZ PAULO BELLINI', '#', 'ARTHUR ALBANI MARCHEZI', 'ROGER ALCANTARA DE FARIA',
                    'JANE REGINA CARLOS MOTA', 'EDILSON MARTINS MUNIZ', '#', 'MENOR DE IDADE', 'WILSON LUIZ PEREIRA',
                    'ZULMA MARIA TAVARES GAMA', '#', 'RONEY MARCOS MARTINS CORDEIRO',
                    'HAUS COMPRA E VENDA DE BENS IMOVEIS LTDA', '#', '#', 'MENOR DE IDADE', '#', 'VOLNEI ANTONIO GAIO',
                    'LAURA VERBICARO CASTRO', 'SANTORINI PARTICIPACOES S/A', 'COMPANIA COLOMBIANA DE CERAMICA S/A',
                    'ALESSANDRO MENDES ROCHA'],
        'Sócio 3': ['HILTON HUGO DA SILVA FABBRI', '#', 'CRISTIANE LAZZARETTI', '#', 'DANILO QUINTO MAGALHAES',
                    'RODRIGO RODRIGUES BRANCO', '#', '#', '#', 'FABIO SUMARA CUSTODIO', '#', '#', '#', '#', '#', '#',
                    '#', 'JAIME ANDRADE RAMOS', '#', 'OCEANIRA MARIA MALCHER MUNIZ', '#', '#', '#', '#', '#', '#', '#',
                    '#', '#', '#', '#', 'CLAITON VOLMIR GAIO', '#', '#', '#', '#'],
        'Sócio 4': ['#', '#', 'GIOVANE LAZZARETTI', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
                    '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        'Participação Sócio 1': ['0', '75', '70', '100', '90', '67', '90', '0', '100', '47,5', '100', '50', '80', '84',
                                 '50', '100', '95', '33,3', '50', '50', '100', '99', '50', '90', '100', '99', '99',
                                 '100', '#', '99', '100', '33,3', '99', '91,6', '60', '50'],
        'Participação Sócio 2': ['0', '25', '10', '#', '5', '16,5', '10', '#', '#', '47,5', '#', '50', '20', '16', '50',
                                 '#', '5', '33,3', '50', '40', '#', '1', '50', '10', '#', '1', '1', '#', '#', '1', '#',
                                 '33,3', '1', '8,3', '0', '50'],
        'Participação Sócio 3': ['0', '#', '10', '#', '5', '16,5', '#', '#', '#', '5', '#', '#', '#', '#', '#', '#',
                                 '#', '33,3', '#', '10', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '33,3',
                                 '#', '#', '#', '#'],
        'Participação Sócio 4': ['#', '#', '10', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
                                 '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
                                 '#', '#'],
        'Ramo de atuação': ['CONSTRUCAO E INCORPORACAO DE IMOVEIS', 'EMPREITEIRA', 'METALURGIA',
                            'CONSTRUCAO E INCORPORACAO DE IMOVEIS', 'CONSTRUCAO E INCORPORACAO DE IMOVEIS',
                            'CONSTRUCAO E INCORPORACAO DE IMOVEIS', 'CONSTRUCAO E INCORPORACAO DE IMOVEIS',
                            'CONSTRUCAO E INCORPORACAO DE IMOVEIS', 'COM DE MATERIAL PARA CONSTRUCAO',
                            'SERVICOS DE ENGENHARIA E ARQUITETURA', 'COM DE FERRAMENTAS E FERRAGENS',
                            'CONSTRUCAO E INCORPORACAO DE IMOVEIS', 'INDUSTRIA', 'EMPREITEIRA',
                            'ADMINISTRADORA DE BENS PROPRIOS', 'CONSTRUCAO E INCORPORACAO DE IMOVEIS',
                            'IND DE ARTEFATOS DE GESSO', 'CONSTRUCAO E INCORPORACAO DE IMOVEIS',
                            'TRANSPORTE RODOVIARIO DE CARGAS', 'IND DE ARTEFATOS DE CIMENTO',
                            'VENDA DE IMOVEIS PROPRIOS', 'CONSTRUCAO E INCORPORACAO DE IMOVEIS',
                            'COM DE FERRAMENTAS E FERRAGENS', 'COM DE FERRAMENTAS E FERRAGENS',
                            'COM DE MATERIAL PARA CONSTRUCAO', 'IND DE ESTRUTURAS METALICAS',
                            'CONSTRUCAO E INCORPORACAO DE IMOVEIS', 'COM DE MATERIAL PARA CONSTRUCAO',
                            'COOPERATIVA DE SERV MEDICOS E ODONTOLOGICOS', 'TRANSPORTE RODOVIARIO DE CARGAS',
                            'COM DE MATERIAL PARA CONSTRUCAO', 'IND DE MAQUINAS E EQUIPAMENTOS AGRICOLAS',
                            'CONSTRUCAO E INCORPORACAO DE IMOVEIS', 'COM DE MATERIAL PARA CONSTRUCAO',
                            'IND DE LOUCAS SANITARIAS', 'COM DE MATERIAL PARA CONSTRUCAO'],
        '% de pontualidade': ['97% à 100%', '97% à 100%', '97% à 100%', '95% à 97%', '97% à 100%', '97% à 100%',
                              '97% à 100%', '#', '97% à 100%', '97% à 100%', '97% à 100%', '87% à 89%', '97% à 100%',
                              '91% à 93%', '97% à 100%', '93% à 95%', '97% à 100%', '97% à 100%', '97% à 100%',
                              '83% à 85%', '97% à 100%', '97% à 100%', '97% à 100%', '95% à 97%', '97% à 100%',
                              '97% à 100%', '97% à 100%', '97% à 100%', '97% à 100%', '97% à 100%', '87% à 89%',
                              '97% à 100%', '79% à 81%', '91% à 93%', '45% à 47%', '97% à 100%'],
        'Número de títulos': ['16', '16', '18', '29', '5', '398', '220', 'NÒo encontrado', '196', '523', '149', '82',
                              '206', '73', '1', '17', '133', '330', '87', '54', '9', '261', '503', '342', '40', '73',
                              '7', '46', '54', '10', '761', '76', '151', '13.039,00', '43', '52'],
        'Número de fontes': ['6', '1', '3', '7', '2', '21', '13', '0', '4', '29', '8', '7', '19', '11', '1', '3', '3',
                             '12', '7', '3', '5', '13', '17', '22', '7', '12', '4', '3', '4', '3', '35', '8', '12',
                             '165', '1', '3'],
        'Valor do maior acumulo': ['B19 | De 13 Mil à 15 Mil', 'B4 | De 3 Mil à 3.5 Mil', 'B18 | De 10 Mil à 13 Mil',
                                   'B15 | De 8.5 Mil à 9 Mil', 'B4 | De 3 Mil à 3.5 Mil', 'C12 | De 200 Mil à 300 Mil',
                                   'C11 | De 100 Mil à 200 Mil', 'B1 | De 1.5 Mil à 2 Mil', 'C10 | De 70 Mil à 100 Mil',
                                   'C13 | De 300 Mil à 400 Mil', 'C11 | De 100 Mil à 200 Mil',
                                   'C11 | De 100 Mil à 200 Mil', 'C12 | De 200 Mil à 300 Mil',
                                   'C9 | De 50 Mil à 70 Mil', 'B6 | De 4 Mil à 4.5 Mil', 'C10 | De 70 Mil à 100 Mil',
                                   'C6 | De 43 Mil à 45 Mil', 'C11 | De 100 Mil à 200 Mil', 'B24 | De 25 Mil à 27 Mil',
                                   'C9 | De 50 Mil à 70 Mil', 'B22 | De 20 Mil à 23 Mil', 'C11 | De 100 Mil à 200 Mil',
                                   'C20 | De 1 Mi à 1.5 Mi', 'C11 | De 100 Mil à 200 Mil', 'C12 | De 200 Mil à 300 Mil',
                                   'C11 | De 100 Mil à 200 Mil', 'C12 | De 200 Mil à 300 Mil',
                                   'C11 | De 100 Mil à 200 Mil', 'C10 | De 70 Mil à 100 Mil', 'B4 | De 3 Mil à 3.5 Mil',
                                   'C10 | De 70 Mil à 100 Mil', 'B11 | De 6.5 Mil à 7 Mil',
                                   'C12 | De 200 Mil à 300 Mil', 'D13 | De 10 Mi à 15 Mi', 'C25 | De 3.5 Mi à 4 Mi',
                                   'C11 | De 100 Mil à 200 Mil'],
        'Total de restrições': ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '68', '0', '0', '0', '0', '0',
                                '700,3', '0', '51.887,95', '0', '0', '0', '0', '54.441,65', '0', '0', '0', '0', '0',
                                '0', '0', '0', '429,18', '840', '0'],
        'Cliente Novo': ['SIM', 'NAO', 'SIM', 'SIM', 'SIM', 'SIM', 'NAO', 'SIM', 'NAO', 'NAO', 'NAO', 'NAO', 'NAO',
                         'SIM', 'SIM', 'SIM', 'SIM', 'NAO', 'SIM', 'NAO', 'SIM', 'NAO', 'NAO', 'NAO', 'NAO', 'NAO',
                         'SIM', 'NAO', 'SIM', 'SIM', 'SIM', 'SIM', 'SIM', 'NAO', 'SIM', 'NAO'],
        'Alerta de Negócio': ['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N',
                              'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N'],
        'Recomendacao gestor': ['RATING B',
                                'RATING B // RESSALVA - SÓCIO(S) COM OCORRÊNCIA(S) DE AÇÕESS JUDICIAIS. // RESSALVA - SÓCIO(S) COM OCORRÊNCIA(S) DE PENDÊNCIA FINANCEIRA (PEFIN).',
                                'RATING B // RESSALVA - SÓCIO(S) COM OCORRÊNCIA(S) DE PROTESTOS.',
                                'RATING B // RESSALVA - SÓCIO(S) COM OCORRÊNCIA(S) DE PENDÊNCIA FINANCEIRA (REFIN).',
                                'RATING B // RESSALVA - SÓCIO(S) COM OCORRÊNCIA(S) DE PENDÊNCIA FINANCEIRA (PEFIN). // RESSALVA - SÓCIO(S) COM OCORRÊNCIA(S) DE PROTESTOS.',
                                'RATING B',
                                'RATING A // RESSALVA - SÓCIO(S) COM OCORRÊNCIA(S) DE AÇÕES DE EXCECUÇÃO. // RESSALVA - SÓCIO(S) COM OCORRÊNCIA(S) DE AÇÕESS JUDICIAIS.',
                                'RATING C // RESSALVA - SÓCIO(S) COM OCORRÊNCIA(S) DE PENDÊNCIA FINANCEIRA (PEFIN).',
                                'RATING A', 'RATING A', 'RATING A', 'RATING B',
                                'RATING A // RESSALVA - SÓCIO(S) COM OCORRÊNCIA(S) DE PENDÊNCIA FINANCEIRA (PEFIN).',
                                'RATING C // RESSALVA - SÓCIO(S) COM OCORRÊNCIA(S) DE AÇÕESS JUDICIAIS.', 'RATING B',
                                'RATING C', 'RATING B', 'RATING A', 'RATING B',
                                'RATING C // RESSALVA - SÓCIO(S) COM OCORRÊNCIA(S) DE PENDÊNCIA FINANCEIRA (PEFIN). // RESSALVA - SÓCIO(S) COM OCORRÊNCIA(S) DE PENDÊNCIA FINANCEIRA (REFIN).',
                                'RATING B', 'RATING A', 'RATING A',
                                'RATING A // RESSALVA - SÓCIO(S) COM OCORRÊNCIA(S) DE PENDÊNCIA FINANCEIRA (PEFIN).',
                                'RATING B // RESSALVA - SÓCIO(S) COM OCORRÊNCIA(S) DE PENDÊNCIA FINANCEIRA (REFIN).',
                                'RATING A',
                                'RATING C // RESSALVA - SÓCIO(S) COM OCORRÊNCIA(S) DE AÇÕESS JUDICIAIS. // RESSALVA - SÓCIO(S) COM OCORRÊNCIA(S) DE PROTESTOS.',
                                'RATING B', 'RATING B', 'RATING B', 'RATING B', 'RATING B',
                                'RATING B // RESSALVA - EMPRESA COM OCORRÊNCIA(S) ACOES JUDICIAIS. // RESSALVA - EMPRESA COM OCORRÊNCIA(S) ACOES DE EXECUÇÃO.',
                                'RATING B',
                                'CREDITO NÃO APROVADO - CLIENTE CONSULTADO CONSTA EM RECUPERAÇÃO JUDICIAL // CREDITO NÃO APROVADO - CLIENTE CONSULTADO CONSTA EM RECUPERAÇÃO JUDICIAL // RATING C // RESSALVA - SÓCIO(S) COM OCORRÊNCIA(S) DE PENDÊNCIA FINANCEIRA (PEFIN).',
                                'RATING A // RESSALVA - SÓCIO(S) COM OCORRÊNCIA(S) DE PENDÊNCIA FINANCEIRA (PEFIN).'],
        'Porte da empresa': ['SMALL', 'SMALL+', 'SMALL', 'SMALL', 'SMALL', '#', 'SMALL', 'SMALL', 'SMALL', 'SMALL',
                             'SMALL', 'SMALL+', 'SMALL', 'SMALL', '#', 'SMALL', 'SMALL', 'MIDDLE', 'SMALL', 'SMALL',
                             '#', 'SMALL', 'MIDDLE', 'SMALL', 'SMALL', 'SMALL', 'SMALL', 'SMALL', 'MIDDLE+', 'SMALL',
                             'SMALL', 'SMALL', 'CORPORATE', 'CORPORATE+', 'CORPORATE', 'SMALL'],
        'Código SAP do Cliente': ['1478064', '10356067', '1528123', '1513563', '1455033', '10158338', '10311263',
                                  '1521543', '10541252', '10541848', '1311183', '1367178', '10648426', '1502901',
                                  '1527333', '1409193', '1059471', '10337221', '10549982', '1001768', '1521635',
                                  '1052119', '10012641', '1046323', '1348362', '10049568', '1527956', '1393423',
                                  '1528025', '1265445', '1378694', '1075474', '1111658', '10367191', '10460667',
                                  '10102671'],
        'Tempo Fundação': ['2,96', '23,43', '24,9', '2,62', '10,13', '19,99', '10,01', '0,99', '7,08', '11,69', '3,05',
                           '16,46', '5,87', '0,68', '4,39', '1,65', '48,56', '14,18', '17,18', '33,93', '2,03', '22,54',
                           '19,09', '26,26', '18,21', '21,25', '1,52', '1,24', '29,65', '14,93', '6,89', '24,91',
                           '20,22', '22,67', '10,51', '15,62'],
        'Limite Anterior': [80000, 0, 300000, 500000, 200000, 150000, 50000, 0, 180000, 500000, 300000, 165000, 450000,
                            250000, 250000, 250000, 200000, 170000, 150000, 0, 800000, 320000, 650000, 160000, 180000,
                            450000, 80000, 180000, 300000, 250000, 185000, 165000, 250000, 1000000, 0, 150000],
        'Contas a Receber': [26340, 3971, 0, 0, 0, 0, 10485, 0, 0, 127218, 138056, 0, 196748, 0, 0, 0, 0, 0, 0, 0, 0,
                             110038, 321236, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 247042, 0, 55608],
        'ano_historico_interno': [[],
                                  [2022, 2022, 2022, 2022, 2022, 2021, 2021, 2021, 2021, 2021, 2017, 2017, 2016, 2015,
                                   2015, 2015], [], [], [],
                                  [2022, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2020, 2020, 2020, 2020, 2020, 2020,
                                   2020, 2020],
                                  [2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2021, 2021, 2021, 2021, 2021, 2021,
                                   2021, 2021], [],
                                  [2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2021, 2021, 2021, 2021, 2021,
                                   2021, 2021],
                                  [2022, 2022, 2022, 2022, 2022, 2022, 2022, 2021, 2021, 2021, 2020, 2019, 2019, 2019,
                                   2018, 2018],
                                  [2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2021, 2021, 2021, 2021, 2021, 2021,
                                   2021, 2020], [2022, 2022, 2022, 2022, 2022, 2022, 2022, 2021],
                                  [2022, 2022, 2021, 2021, 2021], [], [], [], [2021, 2021, 2003], [2022, 2021, 2020],
                                  [2019, 2019, 2019, 2019, 2019, 2018, 2018, 2018, 2018, 2018, 2017, 2017, 2017, 2017,
                                   2017, 2017],
                                  [2022, 2022, 2022, 2022, 2022, 2022, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021,
                                   2021, 2021], [],
                                  [2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2021, 2021, 2021, 2021, 2021, 2021,
                                   2021, 2021],
                                  [2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2021, 2021, 2021, 2021, 2021,
                                   2021, 2021],
                                  [2022, 2022, 2022, 2022, 2022, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021,
                                   2021, 2021],
                                  [2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2021, 2021, 2021, 2021],
                                  [2022, 2022, 2022, 2022, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2020, 2020,
                                   2020, 2020], [], [2022, 2022, 2022], [], [2020, 2020, 2020, 2019], [2021, 2021],
                                  [2021, 2021, 2020, 2020, 2020, 2020, 2020, 2020, 2019, 2019, 2019, 2019, 2019, 2019,
                                   2018, 2018],
                                  [2018, 2018, 2018, 2018, 2018, 2018, 2017, 2017, 2017, 2017, 2017, 2017, 2017, 2017,
                                   2017, 2017],
                                  [2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2021, 2021, 2021, 2021, 2021,
                                   2019, 2019], [],
                                  [2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2021, 2021, 2021, 2021, 2021,
                                   2021, 2021]],
        'valores_historico_interno': [[], [1, 0, 0, 1, 1, 5, 5, 5, 7, 11, 4, 4, 0, 4, 5, 5], [], [], [],
                                      [0, 3, 26, 33, 14, 8, 12, 80, 108, 29, 73, 77, 93, 94, 22, 11],
                                      [1, 3, 6, 8, 11, 22, 7, 35, 110, 60, 26, 11, 11, 3, 3, 3], [],
                                      [13, 6, 12, 3, 11, 15, 5, 6, 11, 11, 35, 17, 7, 11, 6, 8],
                                      [13, 26, 14, 12, 99, 3, 84, 0, 1, 0, 1, 1, 1, 2, 1, 1],
                                      [3, 17, 35, 41, 52, 31, 61, 38, 68, 57, 60, 45, 46, 49, 3, 11],
                                      [1, 6, 24, 30, 23, 35, 33, 0], [40, 82, 5, 33, 8], [], [], [], [51, 55, 10],
                                      [45, 15, 30], [0, 1, 1, 0, 1, 1, 4, 1, 1, 0, 0, 6, 3, 3, 4, 4],
                                      [1, 18, 31, 21, 17, 21, 21, 27, 14, 12, 3, 3, 7, 8, 15, 21], [],
                                      [1, 31, 53, 30, 33, 5, 74, 59, 122, 16, 2, 76, 115, 46, 159, 103],
                                      [93, 36, 101, 62, 33, 55, 47, 67, 54, 91, 13, 54, 54, 107, 181, 112],
                                      [8, 16, 1, 8, 13, 6, 3, 6, 13, 0, 25, 8, 21, 54, 59, 67],
                                      [50, 100, 43, 69, 105, 79, 64, 60, 3, 40, 220, 125],
                                      [5, 12, 184, 9, 15, 2, 41, 32, 6, 6, 7, 15, 7, 10, 163, 87], [], [27, 48, 125],
                                      [], [7, 80, 25, 52], [41, 20], [7, 3, 1, 3, 1, 0, 4, 0, 1, 1, 0, 2, 1, 2, 0, 0],
                                      [1, 1, 0, 19, 0, 0, 0, 1, 1, 1, 2, 1, 0, 0, 0, 2],
                                      [122, 4, 40, 39, 117, 274, 237, 229, 356, 132, 457, 517, 55, 447, 9, 10], [],
                                      [79, 37, 31, 70, 26, 7, 128, 12, 69, 57, 50, 49, 27, 55, 37, 21]],
        'dias_atraso_interno': [[], ['2 ', '3 ', '1 ', '1 ', '1 ', '1 ', '1 ', '0 ', 0, 0, 0, 0, 0, 0, 0, '1 '], [], [],
                                [],
                                ['0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', 0, '0 ', '0 ', '0 ', '0 ', '0 ', '0 ',
                                 '6 '],
                                ['0 ', '0 ', 0, '0 ', '0 ', 0, '0 ', '3 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ',
                                 '0 '], [],
                                ['1 ', '0 ', '1 ', '1 ', '2 ', '3 ', '1 ', 0, '2 ', '1 ', '1 ', '1 ', '1 ', '1 ', '1 ',
                                 '1 '],
                                ['0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ',
                                 '0 ', '0 '], ['0 ', 0, '2 ', 0, 0, '0 ', 0, 0, '10 ', '0 ', 0, 0, 0, 0, '0 ', 0],
                                ['0 ', '1 ', '1 ', '0 ', '0 ', '4 ', '0 ', 0], ['0 ', '0 ', '0 ', '0 ', 0], [], [], [],
                                [0, 0, 0], ['1 ', '0 ', '0 '],
                                ['0 ', '0 ', '0 ', '0 ', '0 ', '0 ', 0, '0 ', '0 ', '0 ', '0 ', 0, '0 ', 0, '0 ', 0],
                                [0, '24 ', '17 ', '18 ', '9 ', '1 ', '0 ', 0, '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ',
                                 0], [],
                                [0, '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', 0, 0, '0 ', 0, '0 ', '0 ', '0 ', '0 ', '0 '],
                                ['0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ',
                                 '0 ', 0],
                                [0, 0, '0 ', '3 ', '6 ', '2 ', '0 ', '0 ', 0, '0 ', 0, '0 ', '5 ', '2 ', '0 ', '0 '],
                                ['28 ', '23 ', '9 ', '7 ', '9 ', '0 ', 0, '1 ', '0 ', 0, '2 ', '1 '],
                                ['7 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', 0,
                                 0], [], [0, 0, 0], [], ['0 ', '0 ', '0 ', '0 '], ['3 ', '0 '],
                                ['0 ', '0 ', '0 ', 0, '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', 0, '0 ', '0 ', '0 ', '0 ',
                                 '0 '],
                                ['0 ', '0 ', '0 ', 0, '0 ', '0 ', '0 ', '0 ', '0 ', 0, '0 ', 0, 0, '0 ', '0 ', 0],
                                ['4 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '4 ', '3 ', 0, '0 ', '0 ', '0 ',
                                 '2 '], [], ['0 ', 0, 0, 0, '0 ', 0, 0, 0, 0, 0, 0, 0, 0, '0 ', 0, 0]],
        'meses_pontuais_internamente': [[], ['2 ', '3 ', '1 ', '1 ', '1 ', '1 ', '1 ', '0 ', 0, 0, 0, 0, 0, 0, 0, '1 '],
                                        [], [], [],
                                        ['0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', 0, '0 ', '0 ', '0 ', '0 ',
                                         '0 ', '0 '],
                                        ['0 ', '0 ', 0, '0 ', '0 ', 0, '0 ', '3 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ',
                                         '0 ', '0 '], [],
                                        ['1 ', '0 ', '1 ', '1 ', '2 ', '3 ', '1 ', 0, '2 ', '1 ', '1 ', '1 ', '1 ',
                                         '1 ', '1 ', '1 '],
                                        ['0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ',
                                         '0 ', '0 ', '0 '],
                                        ['0 ', 0, '2 ', 0, 0, '0 ', 0, 0, '0 ', 0, 0, 0, 0, '0 ', 0],
                                        ['0 ', '1 ', '1 ', '0 ', '0 ', '4 ', '0 ', 0], ['0 ', '0 ', '0 ', '0 ', 0], [],
                                        [], [], [0, 0, 0], ['1 ', '0 ', '0 '],
                                        ['0 ', '0 ', '0 ', '0 ', '0 ', '0 ', 0, '0 ', '0 ', '0 ', '0 ', 0, '0 ', 0,
                                         '0 ', 0], [0, '1 ', '0 ', 0, '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', 0], [],
                                        [0, '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', 0, 0, '0 ', 0, '0 ', '0 ', '0 ', '0 ',
                                         '0 '],
                                        ['0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ',
                                         '0 ', '0 ', 0],
                                        [0, 0, '0 ', '3 ', '2 ', '0 ', '0 ', 0, '0 ', 0, '0 ', '5 ', '2 ', '0 ', '0 '],
                                        ['0 ', 0, '1 ', '0 ', 0, '2 ', '1 '],
                                        ['0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ',
                                         0, 0], [], [0, 0, 0], [], ['0 ', '0 ', '0 ', '0 '], ['3 ', '0 '],
                                        ['0 ', '0 ', '0 ', 0, '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', 0, '0 ', '0 ', '0 ',
                                         '0 ', '0 '],
                                        ['0 ', '0 ', '0 ', 0, '0 ', '0 ', '0 ', '0 ', '0 ', 0, '0 ', 0, 0, '0 ', '0 ',
                                         0], ['4 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '4 ', '3 ', 0, '0 ',
                                              '0 ', '0 ', '2 '], [],
                                        ['0 ', 0, 0, 0, '0 ', 0, 0, 0, 0, 0, 0, 0, 0, '0 ', 0, 0]],
        'historico_interno_12meses': [[], ['2 ', '3 ', '1 ', '1 ', '1 '], [], [], [], ['0 '],
                                      ['0 ', '0 ', 0, '0 ', '0 ', 0, '0 ', '3 ', '0 ', '0 ', '0 '], [],
                                      ['1 ', '0 ', '1 ', '1 ', '2 ', '3 ', '1 ', 0, '2 ', '1 ', '1 ', '1 '],
                                      ['0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 '],
                                      ['0 ', 0, '2 ', 0, 0, '0 ', 0, 0, '10 ', '0 ', 0],
                                      ['0 ', '1 ', '1 ', '0 ', '0 ', '4 ', '0 '], ['0 ', '0 '], [], [], [], [], ['1 '],
                                      [], [0, '24 ', '17 ', '18 ', '9 ', '1 ', '0 ', 0, '0 '], [],
                                      [0, '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', 0, 0, '0 ', 0],
                                      ['0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 '],
                                      [0, 0, '0 ', '3 ', '6 ', '2 ', '0 ', '0 '],
                                      ['28 ', '23 ', '9 ', '7 ', '9 ', '0 ', 0, '1 ', '0 ', 0, '2 '],
                                      ['7 ', '0 ', '0 ', '0 ', '0 '], [], [0, 0, 0], [], [], [], [], [],
                                      ['4 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '4 ', '3 ', 0], [],
                                      ['0 ', 0, 0, 0, '0 ', 0, 0, 0, 0, 0, 0]],
        'valores_interno_12meses': [[], [1, 0, 0, 1, 1], [], [], [], [0], [1, 3, 6, 8, 11, 22, 7, 35, 110, 60, 26], [],
                                    [13, 6, 12, 3, 11, 15, 5, 6, 11, 11, 35, 17], [13, 26, 14, 12, 99, 3, 84],
                                    [3, 17, 35, 41, 52, 31, 61, 38, 68, 57, 60], [1, 6, 24, 30, 23, 35, 33], [40, 82],
                                    [], [], [], [], [45], [], [1, 18, 31, 21, 17, 21, 21, 27, 14], [],
                                    [1, 31, 53, 30, 33, 5, 74, 59, 122, 16, 2],
                                    [93, 36, 101, 62, 33, 55, 47, 67, 54, 91, 13, 54], [8, 16, 1, 8, 13, 6, 3, 6],
                                    [50, 100, 43, 69, 105, 79, 64, 60, 3, 40, 220], [5, 12, 184, 9, 15], [],
                                    [27, 48, 125], [], [], [], [], [],
                                    [122, 4, 40, 39, 117, 274, 237, 229, 356, 132, 457, 517], [],
                                    [79, 37, 31, 70, 26, 7, 128, 12, 69, 57, 50]],
        'meses_pontuais_internamente_12meses': [[], ['2 ', '3 ', '1 ', '1 ', '1 '], [], [], [], ['0 '],
                                                ['0 ', '0 ', 0, '0 ', '0 ', 0, '0 ', '3 ', '0 ', '0 ', '0 '], [],
                                                ['1 ', '0 ', '1 ', '1 ', '2 ', '3 ', '1 ', 0, '2 ', '1 ', '1 ', '1 '],
                                                ['0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 '],
                                                ['0 ', 0, '2 ', 0, 0, '0 ', 0, 0, '0 ', 0],
                                                ['0 ', '1 ', '1 ', '0 ', '0 ', '4 ', '0 '], ['0 ', '0 '], [], [], [],
                                                [], ['1 '], [], [0, '1 ', '0 ', 0, '0 '], [],
                                                [0, '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', 0, 0, '0 ', 0],
                                                ['0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ',
                                                 '0 '], [0, 0, '0 ', '3 ', '2 ', '0 ', '0 '],
                                                ['0 ', 0, '1 ', '0 ', 0, '2 '], ['0 ', '0 ', '0 ', '0 '], [], [0, 0, 0],
                                                [], [], [], [], [],
                                                ['4 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '0 ', '4 ', '3 ', 0],
                                                [], ['0 ', 0, 0, 0, '0 ', 0, 0, 0, 0, 0, 0]]}