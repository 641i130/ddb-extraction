# Takes DDB file and extracts/splits all the raw data for WAV conversion
"""
BASED OFF OF mrsky's code from 
https://gbatemp.net/threads/i-found-out-the-format-of-samples-in-vocaloid-2-3-and-4-voicebanks-now-what.400402/
"""
import sys
import os
# File location / name
try:
    f = sys.argv[1]
except:
    print("Please use:\npython extract.py [location of ddb file]")

# Make folder for samples
path = os.getcwd()
folder = "{}/{}/".format(path,f[:-4])
print(folder)

if not os.path.exists(folder):
    os.makedirs(folder)

with open(f,"rb") as yee:
    array = yee.read()
    # Print size of DDB file.
    print(str(len(array)))

sp = -1
ep = -1
sn = 0
counter=0
# Interate through file and do things with data.
for i in range(len(array)+1):
    # If the current byte = S and following bytes are N and D, set byte after SND to start position
    if array[i] == 83 and array[i+1] == 78 and array[i+2] == 68 and sp == -1:
        sp = i
        print("Found beginning of sample!")
        counter+=1
    #Same thing but with FRM2h,
    if (array[i] == 70 and array[i +1] == 82 and array[i + 2] == 77 and array[i + 3] == 50 and sp != -1):
        ep = i - 1
        print("Found end of sample")
    
    if sp != -1 and ep != -1:
        # Write to file!!!
        sn += 1
        print("Writing sample: {}".format(str(sn)))
        # open file
        fn = "s{}".format(str(sn))
        with open("{}/{}".format(folder,fn),"wb") as samp:
            # File is still raw btw
            samp.write(array[sp:ep])
        # write bytes in given range
        # close file
        sp,ep = -1,-1


print("Total of {} samples.".format(str(counter)))