import unittest
import os
import tempfile
from unittest import mock
from main.file_handler import FileHandler
from unittest.mock import patch


class FileHandlerTests(unittest.TestCase):

    #test when file exist and not exist
    @mock.patch('builtins.open')
    @mock.patch('main.file_handler.os.path')
    def test_writeInputFile_calls_open(self,mock_input_file,mock_open):

        f = FileHandler
        mock_input_file.isfile.return_value = True

        f.writeInputFile("any file")

        #test open was not called
        self.assertFalse(mock_open.called)

        mock_input_file.isfile.return_value = False

        f.writeInputFile("any file")

        mock_open.assert_called_with("any file",'a')

    @mock.patch('builtins.open') #stop test throwing NoneType error
    @mock.patch('main.dir_handler.DirHandler.createDir')
    @mock.patch('main.file_handler.FileHandler.writeInputFile')
    def test_writeOutputFile_calls_writeInputFile_and_calls_createDir_of_dir_handler(self,mock_writeInputFile, mock_createDir, mock_open):

        f = FileHandler
        f.writeOutputFile("any file", "any dir path")
        mock_writeInputFile.assert_called_with("any file")
        mock_createDir.assert_called_with("any dir path")



    @mock.patch('main.file_handler.copy')#stops files and dir created
    @mock.patch('main.dir_handler.os.path')#stops files and dir created
    @mock.patch('main.file_handler.os.path')#stops files and dir created
    @mock.patch('main.content_handler.ContentHandler.input_file_is_blank')
    @mock.patch('main.file_name_handler.FileNameHandler.get_backup_date')
    def test_if_input_file_is_blank_then_get_backup_date_is_called(self,mock_get_backup_date,mock_input_file_is_blank,mock_os_input_file,mock_os_dir,mock_copy):
        f = FileHandler

        mock_copy.return_value = "whatever"#stops files and dir created

        mock_input_file_is_blank.return_value = False
        mock_get_backup_date.return_value = "any file" #stops copy function throwing error
        f.writeOutputFile("any file", "any dir path")

        mock_input_file_is_blank.assert_called_with("any file")

        self.assertTrue(mock_get_backup_date.called)

    @mock.patch('main.dir_handler.os.path')#stops files and dir created
    @mock.patch('main.file_handler.os.path')#stops files and dir created
    @mock.patch('main.file_handler.copy')#stops files and dir created
    @mock.patch('main.content_handler.ContentHandler.input_file_is_blank')
    @mock.patch('main.file_name_handler.FileNameHandler.get_backup_date')
    def test_if_input_file_is_blank_returns_true_then_get_backup_date_is_not_called(self,mock_get_backup_date,mock_input_file_is_blank,mock_copy,mock_os_input_file,mock_os_dir):
        f = FileHandler
        mock_copy.return_value = "whatever"#stops files and dir created

        mock_input_file_is_blank.return_value = True
        mock_get_backup_date.return_value = "19-01-2018"
        f.writeOutputFile("any file", "any dir path")

        mock_input_file_is_blank.assert_called_with("any file")

        self.assertFalse(mock_get_backup_date.called)

    @mock.patch('main.file_handler.copy')
    @mock.patch('main.file_handler.os.path')
    @mock.patch('main.content_handler.ContentHandler.input_file_is_blank')
    @mock.patch('main.file_name_handler.FileNameHandler.get_backup_date')
    def test_if_input_file_is_blank_returns_true_then_file_is_written_to_output_dir_with_correct_name(self,mock_get_backup_date,mock_input_file_is_blank,mock_os_path,mock_copy):
        f = FileHandler
        mock_date = "29-10-2018"
        mock_get_backup_date.return_value = mock_date
        mock_input_file_is_blank.return_value = False
        mock_os_path.join.return_value = mock_date + ".csv"
        f.writeOutputFile("any file", "any dir path")

        mock_copy.assert_called_with("any file", mock_date+".csv" )
        mock_os_path.join.assert_called_with("any dir path",mock_date+".csv")

    # #test when file exist and not exist
    @mock.patch('builtins.open')
    @mock.patch('main.file_handler.os.path')
    def test_clearInputFile_calls_open(self,mock_input_file,mock_open):

        f = FileHandler
        mock_input_file.isfile.return_value = True

        f.clearInputFile("any file")

        #test open was not called
        self.assertTrue(mock_open.called)

        mock_input_file.isfile.return_value = False

        f.clearInputFile("any file")

        mock_open.assert_called_with("any file",'w')

    @mock.patch('main.file_handler.copy')
    @mock.patch('main.dir_handler.os.path')#stops files and dir created
    @mock.patch('main.file_handler.os.path')#stops files and dir created
    @mock.patch('main.content_handler.ContentHandler.input_file_is_blank')
    @mock.patch('main.file_handler.FileHandler.clearInputFile')
    def test_if_input_file_is_blank_then_clearInputFile_is_called(self,mock_clearInputFile,mock_input_file_is_blank,mock_os_input,mock_os_dir,mock_copy):

        f = FileHandler
        mock_input_file_is_blank.return_value = False
        mock_os_dir.isdir.return_value = True
        mock_os_input.isfile.return_value = True
        mock_copy.return_value = "whatever"#stops files and dir created
        f.writeOutputFile("any file", "any dir path")

        mock_clearInputFile.assert_called_with("any file")

        # with tempfile.TemporaryDirectory() as tmpdir:
        #     test_file_name = os.path.join(tmpdir, "any file")
        #     with open(test_file_name,'w+') as test_file:
        #         test_file.write("Lunch, 120")
        #         test_file.seek(0) #start at beginning of file
        #         self.assertEqual("Lunch, 120",test_file.read())
        #         f.clearInputFile("any file")
        #         self.assertEqual("",test_file.read())

if __name__ == '__main__':
    unittest.main()
