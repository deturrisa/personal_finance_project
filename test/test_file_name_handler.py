import unittest
from main.file_name_handler import FileNameHandler
from unittest.mock import patch
from freezegun import freeze_time

class FileNameHandlerTests(unittest.TestCase):

    @freeze_time("19-09-2016")
    @patch('main.file_handler.FileHandler.input_file_path')
    def test_get_backup_date(self,mock_input_file):
        f = FileNameHandler
        self.assertEqual(f.get_backup_date(), "19-09-2016")

if __name__ == '__main__':
    unittest.main()
