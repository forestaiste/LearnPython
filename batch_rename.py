import os
import time


def batch_rename(path):
    global img_num
    if not os.path.isdir(path) and not os.path.isfile(path):
        return False

    if os.path.isfile(path):
        file_path = os.path.split(path)
        lists = file_path[1].split('.')

        file_ext = lists[-1]
        img_ext = ['bmp', 'jpeg', 'gif', 'psd', 'png', 'jpg']
        if file_ext in img_ext:
            os.rename(path, file_path[0] + '/' + lists[0] + '_cn.' + file_ext)
            img_num += 1
        elif os.path.isdir(path):
            for item in os.listdir(path):
                batch_rename(os.path.join(path, item))

