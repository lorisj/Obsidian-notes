# State
**Def (quantum register):** A quantum register $Q$ is the equivalent of a qubit. It can take values either in the hilbert space ($Q \in \mathcal{H}$), meaning $Q$ is a state vector or it can be a density operator ($Q \in L(\mathcal{H},\mathcal{H})$). 

**Def(classical register):** A classical register $R$ can be two things. Either it is a single real number, $R \in \mathbb{R}$ or it is a random variable that takes values in the real numbers $R \in RV(\mathbb{R})$.


**Def (world state):** A world state is the state that the computer could be in. This is the state of all quantum registers combined with all classical registers. Think of this as the state that the quantum computer could be in, given a specific measurement result.

**Def(total state):** The total state is the most general description of all possible states of the system. It consists of a random variable of all of the world states, with each possible value corresponding to a measurement result. Essentially every time a measurement occurs, the world state branches off once per possible measurement outcome.

