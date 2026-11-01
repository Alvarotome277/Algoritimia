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
    """
    Estrategia codiciosa para el problema del cambio de monedas.
    Selecciona en cada paso la moneda de mayor valor que no supere la cantidad restante.
    """
    pass

def optimal_change(coins: List[int], amount: int) -> Optional[List[int]]:
    """
    Solución óptima mediante programación dinámica para el problema del cambio de monedas.
    Determina el menor número de monedas necesario para obtener la cantidad objetivo.
    """
    pass

def compare_change(coins: List[int], max_amount: int) -> Dict[str, List[int]]:
    """
    Evalúa todas las cantidades entre 1 y max_amount, clasifica cada cantidad en
    'optimal', 'suboptimal', 'greedy_failed' o 'impossible'.
    """
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
    """
    Genera n actividades aleatorias reproducibles.
    start en [0, 10000], duration en [1, 100], end = start + duration.
    """
    pass

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