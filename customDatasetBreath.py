import torch
import scipy.io.wavfile as wav
import numpy as np
import pandas as pd

import nameUtility as nu

class my_trainset(torch.utils.data.Dataset):

    def dataMaker(self, directory = ""):
    
        wave_file_name_list = nu.fileNameSpliter().wav48k.scan(directory)
        bunched = np.array([])

        wave_file_name_list = sorted(wave_file_name_list)

        for wave_file_name in wave_file_name_list:
            
            file_directory = directory + "/" + wave_file_name + ".wav"
            sample_rate, wave_data = wav.read( file_directory )
            bunched = np.r_[ bunched, wave_data[38400*4:] ]
            
        return np.array( bunched + 32768, dtype = np.float32 )

    def labelMaker(self, directory = ""):

        h5_file_name_list = nu.fileNameSpliter().h5.scan(directory)
        bunched = np.array([])

        h5_file_name_list = sorted(h5_file_name_list)
        
        for h5_file_name in h5_file_name_list:

            file_directory = directory + "/" + h5_file_name + ".cc" + ".h5"
            pandas_cc_data = pd.read_hdf(file_directory,'df')["breath"].to_numpy()
            bunched = np.r_[bunched, pandas_cc_data]

        return np.array( bunched, dtype = np.uint8 )

    def __init__( self, transform = None, directory = ""):
        
        self.data = self.dataMaker(directory)
        self.label = self.labelMaker(directory)

        self.data_length = len(self.data)
        self.label_length = len(self.label)

        print(self.data_length)
        print(self.label_length)

    def __getitem__(self, index):

        index = index + 1000
        
        # get data position index
        start_position_data = index 
        end_position_data = ( index + 1024 )

        # get label position index
        start_position_label = int( start_position_data / 20 )
        end_position_label = int( end_position_data / 20 )

        # choose data
        ouput_data = np.array([self.data[start_position_data:end_position_data]])
        output_label = self.label[start_position_label:end_position_label][-5]

        # translate one hot encoding
        output_label = np.array( np.eye(128)[output_label], dtype = np.float32 )

        return ouput_data, output_label

    def __len__(self):
    
        return ( self.data_length ) - 4000

class my_testset(torch.utils.data.Dataset):

    def dataMaker(self, directory = ""):
    
        wave_file_name_list = nu.fileNameSpliter().wav48k.scan(directory)
        bunched = np.array([])

        wave_file_name_list = sorted(wave_file_name_list)

        for wave_file_name in wave_file_name_list:
            
            file_directory = directory + "/" + wave_file_name + ".wav"
            sample_rate, wave_data = wav.read( file_directory )
            bunched = np.r_[bunched, wave_data ]

        return np.array( bunched, dtype = np.float32 )

    def labelMaker(self, directory = ""):

        h5_file_name_list = nu.fileNameSpliter().h5.scan(directory)
        bunched = np.array([])

        h5_file_name_list = sorted(h5_file_name_list)
        
        for h5_file_name in h5_file_name_list:

            file_directory = directory + "/" + h5_file_name + ".cc" + ".h5"
            pandas_cc_data = pd.read_hdf(file_directory,'df')["breath"].to_numpy()
            bunched = np.r_[bunched, pandas_cc_data]

        return np.array( bunched, dtype = np.uint8 )

    def __init__( self, transform = None, directory = ""):
        
        self.data = self.dataMaker(directory)
        self.label = self.labelMaker(directory)

    def __getitem__(self, index):

        index = index + 1000
        
        # get data position index
        start_position_data = index 
        end_position_data = ( index + 1024 )

        # get label position index
        start_position_label = int( index / 6.6666 )
        end_position_label = int( ( index + 1024 ) / 6.6666 )
    
        # choose data
        ouput_data = np.array([self.data[start_position_data:end_position_data]])
        output_label = self.label[start_position_label:end_position_label][-10]

        # translate one hot encoding
        output_label = np.array( np.eye(128)[output_label], dtype = np.float32 )

        return ouput_data, output_label

    def __len__(self):
    
        return ( 10240000 * 11 ) - 4000
        
