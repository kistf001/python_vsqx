import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.autograd import Variable

class _breathDetectNet(nn.Module):
    
    def __init__(self):
        super(_breathDetectNet, self).__init__()
        
        self.fc0 = nn.Linear(4200, 2048)
        self.fc1 = nn.Linear(2048, 1024)
        self.fc2 = nn.Linear(1024, 512)
        self.fc3 = nn.Linear(512, 256)
        self.fc4 = nn.Linear(256, 128)
        
    def forward(self, seq):
        
        seq = self.fc0(seq)
        seq = F.relu(seq)
        seq = self.fc1(seq)
        seq = F.relu(seq)
        seq = self.fc2(seq)
        seq = F.relu(seq)
        seq = self.fc3(seq)
        seq = F.relu(seq)
        seq = self.fc4(seq)
        seq = F.relu(seq)
        #seq = F.sigmoid(seq)

        return seq

class breathDetectNet(nn.Module):
    
    def __init__(self):
        super(breathDetectNet, self).__init__()

        self.A1 = nn.Sequential(# 1 ================
                                nn.Conv1d(1, 1024, 512, stride = 4, dilation = 1, padding=254),
                                nn.ReLU(),
                                nn.BatchNorm1d(1024),
                                nn.MaxPool1d(kernel_size=2, stride=0, padding=0)
                                )
                                
        self.A2 = nn.Sequential(# 2 ================
                                nn.Conv1d(1024, 128, 64, stride = 1,dilation = 1, padding=32),
                                nn.ReLU(),
                                nn.BatchNorm1d(128),
                                nn.MaxPool1d(kernel_size=2, stride=0, padding=0)
                                )
        
        self.A3 = nn.Sequential(# 3 ================
                                nn.Conv1d(128, 128, 64, stride = 1,dilation = 1, padding=32),
                                nn.ReLU(),
                                nn.BatchNorm1d(128),
                                nn.MaxPool1d(kernel_size=2, stride=0, padding=0)
                                )
                                
        self.A4 = nn.Sequential(# 4 ================
                                nn.Conv1d(128, 128, 64, stride = 1,dilation = 1, padding=32),
                                nn.ReLU(),
                                nn.BatchNorm1d(128),
                                nn.MaxPool1d(kernel_size=2, stride=0, padding=0)
                                )
                                
        self.A5 = nn.Sequential(# 5 ================
                                nn.Conv1d(128, 256, 64, stride = 1,dilation = 1, padding=32),
                                nn.ReLU(),
                                nn.BatchNorm1d(256),
                                nn.MaxPool1d(kernel_size=2, stride=0, padding=0)
                                )
                                
        self.A6 = nn.Sequential(# 6 ================
                                nn.Conv1d(256, 512, 64, stride = 1,dilation = 1, padding=32),
                                nn.ReLU(),
                                nn.BatchNorm1d(512),
                                nn.MaxPool1d(kernel_size=2, stride=0, padding=0)
                                )
        
        self.fc0 = nn.Linear(2048, 128)

        #self.sgm = nn.functional.sigmoid()

    def forward(self, seq):
        
        seq = self.A1(seq)
        print( seq.shape )

        seq = self.A2(seq)
        print( seq.shape )
        
        seq = self.A3(seq)
        print( seq.shape )
        
        seq = self.A4(seq)
        print( seq.shape )
        
        seq = self.A5(seq)
        print( seq.shape )
        
        seq = self.A6(seq)
        print( seq.shape )

        seq = seq.view(-1,2048)
        
        seq = self.fc0(seq)
        
        seq = F.sigmoid(seq)

        return seq