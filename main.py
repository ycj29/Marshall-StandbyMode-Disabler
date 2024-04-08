from playsound import playsound
from time import sleep
print('This script plays an empty sound every 500 seconds!')
option = input("Pick a mode, (1) Empty Audio, (2) 20Hz Audio")
sound = "empty.mp3"
if option == "2":
    sound = "20hz.mp3"
print('Selected: ' + sound)
while True:
    print("Play")
    playsound(sound)
    print('Stop')
    sleep(500)
