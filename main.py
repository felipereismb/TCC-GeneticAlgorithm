from algoritmoGenetico import AlgoritmoGenetico
from cromossomo import Cromossomo

class Main():
    tamanho_populacao_inicial = 10
    
    AG = AlgoritmoGenetico(tamanho_populacao_inicial) 
    AG.imprimirPopulacao()

    for i in range(50):
        AG.operacao()
    
    AG.imprimirPopulacao()
