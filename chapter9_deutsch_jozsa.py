import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

def constant_zero_oracle(n):
    return QuantumCircuit(n+1, name='Uf_const0')

def parity_oracle(n):
    qc = QuantumCircuit(n+1, name='Uf_parity')
    for i in range(n):
        qc.cx(i, n)
    return qc

def deutsch_jozsa(n, oracle):
    qc = QuantumCircuit(n+1, n)
    qc.x(n)
    qc.h(range(n+1))
    qc.append(oracle, range(n+1))
    qc.h(range(n))
    qc.measure(range(n), range(n))
    return qc

for oracle in [constant_zero_oracle(3), parity_oracle(3)]:
    counts = execute(deutsch_jozsa(3, oracle), Aer.get_backend('qasm_simulator'), shots=1024).result().get_counts()
    print(counts)
