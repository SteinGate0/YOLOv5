import re
import os
from pathlib import Path
import glob

def to_one(mulu, file_name,name_list, xmin, ymin, xmax, ymax, width, height):
    data = []
    num = 1
    for name, x1, y1, x2, y2 in zip(name_list, xmin, ymin, xmax, ymax):
        if name != 'Mask':
            continue
        class_id = class_dict[name]

        x1 = float(x1)
        y1 = float(y1)
        x2 = float(x2)
        y2 = float(y2)
        w1 = float(width[0])
        h1 = float(height[0])

        x = (x2 - x1) / 2 + x1
        y = (y2 - y1) / 2 + y1
        w = x2 - x1
        h = y2 - y1
        x = x / w1
        y = y / h1
        w = w / w1
        h = h / h1
        data.append(' '.join([str(class_id), str(x), str(y), str(w), str(h),'\n']))
        num += 1
    # print(data)

    with open(mulu + os.sep + file_name + '.txt', 'w') as f:
        f.writelines(data)



def xml_to_yolo(path):
    #files_list = os.listdir(path)
    files_list = glob.glob(str(path)+os.sep + '*.*')
    mulu = path.parent.joinpath('txt')
    # files_path = []
    # for file in files_list:
    #     files_path.append(os.path.join(path, file))
    for file in files_list:
        file_name = file.split(os.sep)[-1].split('.')[0]
        with open(file, 'r',encoding="UTF-8") as f:
            data = f.read()
            name_list = re.findall('<name>(.*?)</name>', data)
            xmin = re.findall('<xmin>(.*?)</xmin>', data)
            ymin = re.findall('<ymin>(.*?)</ymin>', data)
            xmax = re.findall('<xmax>(.*?)</xmax>', data)
            ymax = re.findall('<ymax>(.*?)</ymax>', data)
            width = re.findall('<width>(.*?)</width>', data)
            height = re.findall('<height>(.*?)</height>', data)
            to_one(str(mulu), file_name, name_list, xmin, ymin, xmax, ymax, width, height)


def make_dir(P):
    if P.exists():
        pass
    else:
        P.mkdir()


if __name__ == '__main__':
    class_dict = {'nomask':0, 'Mask':1}
    P = Path('D://Project_data//mask_data//other//label//16//xml')
    make_dir(P.parent.joinpath('txt'))
    xml_to_yolo(P)
    print('完成')