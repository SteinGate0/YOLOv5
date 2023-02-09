'''
本代码用于去除YOLO格式标注文件中不合理的文件与图片 一起删除
'''

import re
import os
from pathlib import Path
import glob
import argparse

def Check_YOLO(source_txt_path,source_img_path):
    for file in os.listdir(source_txt_path):
        if file.split('.')[-1] == 'txt':
            img_path = os.path.join(source_img_path,file.replace('.txt','.jpg')) #png to jpg
            txt_path = os.path.join(source_img_path,file)
            txt_file = open(os.path.join(source_txt_path,file)).read().splitlines()

            for line in txt_file:
                line_split = line.split(' ')

                if len(line_split) == 0 :
                    os.remove(img_path)
                    os.remove(txt_path)
                    continue

                if len(line_split) !=5 :
                    os.remove(img_path)
                    os.remove(txt_path)







if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source_txt_path', type=str, default="D:\PyCharm\MyProjcet\Mask_test\yolov5-src\data//new_mask_data//all_mask")
    parser.add_argument('--source_img_path', type=str, default="D:\PyCharm\MyProjcet\Mask_test\yolov5-src\data//new_mask_data//all_mask")

    opt = parser.parse_args()

    Check_YOLO(opt.source_txt_path,opt.source_img_path)