import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

def grover_circuit(n, marked, iterations):
    qc = QuantumCircuit(n, n)
    qc.h(range(n))
    for _ in range(iterations):
        bits = [i for i,b in enumerate(format(marked,f'0{n}b')) if b=='0']
        qc.x(bits)
        qc.h(n-1)
        qc.mct(list(range(n-1)), n-1)
        qc.h(n-1)
        qc.x(bits)
        qc.h(range(n))
        qc.x(range(n))
        qc.h(n-1)
        qc.mct(list(range(n-1)), n-1)
        qc.h(n-1)
        qc.x(range(n))
        qc.h(range(n))
    qc.measure(range(n), range(n))
    return qc

n=3; marked=5; iterations=int(np.pi/4*np.sqrt(2**n))
counts = execute(grover_circuit(n,marked,iterations), Aer.get_backend('qasm_simulator'), shots=1024).result().get_counts()
plot_histogram(counts)
