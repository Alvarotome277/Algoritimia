"""
Práctica 2: Algoritmos codiciosos.
Algoritmia y Estructuras de Datos Avanzadas.
Curso 2026-27.
"""

from typing import List, Tuple, Dict, Optional
import random

# =============================================================================
# I. Problema del cambio de monedas
# =============================================================================

def greedy_change(coins: List[int], amount: int) -> Tuple[List[int], int]:
    coins.sort(reverse=True)
    used_coins = []
    for coin in coins:
        while (amount>=coin):  
            used_coins.append(coin)
            amount = amount - coin
    
    return used_coins, amount
    
def optimal_change(coins: List[int], amount: int) -> Optional[List[int]]:
    infinite = float('inf')
    filas = len(coins) + 1
    columnas = amount + 1
    matriz = [[infinite for _ in range(columnas)] for _ in range(filas)]
    for a in range(1, columnas):
        matriz[0][a] = float('inf')
        for i in range (1,filas):
           coin = coins[i-1]
           if a < coin:
                matriz[i][a] = matriz[i-1][a]
           else:
                matriz[i][a] = min(matriz[i-1][a], 1 + matriz[i] [a-coin])
    if matriz[-1][-1] == float('inf'):
            return None
            
    resultado = []
    i = len(coins)
    a = amount
    
    while a > 0:
        
        if matriz[i][a] == matriz[i-1][a]:
            i -= 1
        
        else:
            resultado.append(coins[i-1])
            a -= coins[i-1] 
            
    return resultado
    
    

def compare_change(coins: List[int], max_amount: int) -> Dict[str, List[int]]:
    """
    Evalúa todas las cantidades entre 1 y max_amount, clasifica cada cantidad en
    'optimal', 'suboptimal', 'greedy_failed' o 'impossible'.
    """
    clasificacion = {
        "optimal": [],
        "suboptimal": [],
        "greedy_failed": [],
        "impossible": []
    }

    coins_copy = coins.copy()
    
    for amount in range(1, max_amount + 1):

        greedy_coins, greedy_remainder = greedy_change(coins_copy, amount)
        opt_coins = optimal_change(coins, amount)


        if opt_coins is None:
            clasificacion["impossible"].append(amount)
        elif greedy_remainder != 0:
            clasificacion["greedy_failed"].append(amount)
        elif len(greedy_coins) == len(opt_coins):
            clasificacion["optimal"].append(amount)
        else:
            clasificacion["suboptimal"].append(amount)
            
    return clasificacion
    pass

# =============================================================================
# II. Selección de actividades
# =============================================================================

def activity_selection(activities: List[Tuple[str, int, int]]) -> List[Tuple[str, int, int]]:
    conj_dia = []
    o_activities = []
    registro = 0

    o_activities= sorted(activities,key= lambda t: t[2] ,reverse= False)
        
    for n in o_activities:
        if registro <= n[1]:
            conj_dia.append(n)
            registro= n[2]

    return conj_dia



def generate_activities(n: int, seed: int = 42) -> List[Tuple[str, int, int]]:
    random.seed(seed)
    activities = []
    
    for i in range(n):
        identificador = f"A{i}"
        start = random.randint(0, 10000)
        duration = random.randint(1, 100)
        end = start + duration
        activities.append((identificador, start, end))
        
    return activities

# =============================================================================
# III. Planificación de tareas con fechas límite
# =============================================================================

def job_scheduling(jobs: List[Tuple[str, int, int]]) -> Tuple[List[Optional[Tuple[str, int, int]]], int]:

    
    ordered_jobs = sorted(jobs, key=lambda t: (-t[2], t[1], t[0]))

    max_deadline = max(t[1] for t in jobs)
    schedule = [None] * max_deadline
    count = 0

    for n in ordered_jobs:
        '''empieza, fin, paso'''
        for i in range(n[1] - 1, -1, -1):
            if schedule[i] is None:
                schedule[i] = n
                count += n[2]
                break   

    return schedule, count




def generate_jobs(n: int, seed: int = 42) -> List[Tuple[str, int, int]]:
    random.seed(seed)
    max_deadline = max(1, n // 10)
    jobs = []

    for i in range(n):
        profit = random.randint(1, 1000)
        deadline = random.randint(1, max_deadline)
        jobs.append((f"J{i}", profit, deadline))
        
    return jobs