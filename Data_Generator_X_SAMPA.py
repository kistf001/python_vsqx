# korean

class korean:

    def __init__(self):

        self.onset = list()
        self.onset.append(" n   ")
        self.onset.append(" g   ")
        self.onset.append(" d   ")
        self.onset.append(" r   ")
        self.onset.append(" l   ")
        self.onset.append(" m   ")
        self.onset.append(" b   ")
        self.onset.append(" s   ")
        self.onset.append(" sh  ")
        self.onset.append(" N   ")
        self.onset.append(" c   ")
        self.onset.append(" ch  ")
        self.onset.append(" k   ")
        self.onset.append(" t   ")
        self.onset.append(" p   ")
        self.onset.append(" h   ")
        self.onset.append(" g'  ")
        self.onset.append(" d'  ")
        self.onset.append(" b'  ")
        self.onset.append(" s'  ")
        self.onset.append(" sh' ")
        self.onset.append(" c'  ")

        self.nucleus = list()
        self.nucleus.append(" a  ")
        self.nucleus.append(" ja ") 
        self.nucleus.append(" j7 ") 
        self.nucleus.append(" o  ")
        self.nucleus.append(" jo ") 
        self.nucleus.append(" u  ")
        self.nucleus.append(" ju ") 
        self.nucleus.append(" M  ")
        self.nucleus.append(" i  ")
        self.nucleus.append(" e  ")
        self.nucleus.append(" je ") 
        self.nucleus.append(" oa ") 
        self.nucleus.append(" u7 ") 
        self.nucleus.append(" ue ") 
        self.nucleus.append(" ui ") 
        self.nucleus.append(" Mi ")

        self.coda = list()
        self.coda.append(" gp ")
        self.coda.append(" np ")
        self.coda.append(" dp ")
        self.coda.append(" rp ")
        self.coda.append(" mp ")
        self.coda.append(" bp ")
        self.coda.append(" Np ")

 # 2019-09-20 21:06:25 (보기 | RAW | Blame | 이 리비젼으로 되돌리기 | 비교)   r65 (-8) afv305 ()
 # 나무위키 위 버전을 기준으로 함

class japanese:

    def __init__(self):

        self.clear = list()
        self.clear.append("k")     # N
        self.clear.append("k'")     # N'
        self.clear.append("s")     # N\\
        self.clear.append("S")     # N\\
        self.clear.append("t")     # n
        self.clear.append("t'")     #*n
        self.clear.append("tS")     # n
        self.clear.append("ts")     # n
        self.clear.append("n")     # n
        self.clear.append("J")     # J
        self.clear.append("h")     # N\\
        self.clear.append("h\\")     # N\\
        self.clear.append("C")
        self.clear.append("p\\")     # N\\
        self.clear.append("p\\'")     # N\\
        self.clear.append("m")     # m
        self.clear.append("m'")     # m'
        self.clear.append("j")     # N\\
        self.clear.append("4")     # n
        self.clear.append("4'")     # n
        self.clear.append("w")     # N\\

        self.nn = list()
        self.nn.append("n")
        self.nn.append("J")
        self.nn.append("m")
        self.nn.append("m'")
        self.nn.append("N")
        self.nn.append("N'")
        self.nn.append("N\\")

        self.dirty = list()
        self.dirty.append("g")     # N
        self.dirty.append("g'")     # N'
        self.dirty.append("dz")     # n
        self.dirty.append("z")     # n
        self.dirty.append("dZ")     # n
        self.dirty.append("Z")     # n
        self.dirty.append("d")     # n
        self.dirty.append("d'")     # n
        self.dirty.append("b")     # m
        self.dirty.append("b'")     # m'
        self.dirty.append("p")     # m
        self.dirty.append("p'")     # m'

        self.chock = list()
        self.chock.append("Sil")

        self.mother = list()
        self.mother.append("a")
        self.mother.append("i")
        self.mother.append("M")
        self.mother.append("e")
        self.mother.append("o")

class japanese_list:

    def __init__(self):

        self.m = list()
        self.m_n = list()

        self.c_m = list()
        self.c_m_n = list()
        
        self.d_m = list()
        self.d_m_n = list()
        
        self.all = list()

        for _mother in japanese().mother:
            self.m.append(_mother)
        for _mother in japanese().mother:
            for _nn in japanese().nn:
                self.m_n.append( _mother + " " + _nn )

        for _mother in japanese().mother:
            for _clear in japanese().clear:
                self.c_m.append( _clear + " " + _mother )
        for _mother in japanese().mother:
            for _clear in japanese().clear:
                for _nn in japanese().nn:
                    self.c_m_n.append( _clear + " " + _mother + " " + _nn )

        for _mother in japanese().mother:
            for _dirty in japanese().dirty:
                self.d_m.append( _dirty + " " + _mother )
        for _mother in japanese().mother:
            for _dirty in japanese().dirty:
                for _nn in japanese().nn:
                    self.d_m_n.append( _dirty + " " + _mother + " " + _nn )
                    
        for _m in self.m:
            self.all.append(_m)
        for _m_n in self.m_n:
            self.all.append(_m_n)

        for _c_m in self.c_m:
            self.all.append(_c_m)
        for _c_m_n in self.c_m_n:
            self.all.append(_c_m_n)

        for _d_m in self.d_m:
            self.all.append(_d_m)
        for _d_m_n in self.d_m_n:
            self.all.append(_d_m_n)

class dd:

    def asd(self):

        self.bright_a = [
            
            "k",  "k'", "s", "S",  "t",   "tS",
            "n",  "J",  "h", "C",  "p\\", "m",
            "m'", "j",  "4", "4'", "w",
            
            "g", "g'", "dz", "dZ", "d",
            "b", "b'", "p",  "p'"
            
        ]

        self.bright_i = [
            
            "k'", "S", "t'", "tS", "ts",
            "J",  "C",
            "m'", "4'", "w",
            
            "g'", "dZ", "dz", "d'",
            "b'", "p'"

        ]

        self.bright_M = [
            
            "k",  "k'", "s", "S",   "t",    "t'", "tS", "ts",
            "n",  "J",  "C", "p\\", "p\\'", "m",
            "m'", "j",  "4", "4'",
            
            "g", "g'", "dz", "z", "dZ", "Z", "d", "d'",
            "b", "b'", "p", "p'"
            
        ]

        self.bright_e = [
            
            "k", "s",  "S", "t",   "ts", "tS",
            "n", "J" , "h", "h\\", "C",  "p\\", 
            "m", "m'", "j", "4",   "w",
            
            "g",       "dz", "z", "dZ", "Z", 
            "d", "b" , "b'", "p", "p'"
             
        ]

        self.bright_o = [
            
            "k", "k'", "s", "S", "t", "tS", "ts",
            "n", "J",  "h", "C", "p\\",
            "m", "m'", "j", "4", "4'", "w",
            
            "g", "g'", "dz", "z","dZ", "Z",
            "d", "d'", "b", "b'", "p", "p'"
            
        ]

        self.aiMeo = [

            "a", "i", "M", "e", "o"
        
        ]

        self.nJmmNNN = {

            "n", "J", "m", "m'", "N", "N'", "N\\"

        }

    def __init__(self):
        
        self.asd()

        self.data = []

        for a in self.bright_a:
            self.data.append(a + " " + self.aiMeo[0])
        for a in self.bright_i:
            self.data.append(a + " " + self.aiMeo[1])
        for a in self.bright_M:
            self.data.append(a + " " + self.aiMeo[2])
        for a in self.bright_e:
            self.data.append(a + " " + self.aiMeo[3])
        for a in self.bright_o:
            self.data.append(a + " " + self.aiMeo[4])

        asas = []

        for s in self.data:
            asas.append(s + " " + "n")
        for s in self.data:
            asas.append(s + " " + "m")
        for s in self.data:
            asas.append(s + " " + "N\\")
        for s in self.data:
            asas.append(s + " " + "g")
        for s in self.data:
            asas.append(s + " " + "k")
        for s in self.data:
            asas.append(s + " " + "d")
        for s in self.data:
            asas.append(s + " " + "t")
        for s in self.data:
            asas.append(s + " " + "b")
        for s in self.data:
            asas.append(s + " " + "p")
        
        self.data = asas