import julia
from julia import SpectralGM

# julia.install() # uncomment this if you run into error. Then try again. After that, in future run, you should comment this line out.
j = julia.Julia()
x = j.include("test.jl")

# print(type(x)) # in case you are curious of the type

hiddenf, s1, s2 = x()

hiddenf(5, 5)


SpectralGM.test("Huong")
SpectralGM.greet()

