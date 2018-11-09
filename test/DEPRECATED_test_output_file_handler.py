#this file is resposnible for counting the files in the output directory and returning the latest file
import unittest
import tempfile
import os
from os.path import getmtime
from unittest import mock
from unittest.mock import patch
from main.output_file_handler import OutputFileHandler

class OutputFileHandlerTests(unittest.TestCase):

    def test_if_no_files_exist_in_output_directory_then_return_0(self):
        o= OutputFileHandler
        with tempfile.TemporaryDirectory() as tmpdir:
            print('Created a temp directory for testing %s' % tmpdir)
            self.assertEqual(0,o.count_files(tmpdir))

    def test_if_files_exist_return_count_of_those_files(self):
        o= OutputFileHandler
        #test with 34 files

        with tempfile.TemporaryDirectory() as tmpdir:
            print('created temporary directory\n', tmpdir)
            for i in range(34):
                open(os.path.join(tmpdir, str(i)), "w").close()
            self.assertEqual(34, o.count_files(tmpdir))


      # @patch('main.output_file_handler.OutputFileHandler.count_files')
      # def test_if_count_files_return_1_then_get_latest_file_return_that_file(self,mock_count_files):
      #     o = OutputFileHandler
      #     mock_count_files.return_value = 1
      #
      #     with tempfile.TemporaryDirectory() as tmpdirname:
      #         with tempfile.NamedTemporaryFile(dir=tmpdirname) as test_file:
      #             expected_file = o.get_latest_file(tmpdirname)
      #             self.assertEqual(test_file.gettempprefix(),expected_file)

    # @patch('main.output_file_handler.OutputFileHandler.count_files')
    # def test_if_more_than_1_files_exist_in_dir_then_get_latest_file_returns_the_latest_file(self,mock_count_files):
    #     o= OutputFileHandler
    #     mock_count_files.return_value = 3



        # with tempfile.TemporaryDirectory() as tmpdirname:
        #     print('created temporary directory\n', tmpdirname)
        #     with tempfile.NamedTemporaryFile(dir=tmpdirname) as test_file1:
        #         print('created temporary file\n', test_file1.name + str(getmtime(test_file1.name)))
        #         with tempfile.NamedTemporaryFile(dir=tmpdirname) as test_file2:
        #             print('created temporary file\n', test_file2.name +str(getmtime(test_file2.name)))
        #             with tempfile.NamedTemporaryFile(dir=tmpdirname) as test_file3:
        #                 print('created temporary file\n', test_file3.name + str(getmtime(test_file3.name)))
        # pass


if __name__ == '__main__':
    unittest.main()
