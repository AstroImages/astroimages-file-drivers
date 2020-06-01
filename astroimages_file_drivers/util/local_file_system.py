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


def store_file(folder_name, file, overwrite=False):
    pass
