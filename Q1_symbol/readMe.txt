Objective: Displaying contents of symbol table and literal table of given assembly program.

Language Used:Python3

Steps of Execution:
  User has to input Assembly file which contains assembly code and this program will
  display contents of symbol table and literal table of the same.

Assumptions:
1)All instruction are of length 32 bit.
2)Sections sequence: .data, .bss ,.text
3)*all register names and keywords in small letters
4)There is some confusion in jmp instruction for address calculation as it depends where
your label is located.
    will update it shortly.

Data Structure used for storing symbol table and literal table:
Singly Linked List
    *I know it's time complexity is large will do Hash table implementation of the same in coming days.

Files Included: symbol_and_literal.py(Code File)
                ref.asm(Assembly File)

Description of Code:
  All instructions under section .data taken care by the function : data()
  All instructions under section .bss taken care by the function : bss()
  All instructions under section .text taken care by the function : text()

Submitted By:
  Name:BHALKE PARESH RAMESH
  Class:MCS(I)
  Roll No: R19111006

