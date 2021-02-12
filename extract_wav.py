#!/usr/bin/env python3

import argparse
import io
import os
import wave
import zipfile

from wave import Wave_write

start_encode = 'SND '.encode()
wav_params = (1, 2, 44100, 0, 'NONE', 'NONE')


def parse_args(args=None):  # : list[str]
    # initialize parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--src-path', help='source ddb file path')
    parser.add_argument('--dst-path',
                        help='destination extract path, default to be "./wav.zip (merge.wav)"')
    parser.add_argument('--merge', help='enable to generate a merged large wav file',
                        action='store_true')
    parser.add_argument('--silence-interval', help='silence interval seconds when "merge" is enabled, default to be 0',
                        type=float, default=0.0)

    # parse args
    args = parser.parse_args(args)
    src_path: str = os.path.normpath(args.src_path)
    dst_path: str = args.dst_path
    merge: bool = args.merge
    silence_interval: float = args.silence_interval
    num_bytes = int(wav_params[1]*wav_params[2]*silence_interval)

    if dst_path is None:
        dst_path = './merge.wav' if merge else './wav.zip'
    elif merge and not os.path.isdir(dst_path):
        dst_path = os.path.join(dst_path, 'merge.wav')
    dst_path: str = os.path.normpath(dst_path)

    # make dirs
    dir_path = dst_path
    if dst_path.endswith('.wav') or dst_path.endswith('.zip'):
        dir_path = os.path.dirname(dst_path)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path)

    return src_path, dst_path, merge, num_bytes


def main():
    src_path, dst_path, merge, num_bytes = parse_args()
    with open(src_path, 'rb') as ddb_f:
        ddb_data = ddb_f.read()
    length = len(ddb_data)

    merge_f: Wave_write = None
    zip_f: zipfile.ZipFile = None
    if merge:
        merge_f = wave.open(dst_path, 'wb')
        merge_f.setparams(wav_params)
    else:
        zip_f = zipfile.ZipFile(dst_path, 'w', compression=zipfile.ZIP_STORED)

    counter = 0
    offset = 0
    while(True):
        if (start_idx := ddb_data.find(start_encode, offset)) == -1:
            break

        file_length = int.from_bytes(ddb_data[start_idx+4:start_idx+8],
                                     byteorder='little')
        """
        4 bytes of "SND "
        4 bytes of size
        4 bytes of frame rate
        2 bytes of 01 00 (channel?)
        4 bytes of unknown
        [data]
        """
        offset = start_idx+file_length
        if offset > length:
            break
        pcm_data = ddb_data[start_idx+18: offset]
        file_id = f'{start_idx:0>8x}'

        counter += 1
        print(f'{counter:<10d}{file_id=} progress: {offset:0>8x} / {length:0>8x}')

        if merge:
            merge_f.writeframes(pcm_data)
            merge_f.writeframes(b'\x00'*num_bytes)
        else:
            bytes_f = io.BytesIO()
            file_path = f'wav/{file_id}.wav'
            with wave.open(bytes_f, 'wb') as wav_f:
                wav_f: Wave_write
                wav_f.setparams(wav_params)
                wav_f.writeframes(pcm_data)
            zip_f.writestr(file_path, bytes_f.getvalue())
            bytes_f.close()
            print('    wav saved at: ', file_path)
    if merge:
        merge_f.close()
        print('merged wav saved at: ', dst_path)
    else:
        zip_f.close()
        print('zip file saved at: ', dst_path)


if __name__ == '__main__':
    main()
