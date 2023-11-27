import copy

def conta_penalidade(tempo, prazo, penalidade, hoje):
    """Faz a conta da penalidade em relação ao dia atual"""
    # dia atual + tempo = dia termino| dia termino - prazo = dias de penalidade| dias de penalidade * penalidade = penalidade atual
    if penalidade >= 0:
        dia_termino = (hoje + tempo) - 1 # -1 porque o dia atual conta. EX: (dia 4 + 4 de prazo = 8, porém começa no dia 4, então vai terminar no dia 7)
        conta = max(0, dia_termino - prazo) * penalidade 

        return conta
    
    return(-100)

def Greedy(trabalhos):

    ordem = [0] * len(trabalhos) # Instancia a ordem 
    trabalhos_copia = copy.deepcopy(trabalhos) # copia a lista trabalhos para poder ser alterada no lugar da original 
    # ordem[0] = 1 # o primeiro trabalho que tem que ser executado é o primeiro da lista
    dia_atual = 1 # instancia o dia
    # dia_atual += trabalhos[0][0] # soma o dia atual com o tempo que leva pro primeiro trabalho ficar pronto e podermos começar o próximo
    # penalidades = (max(0, trabalhos[0][0] - trabalhos[0][1]) * trabalhos[0][2]) # instancia as penalidades com a penalidade de atraso do primeiro trabalho  
    penalidades = 0 # instancia as penalidades 

    for i in range(0, len(trabalhos)):
        k = i # salva o trabalho que vai ser adicionado na ordem
        prioridade = conta_penalidade(trabalhos_copia[i][0], trabalhos_copia[i][1], trabalhos_copia[i][2], dia_atual) # salva qual a maior penalidade que vai ser aplicada para o trabalho que vai ser adicionado a ordem

        for j in range(len(trabalhos)- 1, -1, -1): # Percorre todos os trabalhos para fazer comparações
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
    
def atrasado(tempo, prazo, hoje, fazivel):
    if fazivel == 'Feito':
        return 'Feito'
    else:
        if (tempo + hoje) - 1 > prazo:
            return False
        else:
            return True

def Greedy2(trabalhos):
    ordem = [0] * len(trabalhos)
    fazivel = [True] * len(trabalhos)
    penalidades = 0
    dia_atual = 1

    for i in range(0, len(trabalhos)):        
        k = i
        prioridade = 0
        fazivel[i] = atrasado(trabalhos[i][0], trabalhos[i][1], dia_atual, fazivel[i])
        if fazivel[i] == False:
            penalidades += trabalhos[i][2]
        else:
            if fazivel[i] != "Feito": prioridade = trabalhos[i][2]

            for j in range(len(trabalhos)- 1, -1, -1):
                fazivel[j] = atrasado(trabalhos[j][0], trabalhos[j][1], dia_atual, fazivel[j])
                if fazivel[j] == True and trabalhos[j][2] > prioridade:
                    prioridade = trabalhos[j][2]
                    k = j
            if fazivel[k] != "Feito":
                ordem[i] = k + 1
                dia_atual += trabalhos[k][0]
                fazivel[k] = "Feito"
    
    print(f"ordem de execução: {ordem}")
    print(f"Penalidade máxima: {penalidades}")
    print(f"Execução de trabalhos: {fazivel}")


# trabalhos = [[1, 2, 5], [2, 5, 2], [3, 1, 8], [4, 3, 4]]
trabalhos = [[1, 2, 5], [8, 1, 2], [3, 5, 8], [3, 9, 4], [1, 99, 499], [18, 100, 500], [2, 8, 1], [5, 7, 10000], [3, 14, 41], [15, 84, 37]]
# (tempo que gasta, prazo, penalidade)

Greedy(trabalhos)

# Greedy2(trabalhos)
