# test.py
# ! IMPORTANT: Do not run untill you have finished all steps in installation.md
import julia
from julia import SpectralGM

# julia.install() # uncomment this if you run into error. Then try again. After that, in future run, you should comment this line out.
j = julia.Julia()

## Part 1
# this is to test to call direct functions within Python code
x = j.include("test.jl")
# print(type(x)) # in case you are curious of the type
hiddenf, s1, s2 = x()
hiddenf(5, 5)

## Part 2
# this is to test to call functions from imported packages from julia.
# we can see that we call the function just like we call a python function.
SpectralGM.test("Huong")
SpectralGM.greet()

