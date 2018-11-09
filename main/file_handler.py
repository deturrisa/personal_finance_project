#this script will create a blank input file if it does not already exist
#1.1 it will back up the input file only if the input file is not blank
#1.2 will back up the input file only if the input file does not have the same contents as the latest output file
#Both 1.1 and 1.2 logic comes from content_handler

import os
import os.path
from shutil import copy
from main.dir_handler import DirHandler
from main.content_handler import ContentHandler
from main.file_name_handler import FileNameHandler

class FileHandler:

    def writeInputFile(input_file_path):
        if not os.path.isfile(input_file_path):
            open(input_file_path, 'a').close()
            print("input.csv created!")
        print("input.csv already exists")

    def clearInputFile(input_file_path):
        if os.path.isfile(input_file_path):
            with open(input_file_path,'w') as input_file:
                print("input file wiped ")
        print("no input file to wipe")

    def writeOutputFile(input_file_path,output_dir_path):
        FileHandler.writeInputFile(input_file_path)
        DirHandler.createDir(output_dir_path)

        blank = ContentHandler.input_file_is_blank(input_file_path)

        if not blank:
            output_file_name =FileNameHandler.get_backup_date() + ".csv"
            try:
                output_file_path = os.path.join(output_dir_path, output_file_name)
                copy(input_file_path,os.path.join(output_dir_path, output_file_name))
                FileHandler.clearInputFile(input_file_path)
            except TypeError:
                print("not a valid filename to write")
        print("input file is blank...skipping backup")
