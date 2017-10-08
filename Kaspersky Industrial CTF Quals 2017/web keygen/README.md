**Category: Web Points: 700**
> crackme! http://95.85.55.168/vmctf.html

## 手順
vmctf.htmlを見ると変数名・クラス名が全て難読化されて読みづらいのでvar_{Coの数}_に変更する  
使用スクリプト: `fix_coco.py`  
出力: `vmctf2.html`  

ソースを観察するとパスワードを処理してる部分がVM化されてるのがわかる  
GetFlag.var_20_がバイトコード  
![](https://gyazo.com/45e3c6d6fa92ff94fc0b703a8bcc4d3b.png)

var_19_().var_5_()がバイトコード1バイトフェッチする処理  
var_19_().var_28_()がバイトコードのディスパッチ処理  
![](https://gyazo.com/27b07a44aeee412b8cd98db2f17a414c.png)

バイトコードのハンドラーを観察していくとそれぞれがアセンブラレベルの処理を実行しているのがわかる  
![](https://gyazo.com/3fca3bcbe6c044de2bb6817e7e6f94d7.png)

VMで実行された処理の流れを理解するためにそれぞれのハンドラー内でロギングを行い、ラントレースを作成する  
使用スクリプト: `trace.js`  
出力: `runtrace.txt`  

又、JMP/CALL/RETを無視して上から下まで逆アセンブルするスクリプトも用意する  
使用スクリプト: `disasm.js`  
出力: `disasm.txt`  

逆アセンブルされた処理をC++に書き直す  
出力: `decompile.cpp`

`func_4C7`でパスワードのハッシュのようなものを作成し、  
結果が`0x33E5AE40`なら成功フラグが作成されてユーザーに返されるのがわかる  

`func_4C7`のテーブルをグーグル検索するとCRC32らしいが、  
同一polynomial(0x4C11DB7)とinitial value(0x12345678)でcrc32を生成しても  
解答が一致しないためアルゴリズムが微妙に変えられてると思われる  
※passwordをfunc_4C7に通すと0x8FB99124が返ってくる  
![](https://gyazo.com/7202eacc8e3e6336f179793ee4358d2e.png)

> All flags start with KLCTF.

`func_4C7`の逆関数を作成するのは難しいのでフラグの最初の5文字が`"KLCTF"`で固定されているのに目を付ける  
フラグの生成がパスワードと`func_0.key`の単純なxorで済まされてるので  
パスワードの最初の5文字は`func_0.key`と`"KLCTF"`のxorで求まる  
`func_4C7`の第3引数が`8`な事からパスワードが8文字なのがわかるので  
残り3文字を総当たり攻撃(100文字^3通り)すればパスワードが求まる  
