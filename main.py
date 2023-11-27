import copy
import itertools

def conta_penalidade(tempo, prazo, penalidade, hoje):
    """Faz a conta da penalidade em relação ao dia atual"""
    # dia atual + tempo = dia termino| dia termino - prazo = dias de penalidade| dias de penalidade * penalidade = penalidade atual
    if penalidade >= 0:
        dia_termino = (hoje + tempo) - 1 # -1 porque o dia atual conta. EX: (dia 4 + 4 de prazo = 8, porém começa no dia 4, então vai terminar no dia 7)
        conta = max(0, dia_termino - prazo) * penalidade 

        return(conta)
    
    return(-100)

def Greedy(trabalhos):

    ordem = [0] * len(trabalhos) # Instancia a ordem 
    trabalhos_copia = copy.deepcopy(trabalhos) # copia a lista trabalhos para poder ser alterada no lugar da original 
    ordem[0] = 1 # o primeiro trabalho que tem que ser executado é o primeiro da lista
    dia_atual = 1 # instancia o dia
    dia_atual += trabalhos[0][0] # soma o dia atual com o tempo que leva pro primeiro trabalho ficar pronto e podermos começar o próximo
    penalidades = (max(0, trabalhos[0][0] - trabalhos[0][1]) * trabalhos[0][2]) # instancia as penalidades com a penalidade de atraso do primeiro trabalho  

    for i in range(1, len(trabalhos)):
        k = i # salva o trabalho que vai ser adicionado na ordem
        prioridade = conta_penalidade(trabalhos_copia[i][0], trabalhos_copia[i][1], trabalhos_copia[i][2], dia_atual) # salva qual a maior penalidade que vai ser aplicada para o trabalho que vai ser adicionado a ordem

        for j in range(len(trabalhos)- 1, 0, -1): # Percorre todos os trabalhos para fazer comparações
            penalidade_para_trabalho = conta_penalidade(trabalhos_copia[j][0], trabalhos_copia[j][1], trabalhos_copia[j][2], dia_atual) # salva a penalidade do trabalho analisado      
            
            if penalidade_para_trabalho > prioridade: # Se a penalidade do trabalho analisado for maior que a penalidade do trabalho que vai ser adicionado a ordem, realiza trocas
                prioridade = penalidade_para_trabalho
                k = j
        
        ordem[i] = k + 1 # Adiciona o trabalho na ordem
        trabalhos_copia[k][2] = -100 # Altera o valor da penalidade para negativo para termos controle de que esse trabalho já está na lista
        dia_atual += trabalhos_copia[k][0] # Acrescenta os dias para realização do trabalho ao dia atual
        penalidades += prioridade # Acrescenta a penalidade do atraso
            
    print(f"ordem de execução: {ordem}")
    print(f"Penalidade máxima: {penalidades}")


def calcula_penalidade(sequencia, jobs):
    tempo_total = 0  # Inicializa o tempo total como 0
    penalidade_total = 0  # Inicializa a penalidade total como 0

    for indice in sequencia:
        # Adiciona o tempo do job ao tempo total
        tempo_total += jobs[indice][0]
        # Calcula a penalidade acumulada para o job atual e adiciona à penalidade total
        penalidade_total += max(0, tempo_total - jobs[indice][1]) * jobs[indice][2]

    return penalidade_total  # Retorna a penalidade total para a sequência dada

def branch_and_bound(jobs):
    n = len(jobs)  # Obtém o número de jobs
    melhor_sequencia = None  # Inicializa a melhor sequência como None
    melhor_penalidade = float('inf')  # Inicializa a melhor penalidade como infinito positivo

    for sequencia in itertools.permutations(range(n)):
        # Para cada permutação possível dos índices dos jobs
        penalidade_atual = calcula_penalidade(sequencia, jobs)
        # Calcula a penalidade para a sequência atual usando a função definida acima

        if penalidade_atual < melhor_penalidade:
            # Se a penalidade atual for menor que a melhor penalidade conhecida
            melhor_sequencia = sequencia
            # Atualiza a melhor sequência
            melhor_penalidade = penalidade_atual
            # Atualiza a melhor penalidade conhecida

    return melhor_sequencia, melhor_penalidade

trabalhos = [[1, 2, 5], [2, 5, 2], [3, 1, 8], [4, 3, 4]]
# (tempo que gasta, prazo, penalidade)

Greedy(trabalhos)
melhor_sequencia, melhor_penalidade = branch_and_bound(trabalhos)
melhor_sequencia_incrementada = tuple(i + 1 for i in melhor_sequencia)

print("Melhor sequência:", melhor_sequencia_incrementada)
print("Melhor penalidade:", melhor_penalidade)
    