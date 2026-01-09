import time 
import hashlib

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

numeroRandom = hashlib.sha256(str(ruido).encode()).hexdigest()

numeroRandom = int(numeroRandom, 16)

print(numeroRandom)
