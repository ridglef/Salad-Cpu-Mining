import subprocess
from pymem import Pymem

IsXmrigRunning = False
IsVmmemRunning = False
PathToXmrig = "path/to/your/xmrig.exe"

while True:
    while (True):

        try:

            pm = Pymem('vmmem.exe')
            IsVmmemRunning = True
            try:

                if IsXmrigRunning:
                    pm = Pymem('xmrig.exe')
                    pm.close_process()
                    IsXmrigRunning = False
                    print("Vmmem Running! Closing XMRIG")

            except:
                print("Failed to close XMRIG")

        except:

            if IsXmrigRunning != True:
                subprocess.call(PathToXmrig, shell=True)
                print("Started Xmrig!")
