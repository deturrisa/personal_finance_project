import unittest
from unittest import mock
from main.dir_handler import DirHandler

class DirHandlerTests(unittest.TestCase):

    #test when dir exist and not exist
    @mock.patch('main.dir_handler.os.path')
    @mock.patch('main.dir_handler.os')
    def test_createDir(self, mock_os, mock_dir_path):

        d = DirHandler
        mock_dir_path.isdir.return_value = True

        d.createDir("any output file path")

        #test that mkdir was not called
        self.assertFalse(mock_os.mkdir.called, "Failed to create directory if directory is present.")

        mock_dir_path.isdir.return_value = False

        d.createDir("any output file path")

        mock_os.mkdir.assert_called_with("any output file path")

if __name__ == '__main__':
    unittest.main()
