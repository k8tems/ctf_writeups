---


---

<h1 id="super-encryption">Super Encryption!</h1>
<p><strong>60 points</strong></p>
<pre><code>My friend sent me a flag encrypted with an encryption program. 
Unfortunately, the decryption doesn't seem to work. 
Please help me decrypt this: dufhyuc&gt;bi{{f0|;vwh&lt;~b5p5thjq6goj}
</code></pre>
<p><img src="https://gyazo.com/6446894bd88cdd6a27a5c4d772013086.png" alt=""></p>
<p>The decryption is not implemented in the attached file (<code>superencrypt</code>) so the inverse of the encryption  has to be handcrafted.</p>
<p><strong>The entrypoint(<code>main</code>) in IDA</strong>
<img src="https://gyazo.com/5f9c8326bd25bbb7cc75446627dd3461.png" alt=""></p>
<p>A very straight forward branch is made to <code>encrypt</code> and <code>decrypt</code> based on the user input.</p>
<p><img src="https://gyazo.com/89ada7f09acc77d6445ba25e8b03ee0f.png" alt=""></p>
<p>As expected, nothing happens in the <code>decrypt</code> function.</p>
<p><img src="https://i.gyazo.com/ccc8bcd8ff5d4e4620989b5f3aaec75a.png" alt=""></p>
<p>Prior to calling <code>encrypt</code>, the parameters are copied to <code>rsi</code> and <code>rdi</code>  and later on copied to the stack in the function entrypoint.</p>
<p><img src="https://gyazo.com/6fbec922fbd081dfcd3fb016b984b326.png" alt=""></p>
<p><code>rdi</code> points to the given string<br>
<code>rsi</code> holds <code>0x100</code> which is probably the buffer length</p>
<p><img src="https://gyazo.com/eb2d18a9817ede5b76295abae145c9e3.png" alt=""></p>
<p>Although there are 3 loops in the function, the encryption itself is done in the first one. To be specific, a key is derived from the loop counter(<code>i</code>) and added to each character.</p>
<p><img src="https://gyazo.com/17b63a8897d6dd55a517c2912cf4abd9.png" alt=""></p>
<p>The second and third loops are responsible for reversing the order of the cipher in chunks of 5 and 3 respectively.</p>
<p>The following steps need to be taken for decryption.</p>
<ol>
<li>Reverse order by chunks of 3</li>
<li>Reverse order by chunks of 5</li>
<li>Derive key from loop counter and subtract from each character</li>
</ol>
<p>One thing to note is that instead of deriving the key myself, I ripped the key by logging the values stored in <code>v13</code>(<code>xmm0</code>).<br>
See <code>decrypt.py</code> for the finished script.</p>

