from qiskit.ignis.mitigation.measurement import complete_meas_cal, CompleteMeasFitter
from qiskit import Aer, execute, QuantumCircuit

n=3
cal_circuits, labels = complete_meas_cal(qubit_list=list(range(n)), circlabel='meas_cal')
cal_results = execute(cal_circuits, Aer.get_backend('qasm_simulator'), shots=1024).result()
fitter=CompleteMeasFitter(cal_results, labels)
meas_filter=fitter.filter

qc=QuantumCircuit(n, n)
qc.h(range(n)); qc.measure(range(n), range(n))
raw=execute(qc, Aer.get_backend('qasm_simulator'), shots=2048).result().get_counts()
mitigated=meas_filter.apply(raw)
print("Raw:", raw, "Mitigated:", mitigated)
