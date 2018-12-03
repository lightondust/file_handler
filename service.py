import os
from CONST import BASE_DIR


def get_file_list(dir_path):
    path = os.path.join(BASE_DIR, dir_path)
    if not os.path.exists(path):
        path = BASE_DIR
    file_list = os.listdir(path)
    file_res = {}
    file_res['dirs'] = [file for file in file_list if os.path.isdir(os.path.join(path, file))]
    file_res['imgs'] = [file for file in file_list if file.endswith('jpg') or file.endswith('png') or file.endswith('PNG')]
    file_res['files'] = [file for file in file_list if file not in file_res['dirs']+file_res['imgs']]
    return file_res
