# ddb-extraction

(Attempt to) Extract the samples of a DDB Vocaloid file. Help would be appreciated!

[GBATemp Thread](https://gbatemp.net/threads/i-found-out-the-format-of-samples-in-vocaloid-2-3-and-4-voicebanks-now-what.400402/)

[Discord Server](https://discord.gg/FzB49rq)

## Usage:

I suggest you just copy the DDB file to the folder with this python file. It makes everything easier.

1. ``python extract.py [location of DDB file]``
Extracts all the raw files from the DDB file. (This is probably the wrong way to do it because it is missing a lot of data with white noise being skipped)

2. ``python raw-to-wav [folder name with raw files] [0 or 1]``
This puts the raw files into WAV format.
