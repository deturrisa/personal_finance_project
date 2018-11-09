import os
import os.path

class DirHandler:

	def createDir(output_dir_path):
		if not os.path.isdir(output_dir_path):
			os.mkdir(output_dir_path)
			print("output_file Directory created!")
		else:
			print("output_files Directory already exists. Skipping directory creation")
