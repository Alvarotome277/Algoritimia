import time
import matplotlib.pyplot as plt
from p2 import compare_change, greedy_change, optimal_change

def analizar_monedas():
    sistemas = {
        "Euro_simplificado": [200, 100, 50, 20, 10, 5, 2, 1],
        "Sistema_2": [10, 5, 2, 1],
        "Sistema_3": [25, 10, 4, 1],
        "Sistema_4": [4, 3, 1]
    }
    
    max_amount = 500
    
    print("--- RESULTADOS TABLA CAMBIO DE MONEDAS (1 a 500) ---")
    for nombre, coins in sistemas.items():
        res = compare_change(coins, max_amount)
        print(f"\nSistema: {coins}")
        for categoria, cantidades in res.items():
            num = len(cantidades)
            porcentaje = (num / max_amount) * 100
            print(f"  {categoria}: {num} ({porcentaje:.1f}%)")
            
    print("\nGenerando gráfica de tiempos...")
    
    # Medir tiempos (usando el sistema [4, 3, 1] como ejemplo)
    coins_test = [4, 3, 1]
    cantidades = list(range(10, 501, 10)) # De 10 a 500 de 10 en 10
    
    tiempos_greedy = []
    tiempos_opt = []
    
    for amount in cantidades:
        # Tiempo Codicioso (media de 10 ejecuciones)
        t_ini = time.perf_counter()
        for _ in range(10):
            greedy_change(coins_test.copy(), amount)
        t_fin = time.perf_counter()
        tiempos_greedy.append((t_fin - t_ini) / 10)
        
        # Tiempo Óptimo (media de 10 ejecuciones)
        t_ini = time.perf_counter()
        for _ in range(10):
            optimal_change(coins_test, amount)
        t_fin = time.perf_counter()
        tiempos_opt.append((t_fin - t_ini) / 10)

    # Crear gráfica
    plt.figure(figsize=(10, 6))
    plt.plot(cantidades, tiempos_greedy, marker='o', label='Greedy (Codicioso)', color='blue')
    plt.plot(cantidades, tiempos_opt, marker='x', label='Óptimo (DP)', color='red')
    
    plt.title('Comparativa de Tiempos: Cambio de Monedas')
    plt.xlabel('Cantidad Objetivo (amount)')
    plt.ylabel('Tiempo Medio (s)')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('grafica_monedas.png')
    plt.close()
    
    print("Gráfica 'grafica_monedas.png' guardada.")

if __name__ == "__main__":
    analizar_monedas()