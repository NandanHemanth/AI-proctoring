#Importing libraries
import sounddevice as sd
import numpy as np

# place holders and global variables 
SOUND_AMPLITUDE = 0
AUDIO_CHEAT = 0

# SOUND variables which determine the cheating curve
CALLBACKS_PER_SECOND = 38       # callbacks per sec(16kHz sampling rate) - System dependent
SUS_FREQUENCY = 2               # cals SUS * n times every sec
SOUND_AMPLITUDE_THRESHOLD = 20  # amplitude considered for SUS calc

# packing *n frames to calc SUS
FRAMES_COUNT = int(CALLBACKS_PER_SECOND/SUS_FREQUENCY)
AMPLITUDE_LIST = list([0]*FRAMES_COUNT)
SUS_COUNT = 0
count = 0

# Function to check if audio is more than threshold
def print_sound(indata, outdata, frames, time, status):
    avg_amp = 0
    global SOUNDA_AMPLITUDE, SUS_COUNT, count, SOUND_AMPLITUDE_THRESHOLD, AUDIO_CHEAT
    vnorm = int(np.linalg.norm(indata)*10)
    AMPLITUDE_LIST.append(vnorm)
    count += 1
    AMPLITUDE_LIST.pop(0)
    if count == FRAMES_COUNT:
        avg_amp = sum(AMPLITUDE_LIST)/FRAMES_COUNT
        SOUND_AMPLITUDE = avg_amp
        if SUS_COUNT >= 2:
            #print("!!!!!!!!!!!! FBI OPEN UP !!!!!!!!!!!!")
            AUDIO_CHEAT = 1
            SUS_COUNT = 0
        if avg_amp > SOUND_AMPLITUDE_THRESHOLD:
            SUS_COUNT += 1
            #print("Sus...", SUS_COUNT)
        else:
            SUS_COUNT = 0
            AUDIO_CHEAT = 0
        count = 0

# streaming audio
def sound():
    with sd.Stream(callback=print_sound):
        sd.sleep(-1)

# Analysing the sound
def sound_analysis():
    global AMPLITUDE_LIST, FRAMES_COUNT, SOUND_AMPLITUDE
    while True:
        AMPLITUDE_LIST.append(SOUND_AMPLITUDE)
        AMPLITUDE_LIST.pop(0)

        avg_amp = sum(AMPLITUDE_LIST)/FRAMES_COUNT

        if avg_amp > 10:
            print("Sus...")

# Main Function
if __name__ == '__main__':
    sound()


