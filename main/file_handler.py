from pathlib import Path
from main.dir_handler import DirHandler
import datetime

class FileHandler:
	input_file_path = Path("input.csv") #need to check. .parent fixes creating input.csv after tests
	output_file_dir_path= DirHandler.path

	def createFile():
		DirHandler.createDir()
		if not FileHandler.input_file_path.exists():
			FileHandler.input_file_path.touch()
			print("input.csv File created!")
		else:
			print("input.csv File already exists. Skipping file creation")
		
	def get_mod_time():
		if FileHandler.input_file_path.exists():
			return str(datetime.datetime.fromtimestamp(FileHandler.input_file_path.stat().st_mtime).strftime('%d-%m-%Y'))
