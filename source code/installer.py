# download https://github.com/Hamy-os/computer-outro/raw/main/outro.mp3 and save it to the desktop

import requests
import os

outroURL = "https://github.com/Hamy-os/computer-outro/raw/main/outro.mp3"
choice1URL = "https://github.com/Hamy-os/computer-outro/raw/main/fakebsod.exe"
choice2URL = "https://github.com/Hamy-os/computer-outro/raw/main/bsod.exe"
choice3URL = "https://github.com/Hamy-os/computer-outro/raw/main/shutdown.exe"

print("Downloading the outro.mp3 file...")
response = requests.get(outroURL)
open("outro.mp3", "wb").write(response.content)
print("Download complete.")

print("Please pick one.")
choice = input(
    "There are 3 options. \n Option 1: Fake bsod (fakebsod.exe) \n Option 2: Real bsod (bsod.exe) \n Option 3: Shutdown (shutdown.exe)"
)

if choice == "1":
    print("Downloading Fake bsod")
    # responsee = requests.get(choice1URL)
    # open("fakebsod.exe", "wb").write(responsee.content)
    response = requests.get(
        "https://raw.githubusercontent.com/Hamy-os/computer-outro/fake-bsod/bsod.bat"
    )
    open("bsod.bat", "wb").write(response.content)
    print("Success! Starting the fake bsod...")
    os.system("start fakebsod.exe")

elif choice == "2":
    print("Downloading Real bsod")
    response = requests.get(choice2URL)
    open("bsod.exe", "wb").write(response.content)
    print("Success! Starting the bsod.exe file...")
    os.system("start bsod.exe")

elif choice == "3":
    print("Downloading Shutdown")
    response = requests.get(choice3URL)
    open("shutdown.exe1", "wb").write(response.content)
    print("Success! Starting shutdown.exe")
    os.system("start shutdown.exe")
