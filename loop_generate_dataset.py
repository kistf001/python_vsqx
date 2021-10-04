from Data_Generator import generator
import pandas as pd
from nameUtility import fileNameSpliter
from VOCALO_XML_type import vsqx

directory = "H:/C"

for a in range(0, 1):

    generator(directory)
    print(a)

name_list = fileNameSpliter().h5.scan(directory)

# table make
aaa = "C:/Users/Miku/Desktop/Coding2019/201905281407-python-VocaloidMaster"
A = pd.read_csv( aaa + '/vocaloidSingerManagement/VocaloidDatabaseName.csv' )

def voiceTableMaker( pandasFile, data_length ):

    pandasFile_size = len(pandasFile)

    voice_table = []
    voice_table_counter = 0

    while(1):
        
        # select only JAPAN 
        if(pandasFile["lang"][voice_table_counter] == "J"):
            voice_table.append(pandasFile["productNumber"][voice_table_counter])

            if( len(voice_table) >= data_length ):
                break
        
        # count +1
        voice_table_counter += 1

        # if over
        if( pandasFile_size <= voice_table_counter ):
            voice_table_counter = 0

    return voice_table

voice_table = voiceTableMaker( A, len(name_list)+10 )
voice_table_counter = 0

# main
for ase in name_list:

    _pd_note_dir = directory + '/' + ase + '.note.h5'
    _pd_cc_dir = directory + '/' + ase + '.cc.h5'

    asasdsd = vsqx()
    asasdsd.addTrack( _pd_cc_dir, _pd_note_dir, voice_table[voice_table_counter] )
    asasdsd.to_vsqx4( directory + '/' + ase )

    voice_table_counter += 1

    print(ase)
