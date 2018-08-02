from cromossomo import Cromossomo
import random

class AlgoritmoGenetico():
    cromossomos = []

    def __init__(self, tamanho_população_inicial):
        self.inicializarPopulacao(tamanho_população_inicial)
        self.ordenarPopulacao()

    def imprimirPopulacao(self):
        print("\n\n")
        for i in range(0, len(self.cromossomos)):
            print('Individuo: {} - Size: {} - Acuracia: {}'.format(
                self.cromossomos[i].individuo, self.cromossomos[i].size, self.cromossomos[i].acuracia))

    def inicializarPopulacao(self, tamanho):
        individuoDefault = '0000000000000000000000000000'

        self.cromossomos.append(Cromossomo(individuoDefault))
        for i in range(0, (tamanho - 1)):
            novo = self.gerarUmIndividuo()
            self.cromossomos.append(novo)

    def gerarUmIndividuo(self):
        novo = ''

        criterion = random.randint(0, 1)
        splitter = random.randint(0, 1)

        novo += str(criterion)+str(splitter)

        max_depth_bit1 = random.randint(0, 1)
        max_depth_bit2 = random.randint(0, 1)
        max_depth_bit3 = random.randint(0, 1)
        max_depth_bit4 = random.randint(0, 1)
        max_depth_bit5 = random.randint(0, 1)
        max_depth_bit6 = random.randint(0, 1)

        novo += str(max_depth_bit1) + str(max_depth_bit2) + str(max_depth_bit3) + \
            str(max_depth_bit4) + str(max_depth_bit5) + str(max_depth_bit6)

        min_samples_split_bit1 = random.randint(0, 1)
        min_samples_split_bit2 = random.randint(0, 1)
        min_samples_split_bit3 = random.randint(0, 1)
        min_samples_split_bit4 = random.randint(0, 1)
        min_samples_split_bit5 = random.randint(0, 1)
        min_samples_split_bit6 = random.randint(0, 1)
        min_samples_split_bit7 = random.randint(0, 1)
        min_samples_split_bit8 = random.randint(0, 1)

        novo += str(min_samples_split_bit1) + str(min_samples_split_bit2) + str(min_samples_split_bit3) + str(min_samples_split_bit4) + str(min_samples_split_bit5) + \
            str(min_samples_split_bit6) + str(min_samples_split_bit7) + str(min_samples_split_bit8) 

        min_samples_leaf_bit1 = random.randint(0, 1)
        min_samples_leaf_bit2 = random.randint(0, 1)
        min_samples_leaf_bit3 = random.randint(0, 1)
        min_samples_leaf_bit4 = random.randint(0, 1)
        min_samples_leaf_bit5 = random.randint(0, 1)
        min_samples_leaf_bit6 = random.randint(0, 1)
        min_samples_leaf_bit7 = random.randint(0, 1)
        min_samples_leaf_bit8 = random.randint(0, 1)

        novo += str(min_samples_leaf_bit1) + str(min_samples_leaf_bit2) + str(min_samples_leaf_bit3) + str(min_samples_leaf_bit4) + str(min_samples_leaf_bit5) + \
            str(min_samples_leaf_bit6) + str(min_samples_leaf_bit7) + str(min_samples_leaf_bit8) 

        min_weight_fraction_leaf_bit1 = random.randint(0, 1)
        min_weight_fraction_leaf_bit2 = random.randint(0, 1)
        min_weight_fraction_leaf_bit3 = random.randint(0, 1)

        novo += str(min_weight_fraction_leaf_bit1) + \
            str(min_weight_fraction_leaf_bit2) + \
            str(min_weight_fraction_leaf_bit3)

        presort = random.randint(0, 1)

        novo += str(presort)
        
        return Cromossomo(novo)

    def ordenarPopulacao(self):
        # Ordena a lista pelo fitness (key = lambda cromossomo: cromossomo.fitness)
        listaOrdenada = sorted(self.cromossomos, key=lambda cromossomo: cromossomo.fitness, reverse=True)
        self.cromossomos = listaOrdenada

    def selecaoPaisRandom(self):
        rand1 = random.randint(0, len(self.cromossomos) - 1)
        rand2 = random.randint(0, len(self.cromossomos) - 1)

        print(rand1)
        print(rand2)

        pai1 = self.cromossomos[rand1]
        pai2 = self.cromossomos[rand2]

        return pai1, pai2

    def selecaoPaisElitismo(self):
        pai1 = self.cromossomos[0]
        pai2 = self.cromossomos[1]

        return pai1, pai2

    def cruzamento(self, pai1, pai2):
        individuoFilho1 = ''
        individuoFilho2 = ''

        # Faz o crossover, pegando, alternadamente o bit do pai1 e do pai2
        for i in range(28):
            if((i % 2) == 0):
                individuoFilho1 += pai1.individuo[i]
                individuoFilho2 += pai2.individuo[i]
            else:
                individuoFilho1 += pai2.individuo[i]
                individuoFilho2 += pai1.individuo[i]
    
        return individuoFilho1, individuoFilho2

    def cruzamentoComPontoDeCorte(self, pai1, pai2):
        cromossomoFilho1 = []
        individuoFilho1 = ''

        cromossomoFilho2 = []
        individuoFilho2 = ''

        # 0 0 000000 0000000010 0000000001 101 0
        # Faz o crossover, pegando, alternadamente o bit do pai1 e do pai2
        individuoFilho1 += pai1.individuo[0] + pai2.individuo[1] + pai1.individuo[2:8] +pai2.individuo[8:16]+ pai1.individuo[16:24] + pai2.individuo[24:27] +pai1.individuo[27]
        individuoFilho2 += pai2.individuo[0] + pai1.individuo[1] + pai2.individuo[2:8] +pai1.individuo[8:16]+ pai2.individuo[16:24] + pai1.individuo[24:27] +pai2.individuo[27]

        cromossomoFilho1.append(pai1.cromossomo[0])
        cromossomoFilho1.append(pai2.cromossomo[1])

        cromossomoFilho2.append(pai2.cromossomo[0])
        cromossomoFilho2.append(pai1.cromossomo[1])

        for i in range(2,8):
            cromossomoFilho1.append(pai1.cromossomo[i])
            cromossomoFilho2.append(pai2.cromossomo[i])

        for i in range(8,16):
            cromossomoFilho1.append(pai2.cromossomo[i])
            cromossomoFilho2.append(pai1.cromossomo[i])

        for i in range(16,24):
            cromossomoFilho1.append(pai1.cromossomo[i])
            cromossomoFilho2.append(pai2.cromossomo[i])

        for i in range(24,27):
            cromossomoFilho1.append(pai2.cromossomo[i])
            cromossomoFilho2.append(pai1.cromossomo[i])

        cromossomoFilho1.append(pai1.cromossomo[27])
        cromossomoFilho2.append(pai2.cromossomo[27])

        # Retorna a lista de probabilidade de cada bit do cromossomo
        return cromossomoFilho1, cromossomoFilho2

    def verificaSeContemNaPopulacao(self, cromossomo):
        for i in range(len(self.cromossomos)):
            if(self.cromossomos[i].individuo == cromossomo):
                novo = self.gerarUmIndividuo()
                return self.verificaSeContemNaPopulacao(novo.individuo)
        return cromossomo
    
    def mutacao(self, cromossomo):
        rand = random.randint(0, 27)

        individuo = cromossomo
        m = int(individuo[rand])

        if (m == 0):
            list1 = list(individuo)
            list1[rand] = '1'
            str1 = ''.join(list1)
            individuo = str1
        else:
            list1 = list(individuo)
            list1[rand] = '0'
            str1 = ''.join(list1)
            individuo = str1

        m = int(individuo[rand])

        if (m == 0):
            list1 = list(individuo)
            list1[rand] = '1'
            str1 = ''.join(list1)
            individuo = str1
        else:
            list1 = list(individuo)
            list1[rand] = '0'
            str1 = ''.join(list1)
            individuo = str1

        return Cromossomo(individuo)

    def operacao(self):
        # print("Entrou aqui")
        pai1, pai2 = self.selecaoPaisElitismo()
        cromossomoResultante1, cromossomoResultante2 = self.cruzamento(pai1, pai2)
        
        cromossomoResultante1 = self.verificaSeContemNaPopulacao(cromossomoResultante1)
        cromossomoResultante2 = self.verificaSeContemNaPopulacao(cromossomoResultante2)

        cromossomoResultante1 = self.mutacao(cromossomoResultante1)
        cromossomoResultante2 = self.mutacao(cromossomoResultante2)

        self.cromossomos.append(cromossomoResultante1)
        self.cromossomos.append(cromossomoResultante2)

        self.ordenarPopulacao()
        self.cromossomos = self.cromossomos[:-2]