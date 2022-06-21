# Obsidian-notes

### Sections
Sections should generally start with ###, subsections with ####, ... reserve ## for special occasions.

Section titles should not contain the char ':'

Section titles should be in all caps other than words like "or", "and", etc.

The 1st section should be Prerequisites, and should list the introductions of all material that you use but don't link to later on. So for instance if you don't want to link the group definition every time you use it, place the introduction of the group note in the prerequisites section. You should also link the notation note if you use the notation.

The 2nd section should be Introduction, and should link to every following section in the note, as well as give a brief summary of the note.



### Links
Link aliases should not contain words like "the", "or", "and", ... in the beginning.

So for instance instead of the linked text being "<u>[the Group Ring]</u>" you should make it "the <u>[Group Ring]</u>"

Links to other notes should link as specific as possible, other than summary notes.



### Abbreviations/Directory
1) Highest level directory, gets no abbriviation: such as /Algebra, /Quantum_Information_Theory, ...

2) Next level directory, gets a 3 letter abbriviation: such as /Quantum_Information_Theory/Compression(CMP)

3) Next level directory  gets a 2 letter abbriviation, such as /Quantum_Information_Theory/Compression(CMP)/Schumacher-Compression(SC)

4) Next level directory gets a 1 letter abbriviation.

After that you should not make another directory.



### Summary Notes
Each abbriviated level should have its own summary note. 

Every summary note should contain a link to every file in the same directory (siblings), including the summary notes of directories that are in the same level. 

Each reference should ideally link to the introductions of each sibling note. 

So if I had /root/A(AAA)/B(BB), the summary note of A should have a link to the summary note of B, as well as to the introduction of every file in /A(AAA)



### Math Specific
Every Definition, Theorem, Lemma, Corollary should have a section title "i.e ###Squeeze Theorem" followed by the Thm/Lem/Cor, and if applicable, the proof should follow but be indented 1 time more than the Thm/Lem/Cor.

Every (Theorem, Thm), (Lemma, Lem), (Corollary, Cor) should look like this:

"###Name Theorem"

**Thm(Name of theorem):** Put the theorem result here

[TAB]Begin your proof here

[TAB]End proof here

