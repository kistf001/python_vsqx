import VOCALO_XML_type as vsqxT

class track_Append:

    def track_zero_cheack(self):

        vsTrack_set = self.data[5]
        vsTrack_set_len = len(vsTrack_set)

        mixer = self.data[3]
        vsUnit_set = mixer[1]
        vsUnit_set_len = len(vsUnit_set)

    def add_vsTrack(self):
        empty_vsTrack = vsqxT.vsTrack().vsTrack()
        vsTrack = self.data[5]
        vsTrack.append(empty_vsTrack)

    def add_vsUnit(self):
        empty_vsUnit = vsqxT.mixer().vsUnit()
        vsUnit = self.data[3][1]
        vsUnit.append(empty_vsUnit)

    def vsTrack_tNo_renumbering(self):
        tNo_number = 0
        vsTrack = self.data[5]
        for _vsTrack in vsTrack:
            _vsTrack[0] = tNo_number
            tNo_number = tNo_number + 1

    def mixer_tNo_renumbering(self):
        tNo_number = 0
        mixer = self.data[3]
        vsUnit_set = mixer[1]
        for vsUnit in vsUnit_set:
            vsUnit[0] = tNo_number
            tNo_number = tNo_number + 1

    def __init__(self, _data):
        self.data = _data
        self.add_vsTrack()
        self.add_vsUnit()
        self.vsTrack_tNo_renumbering()
        self.mixer_tNo_renumbering()

class track_delite:

    def del_vsTrack(self):
        vsTrack = self.data[5]
        del vsTrack[self.position]

    def del_mixer(self):
        mixer = self.data[3][1]
        del mixer[self.position]

    def vsTrack_tNo_renumbering(self):
        tNo_number = 0
        vsTrack = self.data[5]
        for _vsTrack in vsTrack:
            _vsTrack[0] = tNo_number
            tNo_number = tNo_number + 1

    def mixer_tNo_renumbering(self):
        tNo_number = 0
        mixer = self.data[3]
        vsUnit_set = mixer[1]
        for vsUnit in vsUnit_set:
            vsUnit[0] = tNo_number
            tNo_number = tNo_number + 1

    def __init__(self, _data, number):
        self.data = _data
        self.position = number
        self.del_vsTrack()
        self.del_mixer()
        self.vsTrack_tNo_renumbering()
        self.mixer_tNo_renumbering()
    
class empty_vsqx:

    def variable_init(self):

        self.number_of_track = 0

    def empty_vsqx(self):
        return vsqxT.empty_vsqx().data

    def write_basic_data_vsqx(self, vsqx):
        
        vsqx[0] = vsqxT.vender().vender()
        vsqx[1] = vsqxT.version().version()
        vsqx[2] = vsqxT.vVoiceTable().vVoiceTable()
        vsqx[3] = vsqxT.mixer().mixer()
        vsqx[4] = vsqxT.masterTrack().masterTrack()
        vsqx[5] = vsqxT.vsTrack().vsTrack_set()
        vsqx[6] = vsqxT.monoTrack().monoTrack()
        vsqx[7] = vsqxT.stTrack().stTrack()
        vsqx[8] = vsqxT.aux().aux()

        return 0
    
    def start(self):
        self.variable_init()
        vsqx = self.empty_vsqx()
        self.write_basic_data_vsqx(vsqx)
        self.data = vsqx
        return self.data

class add_note:

    def check_track_number(self):
        selected_track_number = self.stN
        number_of_tracks = len(self.vsqx[5])
        if(number_of_tracks<selected_track_number):
            a = 0

    def select_track(self):
        selected_track_number = self.stN
        self.vsTrack = self.vsqx[5][selected_track_number]

    def select_vsPart(self):
        self.vsPart = self.vsTrack[3][0]
    
    #def chack_number_of_note(self):

    def __init__(self, _data, 
    selected_track_number, start_time, front_time = 0, end_time = 0, length_time = 0):

        self.vsqx = _data
        self.stN = selected_track_number
        self.sT = start_time
        self.fT = front_time
        self.eT = end_time

        self.check_track_number()
        self.select_track()
        self.select_vsPart()