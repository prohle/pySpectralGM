**Step 1**: Install julia in python<br>
<code>pip install julia</code>
<br><br>
**Step 2**: Install julia -> Once complete, open **cmd** terminal, type<br>
<code>julia</code>
<br><br>
**Step 3**: Once julia terminal opens, install Pycall<br>
<code>import Pkg; Pkg.add("PyCall")</code>
<br><br>
**Step 4**: Install SpectralGM, type<br>
<code>]</code>
<br><br>
**Step 5**: Package management terminal will appear, it will look something like so <code>(@v1.4)Pkg></code>, type<br>
<code>add https://github.com/prohle/SpectralGM.jl.git</code>
<br><br>
**Step 6**: Hit the 'Backspace' key on the keyboard to go back to Julia terminal, type the below to exist Julia<br>
<code>exit()</code>
<br><br>

**Step 7**: (Optional) If path to python.exe is not set to be the same. Uncomment the line <code>julia.install()</code> in the test.py file
<br><br>

**Step 8**: We now test our setup with Python
<code>python test.py</code>
<br><br>

**Troubleshoot**: If python.exe path is not the same, you will receive a notice as such. Look at step 7.

Now, you are ready to go!