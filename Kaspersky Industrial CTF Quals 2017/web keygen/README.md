**Category: Web Points: 700**
> crackme! http://95.85.55.168/vmctf.html

## Writeup
The first step is to deobfuscate the variable names  
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

Log the behavior in every handler to obtain a better understanding of the flow  
Script: `trace.js`  
Output: `runtrace.txt`  

Create another script that disassembles the vmed code by ignoring JMPs/CALLs/RETs  
Script: `disasm.js`  
Output: `disasm.txt`  

※メモリアドレスのオペランド(`Memory`クラス)のコンストラクタで最終的に計算されたアドレスではなく、  
途中で取得されてるレジスタやオフセットを記録しないと正しく逆アセンブルが出来ないので注意が必要  

逆アセンブルされた処理をC++に書き直す  
出力: `decompile.cpp`

`func_4C7`でパスワードのハッシュのようなものを作成し、  
結果が`0x33E5AE40`なら成功フラグが作成されてユーザーに返されるのがわかる  

`func_4C7`のテーブルをグーグル検索するとCRC32らしいが、  
同一polynomial(0x4C11DB7)とinitial value(0x12345678)でcrc32を生成しても  
解答が一致しないためアルゴリズムが微妙に変えられてると思われる  
※`"password"`をfunc_4C7に通すと0x8FB99124が返ってくる  
![](https://gyazo.com/7202eacc8e3e6336f179793ee4358d2e.png)

> All flags start with KLCTF.

`func_4C7`の逆関数を作成するのは難しいのでフラグの最初の5文字が`"KLCTF"`で固定されているのに目を付ける  
フラグの生成がパスワードと`func_0.key`の単純なxorで済まされてるので  
パスワードの最初の5文字は`func_0.key`と`"KLCTF"`のxorで求まる  
`func_4C7`の第3引数が`8`な事からパスワードが8文字なのがわかるので  
残り3文字を総当たり攻撃(100文字^3通り)すればパスワードが求まる  
