#!/bin/bash
# Create and activate environment
conda create --name quantum python=3.9 -y
conda activate quantum
# Install Qiskit
pip install qiskit qiskit[all]
# Save IBMQ token
qiskit ibmq save --token YOUR_API_TOKEN_HERE --name ibm-q
