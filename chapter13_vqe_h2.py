from qiskit_nature.drivers import PySCFDriver
from qiskit_nature.problems.second_quantization.electronic import ElectronicStructureProblem
from qiskit_nature.converters.second_quantization import QubitConverter
from qiskit_nature.mappers.second_quantization import JordanWignerMapper
from qiskit.algorithms import VQE, NumPyMinimumEigensolver
from qiskit.algorithms.optimizers import SLSQP
from qiskit.circuit.library import TwoLocal
from qiskit import Aer

driver=PySCFDriver(atom='H .0 .0 .0; H .0 .0 0.74', basis='sto3g')
esp=ElectronicStructureProblem(driver)
qubit_op=QubitConverter(JordanWignerMapper()).convert(esp.second_q_ops()[0], num_particles=esp.num_particles)
exact=NumPyMinimumEigensolver().compute_minimum_eigenvalue(qubit_op)
ansatz=TwoLocal(qubit_op.num_qubits,['ry','rz'],'cx',reps=2)
vqe=VQE(ansatz,optimizer=SLSQP(),quantum_instance=Aer.get_backend('statevector_simulator'))
res=vqe.compute_minimum_eigenvalue(qubit_op)
print("Exact:", exact.eigenvalue.real, "VQE:", res.eigenvalue.real)
