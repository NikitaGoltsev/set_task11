# I need to rewrite model with pytorch
import torch
import torch.nn as nn
import numpy as np

#  ### Example, I need to rewrite it ### # 
class SimpleModel():

    BaseView = lambda in_ch, out_ch : nn.Sequential(
        nn.Linear(in_ch, 32),  # first linear
        nn.ReLU(), # function of activation
        nn.Linear(32, out_ch, bias=False),  # second linear
        nn.ReLU()
    )

    def __init__(self) -> None:
        
        self.model = self.BaseView(64,10)

        return None
    
    def result(self) -> None:

        print(self.model, sep = '\n', end=' - simple view of nn torch model \n')

        return None
# ### ### #

class Lay_of_model():


    def __init__(self, kernel:int = 0, padd:int = 0, strt:int = 0, delay:int = 0) -> None:
        
        self.par_ker = kernel
        self.par_pad = padd
        self.straig = strt
        self.dly = delay

        return None

    def get
class My_model():

    def __lay_creat__(self, kernel:int = 0, padd:int = 0, strt:int = 0, delay:int = 0) -> np.array:

        return None

    def __init__(self) -> None:
        
        return None
