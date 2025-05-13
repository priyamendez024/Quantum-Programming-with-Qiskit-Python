# Simplified Shor's example for N=15, a=7
import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from qiskit.quantum_info import Statevector

# Inverse QFT function
def inverse_qft(n):
    qc = QuantumCircuit(n, name='iQFT')
    for i in range(n//2):
        qc.swap(i, n-1-i)
    for j in range(n):
        for k in range(j):
            qc.cp(-np.pi/2**(j-k), k, j)
        qc.h(j)
    return qc

N=15; a=7; n=int(np.ceil(np.log2(N)))
qc = QuantumCircuit(2*n, n)
qc.h(range(n))
qc.x(range(n,2*n))
# modular exp placeholder
# apply inverse QFT
qc.append(inverse_qft(n).to_gate(), range(n))
qc.measure(range(n), range(n))
counts = execute(qc, Aer.get_backend('qasm_simulator'), shots=1024).result().get_counts()
print(counts)
