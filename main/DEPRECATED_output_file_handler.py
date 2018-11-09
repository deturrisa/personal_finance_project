from os import listdir
from os.path import isfile, join

class OutputFileHandler:

    def count_files(output_file_dir):
        return len([f for f in listdir(output_file_dir) if isfile(join(output_file_dir, f))])

    def get_latest_file(output_file_dir):
        files = listdir(output_file_dir)
        if OutputFileHandler.count_files(output_file_dir) == 1:
            return files[0]
