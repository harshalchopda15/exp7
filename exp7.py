# Quantum Algorithm and Computational Methods
# Program: SWAP gate using 3 CNOTs and simulate for |110⟩ and |111⟩

from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit_aer import Aer
from IPython.display import display

def swap_gate_simulation(input_state):
    qc = QuantumCircuit(3)

    # Initialize the input state
    if input_state == '110':
        qc.x([0, 1])  # qubits 0 and 1 set to |1⟩
    elif input_state == '111':
        qc.x([0, 1, 2])  # all qubits set to |1⟩

    # Implement SWAP between qubit 0 and qubit 2 using 3 CNOT gates
    qc.cx(0, 2)
    qc.cx(2, 0)
    qc.cx(0, 2)

    # Measure all qubits
    qc.measure_all()

    # Simulate
    backend = Aer.get_backend('qasm_simulator')
    result = backend.run(qc, shots=1024).result()
    counts = result.get_counts()

    # Display output
    print(f"\nInput State: |{input_state}⟩")
    display(qc.draw('mpl'))             # 🖼️ Circuit diagram (Matplotlib format)
    display(plot_histogram(counts))     # 📊 Output probabilities

# Run for |110⟩ and |111⟩
swap_gate_simulation('110')
swap_gate_simulation('111')