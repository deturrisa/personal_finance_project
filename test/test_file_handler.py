import unittest
from main.file_handler import FileHandler
from unittest.mock import patch

class FileHandlerTests(unittest.TestCase):

    @patch('main.dir_handler.DirHandler.createDir')
    def test_create_file_calls_create_dir_of_dir_handler(self,mock_create_dir):
        FileHandler.createFile()
        self.assertTrue(mock_create_dir)

    @patch('main.file_handler.FileHandler.output_file_dir_path')
    @patch('main.file_handler.FileHandler.input_file_path')
    def test_if_input_file_not_exists_then_createFile_calls_touch(self,mock_Path_file,mock_Path_dir):
        f = FileHandler
        mock_Path_dir.exists.return_value = True #stop output_file_dir_created
        mock_Path_file.exists.return_value = False
        f.createFile()
        mock_Path_file.touch.assert_called()

    @patch('main.file_handler.FileHandler.output_file_dir_path')
    @patch('main.file_handler.FileHandler.input_file_path')
    def test_if_input_file_exists_createFile_not_call_touch(self,mock_Path_file,mock_Path_dir):
        f = FileHandler
        mock_Path_dir.exists.return_value = True
        mock_Path_file.exists.return_value = True
        f.createFile()
        mock_Path_file.touch.assert_not_called()

    @patch('main.file_handler.FileHandler.output_file_path')
    @patch('main.file_handler.FileHandler.input_file_path')
    def test_if_input_file_exists_and_0_output_file_exists_then_touch_called_once(self,mock_input_file,mock_output_file):
        f = FileHandler
        mock_output_file.exists.return_value = False
        mock_input_file.exists.return_value = True
        f.createFile()
        mock_output_file.touch.assert_called()

    

if __name__ == '__main__':
    unittest.main()
