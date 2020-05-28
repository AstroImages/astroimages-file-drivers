import os


# List all files in a directory using os.listdir
def list_files_in_folder(path, extension):
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if extension in file:
                files.append(os.path.join(r, file))
    return files


def read_full_file_in_bytes(path):
    contents = None
    try:
        with open(path, mode='rb') as file:
            contents = file.read()
    except FileNotFoundError:
        contents = None

    return contents


def store_files(path, files, overwrite=False):
    for file in files:
        store_file(path, file, overwrite)


def store_file(path, file, overwrite=False):
    pass
