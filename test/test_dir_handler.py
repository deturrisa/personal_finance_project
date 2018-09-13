import unittest
from unittest.mock import patch
from main.dir_handler import DirHandler

class DirHandlerTests(unittest.TestCase):

    @patch('main.dir_handler.DirHandler.path')
    def test_if_output_files_dir_not_exist_createDir_call_mkdir(self,mock_Path):
        d = DirHandler
        mock_Path.exists.return_value = False
        d.createDir()
        mock_Path.mkdir.assert_called()

    @patch('main.dir_handler.DirHandler.path')
    def test_if_output_files_dir_exists_createDir_not_call_mkdir(self,mock_Path):
        d = DirHandler
        mock_Path.exists.return_value = True
        d.createDir()
        mock_Path.mkdir.assert_not_called()

if __name__ == '__main__':
    unittest.main()
