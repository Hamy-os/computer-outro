
# Packages necessary to run
import time
import subprocess
import os
from pygame import mixer
# Find and play sound (if in the same folder as this file)
outrosound = os.path.join(os.getcwd(), 'outro.mp3')
mixer.init()
mixer.music.load(outrosound)
mixer.music.play()

time.sleep(0.1)
for zaky in range(10):
    print("Shutting down in: " + str(10 - zaky) + " Seconds")
    time.sleep(1)


print("Shutting down now!")
time.sleep(1.25)

bat_file_path = str(f"{os.path.dirname(__file__)}/bsod.bat")
subprocess.call([bat_file_path])
