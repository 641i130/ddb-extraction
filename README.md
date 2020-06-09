# ddb-extraction
Extract the samples of a DDB Vocaloid file.

## Usage:

I suggest you just copy the DDB file to the folder with this python file. It makes everything easier.

1. ``python extract.py [location of DDB file]``
Extracts all the raw files from the DDB file. (This is probably the wrong way to do it because it is missing a lot of data with white noise being skipped)

2. ``python raw-to-wav [folder name with raw files] [0 or 1]``
This puts the raw files into WAV format.
