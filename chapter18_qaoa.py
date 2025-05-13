from qiskit_optimization.problems import QuadraticProgram
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit import Aer
from qiskit.algorithms import QAOA
import numpy as np

N=4; mu=np.random.rand(N); Sigma=np.random.rand(N,N); Sigma=(Sigma+Sigma.T)/2; lam=0.5; K=2
prog=QuadraticProgram()
for i in range(N): prog.binary_var(name=f'x{i}')
prog.minimize(quadratic=Sigma, linear={i: -lam*mu[i] for i in range(N)})
prog.linear_constraint(linear={f'x{i}':1 for i in range(N)}, sense='==', rhs=K)
qubo=prog.to_ising()[0]
qaoa=MinimumEigenOptimizer(min_eigen_solver=QAOA(reps=1,quantum_instance=Aer.get_backend('qasm_simulator')))
res=qaoa.solve(qubo)
print(res.x, res.fval)
