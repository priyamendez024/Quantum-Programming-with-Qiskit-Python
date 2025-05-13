from qiskit_nature.drivers import PySCFDriver
from qiskit_nature.problems.second_quantization.electronic import ElectronicStructureProblem
from qiskit_nature.algorithms import GroundStateEigensolver, VQEUCCFactory
from qiskit_nature.converters.second_quantization import QubitConverter
from qiskit_nature.mappers.second_quantization import JordanWignerMapper
from qiskit import Aer
from qiskit.algorithms.optimizers import SPSA

driver=PySCFDriver(atom='H .0 .0 .0; H .0 .0 0.74', basis='sto3g')
prob=ElectronicStructureProblem(driver)
conv=QubitConverter(JordanWignerMapper())
vqe_solver=VQEUCCFactory(quantum_instance=Aer.get_backend('statevector_simulator'),optimizer=SPSA(maxiter=100),mapper=JordanWignerMapper())
gsc=GroundStateEigensolver(conv,vqe_solver)
res=gsc.solve(prob)
print("Energy:", res.total_energies[0])
