import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_state_city

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.h(0)

state = Statevector.from_instruction(qc)
plot_state_city(state)

phis = np.linspace(0, 2*np.pi, 13)
results = []
for phi in phis:
    qc2 = QuantumCircuit(1,1)
    qc2.h(0)
    qc2.rz(phi, 0)
    qc2.h(0)
    qc2.measure(0,0)
    counts = execute(qc2, Aer.get_backend('qasm_simulator'), shots=1000).result().get_counts()
    p0 = counts.get('0',0)/1000
    results.append((phi, p0))
print(results)
