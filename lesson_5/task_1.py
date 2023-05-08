from os import path


def files_info(file: str) -> tuple:
    if path.isfile(file):
        abspath = path.abspath(file)
        file_name = path.basename(file)
        name, extension = path.splitext(file_name)[0], path.splitext(file_name)[1]
        return abspath, name, extension


print(files_info('file.txt'))
