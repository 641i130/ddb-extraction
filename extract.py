#!/usr/bin/env python3

import argparse
import os
import wave

from wave import Wave_write

start_encode = 'SND'.encode()
end_encode = 'FRM2'.encode()
wav_params = (1, 2, 44100, 0, 'NONE', 'NONE')
# threshold = 0


def parse_args(args=None):  # : list[str]
    # initialize parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--src-path', help='source ddb file path')
    parser.add_argument('--dst-path', help='destination extract path, default="./extract/"',
                        default='./extract/')
    parser.add_argument('--merge', help='enable to generate a merged large wav file',
                        action='store_true')

    # parse args
    args = parser.parse_args(args)
    src_path: str = os.path.normpath(args.src_path)
    dst_path: str = os.path.normpath(args.dst_path)
    merge: bool = args.merge
    if merge and not dst_path.endswith('.wav'):
        dst_path = os.path.join(dst_path, 'merge.wav')

    # make dirs
    dir_path = dst_path
    if dst_path.endswith('.wav'):
        dir_path = os.path.dirname(dst_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return src_path, dst_path, merge


def main():
    src_path, dst_path, merge = parse_args()
    with open(src_path, 'rb') as ddb_f:
        ddb_data = ddb_f.read()
    length = len(ddb_data)

    merge_f: Wave_write = None
    if merge:
        merge_f = wave.open(dst_path, 'wb')
        merge_f.setparams(wav_params)

    offset = 0
    file_id = 0
    while(True):
        if (start_idx := ddb_data.find(start_encode, offset)) == -1:
            break
        offset = start_idx+4
        if (end_idx := ddb_data.find(end_encode, offset)) == -1:
            break

        # There are cases that (end_idx - offset) % 2 == 1
        end_idx = offset+(end_idx-offset)//2*2

        offset = end_idx+5
        print(f'{file_id=:<20} progress: {offset:>15,} / {length:<15,}')

        wav_data = ddb_data[start_idx+4: end_idx]
        if merge:
            merge_f.writeframes(wav_data)
            # merge_f.writeframes(b'\x00'*1024)
        else:
            file_path = os.path.join(dst_path, f'{file_id}.wav')
            with wave.open(file_path, 'wb') as wav_f:
                wav_f: Wave_write
                wav_f.setparams(wav_params)
                wav_f.writeframes(wav_data)
            print('    wav saved at: ', file_path)
        file_id += 1
        # if file_id >= threshold and threshold > 0:
        #     break
        if offset >= length:
            break
    if merge:
        merge_f.close()
        print('merged wav saved at: ', dst_path)


if __name__ == '__main__':
    main()
