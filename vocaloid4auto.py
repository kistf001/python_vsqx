from pywinauto.application import Application, findwindows
import pywinauto
import time

#fileName = "H:\\Dataset\\20191210_223335.vsqx"
#fileNameWave = "H:\\Dataset\\20191210_223335"

#"C:/Program Files (x86)/Vocaloid4FE/VOCALOID4.exe"

class ss:

    def init_pywinauto(self, vocaloid_directory = ""):

        # Start VOCALOID 4
        self.app = Application(backend="uia").start(vocaloid_directory, retry_interval=6)

        # Wait 10 Second
        time.sleep(10)

        self.vsqx = self.app.Dialog

        self.vsqx.set_focus()
        self.vsqx.maximize()

    def open_vsqx(self, fileName):

        pywinauto.keyboard.send_keys("%{F},{O}")

        vsqx_open = self.vsqx.child_window(title="열기", control_type="Window")
        vsqx_open_ComboBox = vsqx_open.child_window(title="파일 이름(N):", auto_id="1148", control_type="ComboBox")
        vsqx_open_ComboBox.Edit.set_text(fileName)

        vsqx_open_button = vsqx_open.child_window(title="열기(O)", auto_id="1", control_type="Button")
        vsqx_open_button.click()
        
        # Wait 7 Second
        time.sleep(7)

    def convert_wave(self, fileNameWave):

        pywinauto.keyboard.send_keys("%{F},{E},{W}")

        vsqx_exportWaveFile = self.vsqx.child_window(title="Export Wave File", control_type="Window")
        vsqx_exportWaveFile_samplingRate = vsqx_exportWaveFile.child_window(title="Sampling Rate(S)", auto_id="1405", control_type="ComboBox")
        vsqx_exportWaveFile_samplingRate.select("48000")
        vsqx_exportWaveFile_OK = vsqx_exportWaveFile.child_window(title="OK", auto_id="1", control_type="Button")
        vsqx_exportWaveFile_OK.click()

        vsqx_findFolder = self.vsqx.child_window(title="폴더 찾아보기", control_type="Window")
        vsqx_findFolder_edit = vsqx_findFolder.child_window(title="폴더(F):", auto_id="14148", control_type="Edit")
        vsqx_findFolder_edit.set_text(fileNameWave)
        vsqx_findFolder_button = vsqx_findFolder.child_window(title="확인", auto_id="1", control_type="Button")
        vsqx_findFolder_button.click()
        
        # Wait 3 Second
        time.sleep(3)

    def kill_program(self):

        self.app.Dialog.print_control_identifiers()
        
        self.vsqx.set_focus()
        
        pywinauto.keyboard.send_keys("%{F},{X}")