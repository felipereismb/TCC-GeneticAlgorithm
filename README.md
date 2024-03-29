# Implementação realizada para Trabalho de Conclusão de Curso em Ciência da Computação - [UFT](https://ww2.uft.edu.br//)

## Resumo
Alguns algoritmos em aprendizado de máquina são parametrizáveis, ou seja, permitem a configuração de parâmetros de maneira a aumentar o desempenho na tarefa utilizada. Na maioria dos casos, estes parâmetros são encontrados empiricamente pelo desenvolvedor. Outra abordagem é utilizar alguma técnica de otimização para encontrar um conjunto otimizado de parâmetros. Este projeto tem por objetivo a aplicação dos algoritmos evolutivos, Algoritmo Genético (AG), Fluid Genetic Algorithm (FGA) e Genetic Algorithm using Theory of Chaos (GATC) para otimizar a busca de hiperparâmetros em algoritmos de árvores de decisão. Este trabalho apresenta alguns resultados  satisfatórios dentro do conjunto de dados testados, onde o algoritmo Classification and Regression Trees (CART) foi utilizado como algoritmo classificador para os testes. Nestes, as árvores de decisão geradas a partir dos valores padrão dos hiperparâmetros são comparados com os otimizados pela abordagem proposta. Buscou-se otimizar a acurácia e o tamanho final da árvore gerada, o que foram otimizadas com sucesso pelos algoritmos propostos.

## Problema
O problema de configuração automática de hiperparâmetros tem relação com vários campos que excedem a computação, onde todas essas áreas compartilham de um critério de qualidade específico comparando diferentes objetos, tendo como objetivo selecionar o objeto que melhor representa o conjunto de dados. Assim, modelos estatísticos e metodologia de otimização são implementados em ML com foco de selecionar os valores dos hiperparâmetros.   

Uma grande gama dos problemas necessitam de uma configuração dos parâmetros para obtenção de um resultado mais satisfatório, com isso, é consumido muito tempo e em alguns casos é necessário que um especialista estude a base de dados e o algoritmo utilizado, para assim, realizar a melhor configuração possível dos parâmetros do algoritmo.

## Algoritmo Classification and Regression Trees (CART)
O algoritmo CART é uma árvore de decisão, e tem como entrada um objeto ou um conjunto de atributos e como saída uma resposta, essa é dada a partir de uma sequência de testes.

Basicamente uma Árvore de Decisão permite dividir recursivamente um conjunto de dados de treino até que cada divisão forneça uma classificação para a instância.
As Árvores de Decisão consistem em "nós" que formam uma árvore, o que significa que, existe um nó-raiz que não tem ramos de entrada, ao contrário dos restantes nós. Cada nó intermédio específica um teste para o atributo, e cada ramo descendente desse nó corresponde ao valor possível desse atributo. Este conjunto de regras é seguido até ser atingido o nó-terminal ou folha

![image](https://user-images.githubusercontent.com/17303936/156013600-da25f627-c08a-4649-9bb1-d4fdfcf86715.png)

A árvore de decisão resultante a partir do a algoritmo CART sempre é binária, o critério utilizado para calcular a impureza de um nó é o índice Gini, o qual mede a heterogeneidade dos dados.

Optou-se por manipular os seguintes parâmetros do algoritmo CART:

![image](https://user-images.githubusercontent.com/17303936/156027741-ab12e3b9-1849-43be-8ba7-f0217e082649.png)

## Base de dados
### Steel Plates
Esta base de dados contém dados de falhas na produção de placas de aço, sendo 1941 exemplos descritos por 27 atributos e classificados em 7 classes. Esses atributos descrevem as propriedades físicas das placas de aço, como tamanho do defeito, posição da falha, refletância da luz da superfície, tipo de material, etc. Todos os atributos são numéricos.

### Breast Cancer
Nesta base de dados relata-se sobre a ocorrência ou não do câncer de mama, estão incluídos 201 instâncias de uma classe e 85 instâncias de outra classe. As instâncias são descritas por 9 atributos, alguns dos quais são lineares e alguns são nominais.

### Wine
Está base de dados mostram os resultados de uma análise química de vinhos mas derivados de três diferentes cultivares. A análise determinou as quantidades de 13 constituintes encontrados em cada um dos três tipos de vinhos. Foram registadas 178 instancias.

### Iris
Este é talvez o banco de dados mais conhecido encontrado na literatura sobre reconhecimento de padrões. O conjunto de dados contém 3 classes de 50 instâncias cada, onde cada classe se refere a um tipo de planta da íris. 

### Isolet
Este conjunto de dados foi gerado da seguinte forma. 150 voluntários falaram o nome de cada letra do alfabeto duas vezes

### Madelon
Este conjunto de dados contém pontos de dados agrupados em 32 agrupamentos colocados nos vértices de um hipercubo de cinco dimensões e rotulados aleatoriamente com +1 ou -1. As cinco dimensões constituem 5 características informativas, assim, 15 combinações lineares desses recursos foram adicionadas para formar um conjunto de 20 recursos informativos.


## Algoritmos Genéticos
Os Algoritmos Genéticos são uma técnica de busca, tendo o seu foco analisar as possíveis soluções e encontrar um resultado perto da solução ótima quase sempre sem necessitar da interferência humana. A estrutura básica de um algoritmo genético normalmente é composta por populações de cromossomos, seleção de acordo com a aptidão, cruzamento para produzir novos filhos, e mutação aleatória destes novos filhos.

![image](https://user-images.githubusercontent.com/17303936/156026228-1dfb20f1-dced-4ec1-abc4-667626766319.png)

Para compreender o funcionamento dos AG's faz-se necessário realizar uma analogia à evolução das espécies. Assim, o AG trabalha da seguinte forma:

- Inicialmente é gerado a população inicial, que consiste em uma quantidade n de cromossomos, os quais são possíveis soluções para o problema;
- Durante o processo evolutivo, cada indivíduo na população recebe uma nota referente ao valor obtido na função de avaliação;
- Uma porcentagem dos indivíduos são mais adaptados, fazendo com que os mais fracos sejam descartados;
- Os membros mantidos pela seleção podem sofrer modificações em suas características fundamentais por meio de cruzamentos crossover, mutações ou recombinação genética gerando descendentes para a próxima geração;
- Este processo, chamado geração, é repetido até que uma solução satisfatória seja encontrada ou o critério de parada seja alcançado.





