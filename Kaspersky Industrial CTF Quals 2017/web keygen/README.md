**Category: Web Points: 700**
> crackme! http://95.85.55.168/vmctf.html

## 手順
vmctf.htmlを見ると変数名・クラス名が全て難読化されて読みづらいのでvar_{Coの数}_に変更する
使用スクリプト: `fix_coco.py`  
出力: `vmctf2.html`  

ソースを観察するとパスワードを処理してる部分がVM化されてるのがわかる
GetFlag.var_20_()がバイトコード
![](https://gyazo.com/45e3c6d6fa92ff94fc0b703a8bcc4d3b.png)

var_19_().var_28_()がバイトコードのディスパッチ処理
![](https://gyazo.com/27b07a44aeee412b8cd98db2f17a414c.png)

バイトコードのハンドラーを観察していくとそれぞれがアセンブラレベルの処理を実行しているのがわかる
![](https://gyazo.com/3fca3bcbe6c044de2bb6817e7e6f94d7.png)

