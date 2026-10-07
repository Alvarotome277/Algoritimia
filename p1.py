import time # Para la función time_measure. Entender código dado.
import matplotlib.pyplot as plt # Para imprimir gráficas. Entender código dado.
import random # Puede usarse random.randint(n, m) para generar listas aleatorias de enteros en las funciones dataprep.
import numpy as np

# I.A.1 Medición de tiempos de ejecución
def time_measure(f, dataprep, Nlist, Nrep=1000, Nstat=100):
    """Mide la media y varianza del tiempo de ejecución de la función f
    para cada tamaño n presente en Nlist.
    """
    res = []
    for n in Nlist:
        partial = []
        for _ in range(Nstat):
            data = dataprep(n)
            t1 = time.perf_counter()
            for _ in range(Nrep):
                f(data)
            t2 = time.perf_counter()
            t_elem = (t2 - t1) / float(Nrep)
            partial.append(t_elem)

        mean_val = sum(partial) / float(Nstat)
        var_val = sum((x - mean_val) ** 2 for x in partial) / float(Nstat)
        res.append((mean_val, var_val))
    return res

def dataprep_sum_pair_hit(n):
    """Genera un caso donde SÍ existe un par que suma target.
    Devuelve una tupla (lista, target)
    """
    random1 =random.randint(0,n-1)
    random2 =random.randint (0,n-1)
    while random1 == random2:
       random2 = random.randint(0, n - 1)
    lista = [random.randint(0, n-1) for i in range(n)]
    target = random.randint(0,n)
    lista [random1] = target - lista [random2]
    return (lista, target)
            
        

   

def dataprep_sum_pair_miss(n):
    """Genera un caso donde NO existe ningún par (Caso peor).
    Devuelve una tupla (lista, target)
    """
    target = random.randint(0,n)
    lista = [target + 1 + random.randint(0, n-1) for i in range(n)]
    return (lista, target)

def dataprep_rle(n):
    """Genera una lista con rachas repetidas de dimensión n.
    Devuelve una lista.
    """
    
    pass

# I.A.2 Búsqueda de duplicados manteniendo orden de aparición
def find_duplicates(lst):
    #creamos una lista
    lst_aux = []
    lst_final = []

    #queremos que llame a este metodo para cada uno de los elementos
    longitud = len(lst)
    for i in range(longitud):
        if lst[i] not in lst_aux:
         lst_aux.append(lst[i])
    
        else: 
            if lst[i] not in lst_final:
                lst_final.append(lst[i])


    return lst_final           
    

# I.A.3 Búsqueda de par que suma target con complejidad O(n)
def has_sum_pair(par):
    """Dada una tupla (lst, target), devuelve True si existen dos elementos
    distintos en lst que sumen target; de lo contrario devuelve False.
    """
    list = par[0]
    longitud = len (list)
    target = par[1]

    for n in range(longitud):
        for i in range (n+1, longitud):
            if n + i == target:
                return True
        
    else:
        return False
    

# I.B.1 RLE Naive / Ingenuo
def rle_encode_naive(lst):
    """Codificación RLE utilizando operador + concatenador de listas."""

    longitud = len (lst)
    last_lst = []
    n = 0
    while n < longitud:
        n_elem = 0 #Empiezo en 0 elementos y luego sumo 1 
        elemento1 = lst[n]
        for i in range (n+1, longitud):
            elemento_aux = lst[i]
            if elemento1 == elemento_aux:
                n_elem = n_elem + 1 #Cuento el numero de veces que se repiten el elemento para despues poder saltarmelo en el indice y meterlo en la lista final
            else:
                break
        
        
        n = n + n_elem + 1 #
        last_lst = last_lst + [(elemento1, n_elem+1)]

                
    return last_lst

# I.B.2 RLE Optimized / Óptimo
def rle_encode_optimized(lst):
    longitud = len (lst)
    last_lst = []
    n = 0
    while n < longitud:
        n_elem = 0
        elemento1 = lst[n]
        for i in range (n+1, longitud):
            elemento_aux = lst[i]
            if elemento1 == elemento_aux:
                n_elem = n_elem + 1
            else:
                break
        
        
        n = n + n_elem + 1
        last_lst.append((elemento1, n_elem+1))

                
    return last_lst

        
            

        
  
 
       
       


# Función auxiliar para generar una gráfica de una serie de datos.
def plot_single_curve(
    x,
    y,
    title="Gráfica de Datos",
    xlabel="Eje X",
    ylabel="Eje Y",
    label=None,
    style="o-",
    color="b",
    grid=True,
    filename=None,
    figsize=(8, 5),
):
    """Genera y muestra/guarda una gráfica limpia para una única serie de datos."""
    plt.figure(figsize=figsize)  # Crea la figura con el tamaño indicado

    # Dibuja la curva
    plt.plot(x, y, style, color=color, label=label)

    # Personalización básica de ejes y título
    plt.title(title)  # Asigna el título
    plt.xlabel(xlabel)  # Etiqueta X
    plt.ylabel(ylabel)  # Etiqueta Y

    if grid:
        plt.grid(True, linestyle="--", alpha=0.6)

    if label:
        plt.legend(
            loc="best"
        )  # Muestra la leyenda si se definió una etiqueta

    plt.tight_layout()

    # Guarda la gráfica en un fichero si se especifica un nombre
    if filename:
        plt.savefig(
            filename, format=filename.split(".")[-1], dpi=300
        )  #

    plt.show()  # Muestra la figura


def init_cd(n: int)-> np.ndarray:
    p = len(n) * [-1]  # se crea una tabla (lista) de tamaño |n| en la que 
                       # todas las componentes se inicializan a -1
    return p

def find_cc(ind: int, p_cd: np.ndarray) -> int:
    # find the representative
    z = ind
    
    # get the root (representant)
    while p_cd[z] > -1:
        z = p_cd[z]
        
    # compress the path from u to the root
    while p_cd[u] >-1:
        y = p_cd[u]
        p_cd[u] = z
        u = y
    return z


def union(rep_1: int, rep_2: int, p_cd: np.ndarray) -> int:
        
        x = find_cc(rep_1)
        y = find_cc(rep_2)
        
        if x == y:
            return None
        
        if p_cd[y] < p_cd[x]:      # T_y is taller
            p_cd[x] = y
            return y  
        
        elif p_cd[y] > p_cd[x]:    # T_x is taller
            p_cd[y] = x 
            return x
        
        else:                # T_x, T_y have the same lenght
            p_cd[y] = x
            p_cd[x] -= 1        # Increase the height
            return   x    




'que reciba un CD en el array p_cd y devuelva un diccionario cuyas claves sean los representantes de los'
'subconjuntos del CD y donde el valor de la clave u del dict sea una lista con los miembros del subconjunto'
'representado por u , incluyendo, por supuesto el propio u .'

def cd_2_dict(p_cd: np.ndarray)-> dict:

    diccionario = dict()
    longitud = len (p_cd)
    for i in range (longitud):
        representante = diccionario(find_cc(i, p_cd))

        if representante not in diccionario:
            diccionario[representante] = []

        diccionario[representante].append(i)


            
def ccs(n: int, l: list)-> dict: 
    diccionario = dict ()
    longitud = len (l)
    for i in range (longitud):
        representante = l [i]
        diccionario 

