import unittest
import os
from main.content_handler import ContentHandler
from unittest.mock import patch
from unittest.mock import MagicMock
from main.file_handler import FileHandler

class ContentHandlerTests(unittest.TestCase):

    #look into re-writing this test better to mimic files
    def test_get_contents(self):
        c = ContentHandler
        test_content = "Lunch, 120"

        with open('test.csv','w') as test_file:
            test_file.write(test_content)

        result = c.get_contents(test_file.name)
        self.assertEqual(result, "Lunch, 120")
        #remove test file after finishing test
        os.remove('test.csv')
        #test raises exception when no such file
        self.assertRaises(FileNotFoundError, c.get_contents("nonexistent file"))

    @patch('main.content_handler.ContentHandler.get_contents')
    def test_if_input_file_content_is_blank_return_true_and_if_not_blank_return_false(self,mock_get_contents):
        c = ContentHandler
        mock_get_contents.return_value = ""
        result = c.input_file_is_blank("any input file")
        self.assertTrue(result)

        mock_get_contents.return_value = "   "
        result = c.input_file_is_blank("any input file")
        self.assertTrue(result)

        mock_get_contents.return_value = "   \n\t"
        result = c.input_file_is_blank("any input file")
        self.assertTrue(result)

        mock_get_contents.return_value = "this is not blank"
        result = c.input_file_is_blank("any input file")
        self.assertFalse(result)

    def test_if_input_file_content_is_same_as_output_file_content_return_false(self):
        c = ContentHandler
        test_content = "Lunch, 120"

        with open('test1.csv','w') as test_file1:
            test_file1.write(test_content)
        with open('test2.csv','w') as test_file2:
            test_file2.write(test_content)

        result = c.is_different(test_file1.name,test_file2.name)
        self.assertFalse(result)

        with open('test2.csv','w') as test_file2:
            test_file2.write("different content")

        result = c.is_different(test_file1.name,test_file2.name)
        self.assertTrue(result)
        #remove test file after finishing test
        os.remove('test1.csv')
        os.remove('test2.csv')

if __name__ == '__main__':
    unittest.main()
