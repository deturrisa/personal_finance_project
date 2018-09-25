import unittest
from main.file_handler import FileHandler
from unittest.mock import patch

class FileHandlerTests(unittest.TestCase):

    @patch('main.dir_handler.DirHandler.createDir')
    def test_create_file_calls_create_dir_of_dir_handler(self,mock_create_dir):
        FileHandler.createFile()
        self.assertTrue(mock_create_dir)

    @patch('main.file_handler.FileHandler.input_file_path')
    def test_if_input_file_not_exists_then_createFile_calls_touch(self,mock_Path_file):
        f = FileHandler
        mock_Path_file.exists.return_value = False
        f.createFile()
        mock_Path_file.touch.assert_called()

    @patch('main.file_handler.FileHandler.input_file_path')
    def test_if_input_file_exists_createFile_not_call_touch(self,mock_Path_file):
        f = FileHandler
        mock_Path_file.exists.return_value = True
        f.createFile()
        mock_Path_file.touch.assert_not_called()

    @patch('main.file_handler.FileHandler.input_file_path')
    def test_get_modification_date_of_input_file(self,mock_Path_file):
        f = FileHandler
        mock_Path_file.exists.return_value = True
        #stubbing the input file to have a modification date for 24-09-2018
        mock_Path_file.stat().st_mtime = 1537774559.9282894
        self.assertEqual(f.get_mod_time(), "24-09-2018")

    @patch('main.file_handler.FileHandler.output_file_dir_path')
    @patch('main.file_handler.FileHandler.input_file_path')
    def test_if_no_output_file_exists_then_create_output_file_as_modification_date_of_input_file(self,mock_Path_file,mock_output_dir_path):
        f = FileHandler
        mock_Path_file.exists.return_value = True
        mock_Path_file.stat().st_mtime = 1537774559.9282894



if __name__ == '__main__':
    unittest.main()
