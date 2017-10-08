**Category: Web Points: 700**
> crackme! http://95.85.55.168/vmctf.html

## Writeup
**The first step is to deobfuscate the variable names**  
Script: fix_coco.py  
Output: `vmctf2.html`  

As you can see in `vmctf2.html` the functionality that processes the password is vmed    
GetFlag.var_20_ represents the bytecode  
![](https://gyazo.com/45e3c6d6fa92ff94fc0b703a8bcc4d3b.png)  

var_19_().var_5_() represents the method to fetch 1 instruction byte  
var_19_().var_28_() dispatches the byte code to the corresponding handler  
![](https://gyazo.com/27b07a44aeee412b8cd98db2f17a414c.png)

Each handler represents an x86 instruction  
![](https://gyazo.com/3fca3bcbe6c044de2bb6817e7e6f94d7.png)

**Log the behavior in every handler to obtain a better understanding**  
Script: `trace.js`  
Output: `runtrace.txt`  
Variables and classes are renamed in trace.js for the sake of visual aid

**Create another script that disassembles the vmed code from top to bottom by not executing JMPs**  
Script: `disasm.js`  
Output: `disasm.txt`  

Note that in order to get an accurate disassembly, the constructor of class `Memory` has to be modified to  
save the registers and offsets of the operand for later reference.

**Rewrite the disassembly to C++**  
出力: `decompile.cpp`

As seen in `decompile.cpp`, `func_4C7` creates a hash-like value of the password and if it matches with 0x33E5AE40,   
the flag is generated and returned to the user  

Creating an inverse function of `func_4C7` is not feasible.  
However, we do know that the flag starts with `"KLCTF"` according to the ctf homepage and   
we also know that it's derived from the password with a simple xor with a fixed key(`func_0.key`).  
Therefore the first 5 characters of the password can be computed by XORing `func_0.key` and `"KLCTF"`.  
The 3rd parameter in `func_4C7` representing the number of iterations is 8 implying the password length. 
This leaves us with 3 characters and 100^3 different combinations which can be easily bruteforced.  
