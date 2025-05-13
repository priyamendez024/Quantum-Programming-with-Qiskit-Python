import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from qiskit.circuit.library import QFT
from qiskit.visualization import plot_histogram

theta=1/8; n_phase=3
qc=QuantumCircuit(n_phase+1, n_phase)
qc.x(n_phase)
qc.h(range(n_phase))
for j in range(n_phase):
    qc.cp(2*np.pi*theta*2**j, j, n_phase)
qc.append(QFT(n_phase, inverse=True).to_gate(), range(n_phase))
qc.measure(range(n_phase), range(n_phase))
counts = execute(qc, Aer.get_backend('qasm_simulator'), shots=1024).result().get_counts()
plot_histogram(counts)
