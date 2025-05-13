import numpy as np
from qiskit import QuantumCircuit, Aer
from qiskit_machine_learning.neural_networks import SamplerQNN
from qiskit_machine_learning.algorithms import NeuralNetworkClassifier
from qiskit.algorithms.optimizers import COBYLA
from sklearn import datasets
from sklearn.model_selection import train_test_split

iris=datasets.load_iris()
X=iris.data[:100,:2]/np.pi; y=iris.target[:100]
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=0.2,random_state=42)

n=2
from qiskit.circuit.library import TwoLocal
ansatz=TwoLocal(n,['ry','rz'],'cx',reps=2)
sampler=SamplerQNN(circuit=ansatz,input_params=ansatz.parameters[:n],weight_params=ansatz.parameters[n:],interpret=lambda counts: (counts.get('0'*n,0)-counts.get('1'*n,0))/sum(counts.values()))
clf=NeuralNetworkClassifier(neural_network=sampler,optimizer=COBYLA(maxiter=100))
clf.fit(Xtr,ytr)
print("Accuracy:", clf.score(Xte,yte))
