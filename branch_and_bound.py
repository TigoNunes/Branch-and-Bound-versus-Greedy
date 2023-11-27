import sys
import time

from collections import namedtuple

# Define a estrutura de dados para as tarefas
Task = namedtuple('Task', ['id', 'time', 'deadline', 'penalty'])

def branch_and_bound(tasks):
    # Ordena as tarefas por penalidade em ordem decrescente
    tasks.sort(key=lambda x: x.penalty, reverse=True)

    # Inicializa a melhor sequência e a penalidade mínima
    best_seq = []
    min_penalty = sys.maxsize

    # Função recursiva para encontrar a melhor sequência
    def sequence_tasks(seq, penalty, time):
        nonlocal best_seq, min_penalty

        # Se todas as tarefas foram sequenciadas
        if len(seq) == len(tasks):
            # Atualiza a melhor sequência e a penalidade mínima
            if penalty < min_penalty:
                best_seq = seq[:]
                min_penalty = penalty
            return

        for i in range(len(tasks)):
            if i not in seq:
                # Calcula a penalidade para a tarefa atual
                curr_penalty = max(0, time + tasks[i].time - tasks[i].deadline) * tasks[i].penalty

                # Continua apenas se a penalidade atual for menor que a penalidade mínima
                if penalty + curr_penalty < min_penalty:
                    seq.append(i)
                    sequence_tasks(seq, penalty + curr_penalty, time + tasks[i].time)
                    seq.pop()

    # Inicia o algoritmo
    sequence_tasks([], 0, 0)

    # Retorna a melhor sequência e a penalidade mínima
    return [tasks[i] for i in best_seq], min_penalty

# Exemplo de uso
tasks = [Task(1, 1, 2, 5), Task(2, 8, 1, 2), Task(3, 3, 5, 8), Task(4, 3, 9, 4), Task(5, 1, 99, 499), Task(6, 18, 100, 500), Task(7, 2, 8, 1), Task(8, 5, 7, 10000), Task(9, 3, 14, 41), Task(10, 15, 84, 37)]

tempo_inicial = time.time()
best_seq, min_penalty = branch_and_bound(tasks)
tempo_final = time.time()

best_seq_id = tuple(best_seq[i][0] for i in range(len(best_seq)))

print(f'Sequência de Execução: {best_seq_id}')
print(f'Penalidade total: {min_penalty}')
print(f"{tempo_final - tempo_inicial} segundos")
