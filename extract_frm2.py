#!/usr/bin/env python3

import argparse
import os
import zipfile

start_encode = 'FRM2'.encode()


def parse_args(args=None):  # : list[str]
    # initialize parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--src-path', help='source ddb file path')
    parser.add_argument('--dst-path',
                        help='destination extract path, default to be "./frm2.zip"')

    # parse args
    args = parser.parse_args(args)
    src_path: str = os.path.normpath(args.src_path)
    dst_path: str = args.dst_path
    if dst_path is None:
        dst_path = './frm2.zip'
    dst_path: str = os.path.normpath(dst_path)

    # make dirs
    dir_path = dst_path
    if dst_path.endswith('.zip'):
        dir_path = os.path.dirname(dst_path)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return src_path, dst_path


def main():
    src_path, dst_path = parse_args()
    with open(src_path, 'rb') as ddb_f:
        ddb_data = ddb_f.read()
    length = len(ddb_data)

    zip_f = zipfile.ZipFile(dst_path, 'w', compression=zipfile.ZIP_STORED)

    counter = 0
    offset = 0
    while(True):
        if (start_idx := ddb_data.find(start_encode, offset)) == -1:
            break

        file_length = int.from_bytes(ddb_data[start_idx+4:start_idx+8],
                                     byteorder='little')
        offset = start_idx+file_length
        if offset > length:
            break
        frm2_data = ddb_data[start_idx: offset]
        file_id = f'{start_idx:0>8x}'

        counter += 1
        print(f'{counter:<10d}{file_id=} progress: {offset:0>8x} / {length:0>8x}')

        file_path = f'frm2/{file_id}.frm2'
        zip_f.writestr(file_path, frm2_data)
        print('    frm2 saved at: ', file_path)
    zip_f.close()
    print('zip file saved at: ', dst_path)


if __name__ == '__main__':
    main()
