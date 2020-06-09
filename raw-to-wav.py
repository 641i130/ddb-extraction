# RAW to WAV
# Written by 641i130
import sys, wave, os
# Set range of all raw files to put into a wav file or files
x,y = 1,5859 # 5859

# Make samples folder if non-exsistant
if not os.path.exists("samples"):
    os.makedirs("samples")

try:
    fold = sys.argv[1]
except:
    print("Please use:\npython raw-to-wav.py [folder name with raw files] [0 or 1]\n\nThis should be the name of the ddb file without the extension.\n0 as in seperate sample files.\n1 as in one large sample file.")

for i in range(x,y+1):
    fi = "{}/s{}".format(fold,str(i))
    print("Making s{}.wav".format(str(i)),end="\r")
    if i == y:
        print("Processed s{}.wav".format(str(i)))
    # Opens raw data from DDB file extraction
    with open(fi, "rb") as pcmfile:
        pcmdata = pcmfile.read()
    # Writes raw data to a WAV for use later
    wa = "samples/s{}.wav".format(str(i))
    with wave.open(wa, "wb") as wavfile:
        wavfile.setparams((1, 2, 44100, 0, 'NONE', 'NONE'))
        wavfile.writeframes(pcmdata)
        
if sys.argv[2] == 1:
    # Combines all WAV files
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
