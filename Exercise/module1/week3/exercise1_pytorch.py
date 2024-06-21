import torch
import torch.nn as nn
'''
    In torch.sum() function 
        dim = 0 that mean calculate x axis
        keepdim: [= True] that mean keep all of axis after you calculated
        keepdim: [=False] remove axis

        
'''
class SoftMax(nn.Module):
    ''''
        Class customize with purpose calcualate softmax of tensor
        >> tensor = torch.Tensor([1,2,3])
        >> softmax  = SoftMax(dim=0)
        >> print(softmax(tensor))
        tensor([0.0900, 0.2447, 0.6652])
    '''

    def __init__(self, dim=1):
        super().__init__()
        self.dim = dim

    def forward(self, input):
        return torch.exp(input) / torch.sum(torch.exp(input), dim=self.dim, keepdim=True)

class SoftMaxStable(nn.Module):
    ''''
        Class customize with purpose calcualate softmax of tensor
        >> tensor = torch.Tensor([1,2,3])
        >> softmax  =SoftMaxStable(dim=0)
        >> print(softmax(tensor))
        tensor([0.0900, 0.2447, 0.6652])
    '''

    def __init__(self, dim=1):
        super().__init__()
        self.dim = dim

    def forward(self, input):
        c, _ = torch.max(input, dim=self.dim, keepdim=True)
        return torch.exp(input - c) / torch.sum(torch.exp(input -c), dim=self.dim, keepdim=True)
    

if __name__ == "__main__":

    tensor = torch.Tensor([1,2,3])
    softmax  = SoftMax(dim=0)
    print(f'Question 1: {softmax(tensor)}\n')

    tensor = torch.Tensor([1,2,300000000])
    softmax  = SoftMax(dim=0)
    print(f'Question 2: {softmax(tensor)}\n')

    tensor = torch.Tensor([5,2,4])
    softmax  = SoftMax(dim=0)
    print(f'Question 3: {softmax(tensor)} \n')

    tensor = torch.Tensor([1,2,3])
    softmax_stabel  = SoftMaxStable(dim=0)
    print(f'Question 4: {softmax_stabel(tensor)}\n')