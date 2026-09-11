from qiskit import QuantumCircuit, QuantumRegister

qubits = QuantumRegister(2, name="q")
circuit = QuantumCircuit(qubits)

q0, q1 = qubits

circuit.h(q0)
circuit.cx(q0, q1)
circuit.measure_all()

fig = circuit.draw("mpl")
fig


import matplotlib.pyplot as plt

circuit.draw("mpl")
plt.show()
