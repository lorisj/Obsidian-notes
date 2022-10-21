# Turing Machines
### Metadata
Path: #pathCOMP
Tags:

### Prerequisites
[[Algorithm#Introduction|algorithms]]

### Introduction

### Turing Machine Definition
**Def(Turing Machine):** A Turing machine consists of:
- 2 way infinite tape, divided into cells.
- Finite number of Internal states $Q = \{ q_0, q_1, \ldots q_n\}, n \ge 1$ 
- Symbols $S = \{b,1\}$ ($b$ for blank) but could be any finite list of symbols.
- Transition function $\delta: (Q\times S)\to (Q\times S \times \{L,R\})$ ($L,R$ dictates move left/right)

### Running a Turing Program
**Def(Running a Turing program):** At each step of the computation, read the cell under the head, and do one of:
- Change the state
- Replace the symbol at the current position with a new symbol
- Move the head $L/R$ by one cell

A computation with *one input* $x \in \omega$ starts with state $q_1$ with tape:
        $\vee$
$[b|b|b|1|1|\ldots|1|b|b|\ldots]$
where there are $x$ many $1$s.
Then run according to $\delta$. If the state ever becomes $=q_0$ , then the computation halts, and output $=$ the number of $1$s on the tape at the end. (or you could ask for the number of consecutive $1$s). Note that the computation might run forever, and never halt.

A computation with *multiple inputs* $\bar x \in \omega^n$ starts with either
- n inputs separated by one blank
- $<\bar{x}> \in \omega$ as the output of $n$ [[Pairing#Pairing Function Definition|pairing function]] $<._n>$ 

### Configurations Definition
**Def(Configurations):** If we think of the act of running a computation, you could think of the Turing machine at each step as a configuration, containing:
1) A current state $q$
2) A symbol $s$ that is currently being scanned
3) A finite sequence of symbols $\bar{l} = l_0, \ldots l_m$ representing all symbols to the left of the head
4) A finite sequence of symbols $\bar{r}=r_0, \ldots r_n$ representing all symbols to the right of the head

**Cor(Numbering configurations):** $\implies$ we  can number the configurations
