Programming Assignment 3: Highest Value Longest Common Sequence

Om Vaddi (15302285)
Thomas Alvarado (65211333)

Instructions:
- After cloning, run "cd COP4533-Highest-Value-Longest-Common-Sequence"
- Create an input file in the files folder.
- See assumptions section for file formatting.
- Run "python src/sequence.py".
- Enter the file path when prompted. ex: files/file1.txt
- Read output.

Example input (files/example.in):  
3  
a 4  
b 2  
c 3  
abcb  
bcab

Example output (files/example.out):  
7  
bcb

Assumptions:
- The first line of the file should be an integer K >= 1, where K represents how many letters are in the alphabet. The next K lines should each contain a character and its  value seperated by a space. The next line should contain string A. The next and final line should contain string B. Both string A and B should only contain characters found in the alphabet.
- The output will display the value of the highest value common subsequence of string A and B on the first line. The second line will display the highest value common subsequence.

Question 1: Empirical Comparison 
![Runtime Graph](runtime_graph.png) 
 
Question 2: Recurrence Equation 
Let the two strings be: 
A = a1a2...a_n,   B = b1b2...b_m 
Let v(c) be the value of character c from the fixed alphabet. 
Let OPT(i, j) be the maximum total value of a common subsequence of the first i characters of A and the first j characters of B. 
The recurrence equation is: 
            {0                                  if i = 0 or j = 0 (base case) 
OPT(i, j) = {OPT(i-1, j-1) + v(a_i)             if a_i = b_j
            {max(OPT(i-1, j), OPT(i, j-1))      if a_i != b_j 

This recurrence is correct because when the characters of each string matches, it will include this character in the subsequence 
and thus add its value. When the characters do not match, it will keep the highest value of the previous subsequences. 
The equation considers all possibilites for either including or skipping each character, and builds the correct solution 
from smaller subproblems.