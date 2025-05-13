from qiskit import QuantumCircuit, Aer, execute
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector, plot_histogram

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.barrier()
qc.measure([0, 1], [0, 1])

state = Statevector.from_instruction(qc.remove_final_measurements(inplace=False))
plot_bloch_multivector(state)

counts = execute(qc, Aer.get_backend('qasm_simulator'), shots=1000).result().get_counts()
plot_histogram(counts)
