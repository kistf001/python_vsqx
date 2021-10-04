import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable

import numpy as np

from customDatasetBreath import my_trainset, my_testset
from customModelBreath import breathDetectNet

import timeit
from time_stemp import timeStemp

from nameUtility import fileNameSpliter

import os

class looper:

    def __init__(self):

        self.standard_start = timeit.default_timer()
        self.timeout_start = timeit.default_timer()
        self.model_save_direction = "H:/"
        self.trainset_directory = "H:/Dataset"

    def name_maker(self):
        name = timeStemp() + "_breath" + ".pth"
        return name

    def model_make_and_save(self):

        # 모델을 선언
        model = breathDetectNet()

        # 모델 네임
        name = self.name_maker()
        directory = self.model_save_direction + name

        # 임시 이름을 사용하여 모델을 저장
        temporary_name = self.model_save_direction + "temp.pth"
        torch.save( model.state_dict(), directory )

        # 다시 본래 이름으로 만듬
        os.rename(temporary_name, directory)

    def model_save_and_sending_when_timeout(self, model, timeout = 13):
        
        self.timeout_end = timeit.default_timer()

        # 지정된 시간이 넘어가면 모델을 저장하고 ftp로 전송함
        if ( (self.timeout_end - self.timeout_start) > timeout ):
            model_cpu = model.cuda()

            # 모델 네임
            name = name = self.name_maker()
            directory = self.model_save_direction + name

            # 임시 이름을 사용하여 모델을 저장
            temporary_name = self.model_save_direction + "temp.pth"
            torch.save( model_cpu.state_dict(), temporary_name )
            
            # 다시 본래 이름으로 만듬
            os.rename(temporary_name, directory)

            # 시작시간을 초기화함
            self.timeout_start = timeit.default_timer()

            return 1

        return 0

    def start(self):

        ##############################################
        # dataset
        ##############################################

        trainset = my_trainset(directory = self.trainset_directory)

        trainset_loader = torch.utils.data.DataLoader(dataset=trainset,
                                                      batch_size=1,
                                                      shuffle=False)

        ##############################################
        # loss select
        ##############################################

        # loss selecter
        #loss_function = nn.BCEWithLogitsLoss()
        #loss_function = nn.SmoothL1Loss()
        loss_function = nn.BCELoss()
        #loss_function = nn.MSELoss()
        #loss_function = nn.MultiLabelSoftMarginLoss()

        ##############################################
        # model import
        ##############################################

        name_list = fileNameSpliter().pth_breath.scan(self.model_save_direction)
        name = self.model_save_direction + name_list[-1] + ".pth"

        device = torch.device('cpu')

        model = breathDetectNet()
        model.load_state_dict(torch.load(name, map_location=device))

        ##############################################
        # optimizer setting
        ##############################################

        optim = torch.optim.SGD(model.parameters(), lr = 0.001, momentum = 0.9)

        ##############################################
        # cuda cheack
        ##############################################

        if True and torch.cuda.is_available():
            model.cuda()
            print("can cuda")
        else:
            print("can't cuda")

        ##############################################
        # learning loop
        ##############################################

        for ii in range(0,1000):

            for i, data in enumerate(trainset_loader):

                _sig, _label = data

                #optim.zero_grad()

                output = model(_sig)

                #loss = loss_function(output, _label)

                #loss.backward()

                #optim.step()

                #if((i%10)==0):
#
                #    print( "data :", _sig  )
                #    print( "label :", _label )
                #    print( "output :", output )
                #    print( "loss :", loss )
                #    print("i :", i, "ii :", ii)
#
                #    state = self.model_save_and_sending_when_timeout(model)
#
                #    print(state)

looper().start()
#looper().model_make_and_save()