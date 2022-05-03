# ddb-extraction

# Check out this modified version by [ain-soph](https://github.com/ain-soph)
[github.com/ain-soph](https://github.com/ain-soph/ddb-extraction)
They got the ddi extraction with naming samples down really well!!!

(Attempt to) Extract the samples of a DDB Vocaloid file. Help would be appreciated!

[GBATemp Thread](https://gbatemp.net/threads/i-found-out-the-format-of-samples-in-vocaloid-2-3-and-4-voicebanks-now-what.400402/)

[Discord Server](https://discord.gg/rZzwH9d4Hm)

## Usage:

```
extract_wav.py [-h] [--src-path SRC_PATH] [--dst-path DST_PATH] [--merge] [--silence-interval SILENCE_INTERVAL]

optional arguments:
  -h, --help            show this help message and exit
  --src-path SRC_PATH   source ddb file path
  --dst-path DST_PATH   destination extract path, default to be "./wav.zip (merge.wav)"
  --merge               enable to generate a merged large wav file
  --silence-interval SILENCE_INTERVAL
                        silence interval seconds when "merge" is enabled, default to be 0
```


```
extract_frm2.py [-h] [--src-path SRC_PATH] [--dst-path DST_PATH]

optional arguments:
  -h, --help           show this help message and exit
  --src-path SRC_PATH  source ddb file path
  --dst-path DST_PATH  destination extract path, default to be "./frm2.zip"     
```
