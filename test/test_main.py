import unittest
import os
import os.path
from main.PATHS import TEST_INPUT_FILE, TEST_OUTPUT_DIR
from shutil import rmtree
from main.file_handler import FileHandler
from freezegun import freeze_time
class MainTests(unittest.TestCase):


    def test_if_no_input_file_and_no_output_dir_exists_then_they_are_created(self):

        FileHandler.writeOutputFile(TEST_INPUT_FILE, TEST_OUTPUT_DIR)

        self.assertTrue(os.path.isdir(TEST_OUTPUT_DIR))
        self.assertTrue(os.path.isfile(TEST_INPUT_FILE))

        os.remove(TEST_INPUT_FILE)
        rmtree(TEST_OUTPUT_DIR)

    def test_if_input_file_is_blank_then_no_file_is_copied_to_output_dir_and_input_file_remains_blank(self):
        #create file and dir
        FileHandler.writeOutputFile(TEST_INPUT_FILE, TEST_OUTPUT_DIR)
        #attempt to backup by calling function again
        FileHandler.writeOutputFile(TEST_INPUT_FILE, TEST_OUTPUT_DIR)
        #assert file is blank
        with open(TEST_INPUT_FILE, 'r') as input_file:
            self.assertEqual("",input_file.read())
        #assert no file exists in output
        number_of_files = len([f for f in os.listdir(TEST_OUTPUT_DIR) if os.path.isfile(os.path.join(TEST_OUTPUT_DIR, f))])
        self.assertEqual(0,number_of_files)
        os.remove(TEST_INPUT_FILE)
        rmtree(TEST_OUTPUT_DIR)

    @freeze_time("01-01-2018")
    def test_if_input_file_has_content_then_it_is_copied_to_output_directory_with_date_as_name_and_input_file_is_cleared(self):
        #create file and dir
        FileHandler.writeOutputFile(TEST_INPUT_FILE, TEST_OUTPUT_DIR)
        #create input file with content
        with open(TEST_INPUT_FILE, 'w') as input_file:
            input_file.write("Lunch, 120")
        #call function again to backup the input file
        FileHandler.writeOutputFile(TEST_INPUT_FILE, TEST_OUTPUT_DIR)
        #Get file from output dir
        output_files = os.listdir(TEST_OUTPUT_DIR)

        #assert filename is the same as date
        self.assertEqual("01-01-2018.csv",output_files[0])

        #assert conent of output file is the same as input file
        with open(os.path.join(TEST_OUTPUT_DIR,output_files[0]), 'r') as output_file:
            self.assertEqual('Lunch, 120', output_file.read())

        #assert file is blank
        with open(TEST_INPUT_FILE, 'r') as input_file:
            self.assertEqual("",input_file.read())

        os.remove(TEST_INPUT_FILE)
        rmtree(TEST_OUTPUT_DIR)


if __name__ == '__main__':
    unittest.main()
