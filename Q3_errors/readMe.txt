Objective: Displaying Errors in a sample assembly program given as input.

Language Used:Python3

Steps of Execution:
  User has to input Assembly file which contains assembly code and this program will
  display errors of the same(if any) .

Output:Display all errors in one go(by line number)

Assumptions:
1)section sequence - data,bss,text
*all register names and keywords in small letters


Data Structure used for storing symbols for (checking of redefine or undefine symbols)
Singly Linked List
    *I know it's time complexity is large will do Hash table implementation of the same in coming days.

Files Included: error.py(Code File)
                referror.asm(Assembly File)

Description of Code:
  All instructions under section .data taken care by the function : data()
  All instructions under section .bss taken care by the function : bss()
  All instructions under section .text taken care by the function : text()
  For instructions having one operand some helper functions used like proper_sib(),base_index(),base_scale(),base().

Submitted By:
  Name:BHALKE PARESH RAMESH
  Class:MCS(I)
  Roll No: R19111006


