import os
import os.path
from filecmp import cmp
class ContentHandler:

    def get_contents(file):
        try:
            return open(file,'r').read()
        except FileNotFoundError:
            print("no such file or invalid file")


    def input_file_is_blank(input_file):
        input_file_contents = ContentHandler.get_contents(input_file)
        if input_file_contents == "" or input_file_contents.isspace():
            return True
        return False
