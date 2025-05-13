from qiskit import IBMQ
import pandas as pd

provider=IBMQ.load_account(); backend=provider.get_backend('ibmq_lima')
props=backend.properties()
data={'qubit': list(range(len(props.qubits))),
      't1': [props.t1(i) for i in range(len(props.qubits))],
      't2': [props.t2(i) for i in range(len(props.qubits))]}
df=pd.DataFrame(data)
print(df)
