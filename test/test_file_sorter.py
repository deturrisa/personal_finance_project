import unittest
from main.file_sorter import FileSorter

class FileSorterTests(unittest.TestCase):

    def test_sort_files_in_order_of_date_newwest_to_oldest(self):

        test_filename = ["01-03-18.csv","01-01-18.csv"]
