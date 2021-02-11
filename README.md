# ddb-extraction

(Attempt to) Extract the samples of a DDB Vocaloid file. Help would be appreciated!

[GBATemp Thread](https://gbatemp.net/threads/i-found-out-the-format-of-samples-in-vocaloid-2-3-and-4-voicebanks-now-what.400402/)

[Discord Server](https://discord.gg/FzB49rq)

## Usage:

```
extract.py [-h] [--src-path SRC_PATH] [--dst-path DST_PATH] [--merge]

optional arguments:
  -h, --help           show this help message and exit
  --src-path SRC_PATH  source ddb file path
  --dst-path DST_PATH  destination extract path, default="./extract/"
  --merge              enable to generate a merged large wav file
```