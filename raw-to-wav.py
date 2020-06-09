# RAW to WAV
# Written by 641i130
import sys, wave, os
# Set range of all raw files to put into a wav file or files
x,y = 1,5859 # 5859

fold = SOMETHING # This is the name of the DDB file without the extension 

for i in range(x,y+1):
    fi = "{}/s{}".format(fold,str(i))
    print("Making s{}.wav".format(str(i)),end="\r")
    if i == y:
        print("Processed s{}.wav".format(str(i)))
    # Opens raw data from DDB file extraction
    with open(fi, "rb") as pcmfile:
        pcmdata = pcmfile.read()
    # Writes raw data to a WAV for use later
    with wave.open(fi+".wav", "wb") as wavfile:
        wavfile.setparams((1, 2, 44100, 0, 'NONE', 'NONE'))
        wavfile.writeframes(pcmdata)
        
# Comment out the bottom part if you don't want the files as one
with wave.open("yee.wav", "wb") as out:
    # Set WAV parameters
    out.setparams((1, 2, 44100, 0, 'NONE', 'NONE'))
    for i in range(x,y+1):
        # For each wav file made above, combine it into one wav file then delete
        fi = "{}/s{}".format(fold,str(i))
        with wave.open(fi, "rb") as w:
            out.writeframes(w.readframes(w.getnframes()))
        os.remove(fi)

print("\nConverted {} files total.".format(str((y+1)-x)))