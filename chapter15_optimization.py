from qiskit import transpile, Aer, QuantumCircuit
qc=QuantumCircuit(4)
# ... build circuit ...
print("Before:", qc.depth(), qc.count_ops())
opt = transpile(qc, backend=Aer.get_backend('qasm_simulator'), optimization_level=3)
print("After:", opt.depth(), opt.count_ops())
