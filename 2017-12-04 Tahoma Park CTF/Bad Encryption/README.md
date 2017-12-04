---


---

<h1 id="bad-encryption">Bad Encryption</h1>
<p><strong>100 points</strong></p>
<pre><code>I was making an encryption program, but it is far from perfect. 
Instead of make the encryption work, I decided to just encrypt everything 100 times.
</code></pre>
<p>The first step is to rename all the variables for readability with <code>Pycharm</code>(Any modern IDE would work).</p>
<p><img src="https://gyazo.com/8500147c8e648d83249c10bec091b672.png" alt=""></p>
<p>The script seems to encode the input string(<code>"REDACTED"</code>)  as a PNG image.<br>
One can assume that instead of the hardcoded string <code>"REDACTED"</code>, the flag has been processed in the script to generate the attached 100 images.</p>
<p><strong>For each character/pixel…</strong></p>
<ul>
<li>The red and green are randomly generated.</li>
<li>The blue is calculated with the following formula</li>
</ul>
<pre><code>blue = round(character * (red/256) * (green/256) * 10)
</code></pre>
<p>The idea seems to be that I need to figure out the original character by reversing the formula.</p>
<p>Now to look at the properties of the encryption,</p>
<ul>
<li>Although 100 images are generated, each image is independent.</li>
<li>Blue values over 255 are capped to 255. (This took me a while to realize)</li>
<li>The <code>round</code> function introduces uncertainty making it impossible to create the inverse.</li>
</ul>
<pre><code>y = round(x)
y-0.5≦x&lt;y+0.5
</code></pre>
<p>Since it is impossible to create the inverse with only the RGB values we need to exploit that fact that there are 100 images.</p>
<p>For every pixel with a blue value under 256, we bruteforce the formula to find all possible characters.</p>
<p>For example,</p>
<pre><code>blue = 59
red = 51
green = 74

...
round(101 * 51/256 * 74/256 * 10) = 58
round(102 * 51/256 * 74/256 * 10) = 59
round(103 * 51/256 * 74/256 * 10) = 59
round(104 * 51/256 * 74/256 * 10) = 60
...
</code></pre>
<p>In this case the candidates are 102(<code>f</code>) and 103(<code>g</code>).<br>
We repeat this process for every single pixel in every single image.<br>
<img src="https://gyazo.com/be48ddfda91f7cd19843548cfd8f2bdb.png" alt=""></p>
<p>The flag can be restored by selecting the candidate that is most common.</p>
<p>See <code>decrypt.py</code> for the finished script.</p>

