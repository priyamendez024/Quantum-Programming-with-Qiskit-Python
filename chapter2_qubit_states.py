from qiskit import QuantumCircuit
from qiskit.visualization import plot_bloch_multivector
from qiskit.quantum_info import Statevector

theta = 3.14159/3
phi = 3.14159/4

qc = QuantumCircuit(1)
qc.ry(theta, 0)
qc.rz(phi, 0)

state = Statevector.from_instruction(qc)
plot_bloch_multivector(state)
