from qiskit import QuantumCircuit
from qiskit.visualization import circuit_drawer

prep = QuantumCircuit(2, name='Prep')
prep.h([0,1])

oracle = QuantumCircuit(2, name='Oracle')
oracle.cz(0,1)

diffusion = QuantumCircuit(2, name='Diffusion')
diffusion.h([0,1])
diffusion.x([0,1])
diffusion.cz(0,1)
diffusion.x([0,1])
diffusion.h([0,1])

grover = prep.compose(oracle).compose(diffusion)
grover.draw(output='mpl')
