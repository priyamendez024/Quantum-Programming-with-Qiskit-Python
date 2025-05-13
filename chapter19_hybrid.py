from qiskit import Aer, execute, QuantumCircuit
from qiskit.algorithms.optimizers import COBYLA

def run_hybrid(qc, shots=1024):
    backend=Aer.get_backend('qasm_simulator')
    def obj(x):
        bound=qc.bind_parameters({p:v for p,v in zip(qc.parameters, x)})
        counts=execute(bound,backend,shots=shots).result().get_counts()
        return 1 - (counts.get('0'*qc.num_qubits,0)/shots)
    from qiskit.algorithms.optimizers import COBYLA
    return COBYLA(maxiter=10).minimize(fun=obj, x0=[0.1]*len(qc.parameters))
