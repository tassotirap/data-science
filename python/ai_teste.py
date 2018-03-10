import torch

import csv

from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F

class NNTest(nn.Module):
    def __init__(self, input_size, output_size):
        super(NNTest, self).__init__()
        self.fc1 = nn.Linear(input_size, 50)
        self.fc2 = nn.Linear(50, 100)
        self.fc3 = nn.Linear(100, 50)
        self.fc4 = nn.Linear(50, output_size)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = self.fc4(x)
        return x

net = NNTest(6, 1).cuda()
    
# Loss and Optimizer
# criterion = nn.CrossEntropyLoss()  
optimizer = torch.optim.Adam(net.parameters(), lr = 0.001)  

for epoch in range(1500):
    with open('data.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        next(reader, None)
        for row in reader:
            in1 = float(row[0])
            in2 = float(row[1])
            in3 = float(row[2])
            in4 = float(row[3])
            in5 = float(row[4])
            in6 = float(row[5])

            out = float(row[6])

            input = torch.FloatTensor([in1, in2, in3, in4, in5, in6]).unsqueeze(0)
            input = Variable(input.cuda())

            realOutput = torch.FloatTensor([out])
            realOutput = Variable(realOutput.cuda())
            
            optimizer.zero_grad()  # zero the gradient buffer
            outputs = net(input)

            loss = F.smooth_l1_loss(outputs, realOutput)
            
            loss.backward()
            optimizer.step()

    print("Fim do Treino: %d" % epoch)

erros = 0

print("Fim do Treino")

with open('data.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    next(reader, None)
    for row in reader:
        in1 = float(row[0])
        in2 = float(row[1])
        in3 = float(row[2])
        in4 = float(row[3])
        in5 = float(row[4])
        in6 = float(row[5])

        out = float(row[6])

        input = torch.FloatTensor([in1, in2, in3, in4, in5, in6]).unsqueeze(0)
        input = Variable(input.cuda())

        realOutput = torch.FloatTensor([out])
        realOutput = Variable(realOutput.cuda())
        outputs = net(input)

        if abs(out - outputs.data[0][0]) > 0.1:
            erros = erros + 1

print(erros)