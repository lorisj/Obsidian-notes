# Pairing
### Metadata
Path: #pathCOMP
Tags:

### Prerequisites

### Introduction


### Pairing Function Definition 
**Def(Pairing Function):** For any pair of natural numbers $(x,y)\in \omega^2$, assign a codeword $<x,y>\in \omega$. Turns out there is a bijection from $\omega^2 \leftrightarrow \omega$, namely:
$<x,y>=\frac{1}{2}(x^2+2xy+y^2+3x+y)$

*This function is computable, so we can use it to show other things are computable.*

**Cor(Pairing Function on Multiple Inputs):** If we have a pairing function $<x,y>\to \omega$, we can create a $n$ pairing function that takes in $n \in \omega$ arguments $(x_1 \ldots x_n \to <n,<x_1,<x_2,<\ldots <x_{n-1}, x_n>\ldots >)$. This is a bijection from $\omega^{<\omega} \to \omega$.

### Pairing on Subsets Lemma
**Lem(Pairing on Subsets):** We can identify $A \subseteq \omega^2$ with $\{<x,y>:(x,y)\in A\}$
*Applying this on the graph of a function would give us a way to represent functions $f:\omega^n \to \omega^m$ with a  single natural number, and therefore use them in our algorithms*



