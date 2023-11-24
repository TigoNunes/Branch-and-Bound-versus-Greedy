import copy

def conta_penalidade(tempo, prazo, penalidade):
    """Faz a conta da penalidade em relação ao dia atual"""
    conta = (prazo - tempo) * penalidade
    if conta < 0:
        conta *= -1
    return(conta)

def Greedy(trabalhos):
    # TODO: Temos que fazer a relação entre o tempo de execução e a penalidade em relação ao dia atual

    ordem = [0] * len(trabalhos)
    trabalhos_copia = copy.deepcopy(trabalhos)
    ordem[0] = 1
    dia_atual = 1
    dia_atual += trabalhos[0][0]
    penalidades += (max(0, trabalhos[0][0] - trabalhos[0][1]) * trabalhos[0][2]) 


    for i in range(1, len(trabalhos)):
        for j in range(i, len(trabalhos)):
            # determinar a relação entre o tempo de execução e a penalidade em relação ao dia atual de cada trabalho e comparar qual o maior
            # implementar o dia, salvar a ordem
            # verificar a ordem.
            pass 
    
    
    # for i in range(1, len(trabalhos)):
    #     k = i
    #     prioridade = trabalhos_copia[i][2]

    #     for j in range(len(trabalhos)- 1, 0, -1):
    #         if trabalhos_copia[j][2] > prioridade:
    #             prioridade = trabalhos_copia[j][2]
    #             k = j
        
    #     ordem[i] = k + 1
    #     trabalhos_copia[k][2] = -100      
    

trabalhos = [[1, 2, 5], [2, 5, 2], [3, 1, 8], [4, 3, 4]]
# (tempo que gasta, prazo, penalidade)

Greedy(trabalhos)

