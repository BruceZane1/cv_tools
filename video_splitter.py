# -*- coding: UTF-8 -*-
# '''=================================================
# @Project -> File :climbing_detection -> video_splitter.py
# @IDE    :PyCharm
# @Version:
# @Author : Bochao Zheng
# @Time   : 2023-11-01 9:13
# @Email  : seu_zbc@hotmail.com
# @Desc   :
# '''=================================================

import argparse
import os

import cv2


# from argparse import ArgumentParser


def rename_video(video_dir_path):
    basedir = video_dir_path
    prefix_dir = basedir.split('/')[-1]
    for ndx, file_name in enumerate(os.listdir(basedir)):
        file_suffix = os.path.splitext(file_name)[-1]
        new_file_name = f"{prefix_dir}_{ndx}{file_suffix}"
        new_file_path = os.path.join(basedir, new_file_name)
        original_file_path = os.path.join(basedir, file_name)
        os.rename(original_file_path, new_file_path)


def video_split(video_dir_path, sample_rate_fps):
    basedir = video_dir_path
    splitted_image_dir_path = os.path.join(basedir, "images")
    number_all_images_splited = 0
    if not (os.path.exists(splitted_image_dir_path)):
        os.mkdir(splitted_image_dir_path)
    for ndx, video_file_name in enumerate(os.listdir(basedir)):
        video_file_path = os.path.join(basedir, video_file_name)
        cap = cv2.VideoCapture(video_file_path)
        original_fps = cap.get(cv2.CAP_PROP_FPS)
        index_frame = 0
        index_image = 0
        if cap.isOpened():
            rval, frame = cap.read()
        else:
            rval = False
        while rval:

            rval, frame = cap.read()
            if index_frame % sample_rate_fps == 0 and frame is not None:
                print(f"video_source={video_file_name},index_image={index_image}, index_frame={index_frame}\n")
                video_file_name_without_suffix = os.path.splitext(video_file_name)[0]
                image_file_name = f"{video_file_name_without_suffix}_{index_image}.jpg"
                image_file_path = os.path.join(splitted_image_dir_path, image_file_name)
                cv2.imwrite(image_file_path, frame)
                index_image += 1

            index_frame += 1
        number_all_images_splited += index_image
    print("Total splitted images number={}".format(number_all_images_splited))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="video_splitter",
                                     description="split videos in given folder into frames at designated fps")
    parser.add_argument("-r", "--rename", action="store_true", help="rename video file")
    parser.add_argument("-p", "--path", help="path of dir where videos locate in")
    parser.add_argument("-f", "--fps", type=int, help="designated fps for frame")
    args = parser.parse_args()
    video_dir_path = args.path
    fps = args.fps
    if args.rename:
        rename_video(video_dir_path)
    video_split(video_dir_path, fps)
