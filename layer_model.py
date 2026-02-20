import numpy as np

# Layer model
def layer_model(n):
    Ta = 255 # above atmo temp in K 
    Ts = [0] * n # init list of surface temperatures
    for i in range(n):
        Ts[i] = Ta * (1.19) ** (i + 1) # temp of n bb layers add i + 1 bc i starts at 0
    return(Ts)
print(layer_model(4))
