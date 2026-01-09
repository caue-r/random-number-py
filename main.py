import time 
import hashlib

def jitter_random_256bits(iteracoes):
    b = time.perf_counter_ns()
    ruido = []

    for i in range(10000):
        a1 = time.perf_counter_ns()
        a2 = time.perf_counter_ns()
        c1 = time.perf_counter_ns()
        c2 = time.perf_counter_ns()

        deltaA = a2 - a1
        deltaC = c2 - c1

        # PCG 64-bit - 6364136223846793005 
        b = (b * 6364136223846793005 + deltaA + deltaC) & ((1 << 64) - 1)
        ruido.append(b)

    hash_hex = hashlib.sha256(str(ruido).encode()).hexdigest()
    return int(hash_hex, 16)

def random_input_user(maxValor):
    n = jitter_random_256bits(2000) #default 2000 iteracoes
    return n % (maxValor + 1)

max_valor = int(input("Max range: "))
numero= random_input_user(max_valor)
print(numero)