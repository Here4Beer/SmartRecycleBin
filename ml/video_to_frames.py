import os
import argparse
import cv2
from tqdm import tqdm
import numpy as np


def extract_frames(video, out_path, file_name):
    vidcap = cv2.VideoCapture(video)
    vidcap.read()

    success = True
    count = 0
    while success:
        success, image = vidcap.read()
        if not success:
            continue
        save_path = out_path if np.random.rand() > 0.2 else out_path.replace('train', 'val')
        if not os.path.isdir(save_path):
            os.makedirs(save_path, exist_ok=True)
        cv2.imwrite(os.path.join(save_path, f'{file_name}_{count}.jpg'), image)
        count += 1


def video_to_frames(path_in, path_out):
    for root, dirs, files in os.walk(path_in):
        for file in tqdm(files):
            if not file.endswith('.mp4'):
                continue

            video = os.path.join(root, file)
            file_name = file.split('.')[0]
            rel_path = os.path.relpath(root, start=path_in)
            out_path = os.path.join(path_out, rel_path)
            extract_frames(video, out_path, file_name)


if __name__ == '__main__':
    a = argparse.ArgumentParser()
    a.add_argument('--path_in', help='path to video')
    a.add_argument('--path_out', help='path to images')
    args = a.parse_args()
    video_to_frames(args.path_in, args.path_out)
