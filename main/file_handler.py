from pathlib import Path
from main.dir_handler import DirHandler

class FileHandler:
	input_file_path = Path("input.csv") #need to check. .parent fixes creating input.csv after tests
	output_file_dir_path= DirHandler.path
	output_file_path = output_file_dir_path.joinpath("output_file")


	def createFile():
		DirHandler.createDir()
		if not FileHandler.input_file_path.exists():
			FileHandler.input_file_path.touch()
			print("input.csv File created!")
		else:
			print("input.csv File already exists. Skipping file creation")
			FileHandler.output_file_path.touch()
