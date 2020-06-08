Step 1: Install julia in python
pip install julia

Step 2: Install julia -> Once complete, from cmd, type
julia

Step 3: Once julia terminal opens, install Pycall
import Pkg; Pkg.add("PyCall")

Step 4: Install SpectralGM, type
]

Step 5: Package management terminal will appear Pkg>, type
add https://github.com/prohle/SpectralGM.jl.git

Step 6: Hit the 'Backspace' key on the keyboard to go back to Julia terminal, type the below to exist Julia
exit()

Step 7: (Optional) If path to python.exe is not set to be the same. Uncomment the line 'julia.install()' in the test.py file

Step 8: Navigate to getStarted folder, we now test our setp
python test.py

If python.exe path is not the same, you will receive a notice as such. Look at step 7.

Now, you are ready to go!