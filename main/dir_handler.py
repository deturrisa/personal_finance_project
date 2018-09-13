from pathlib import Path

class DirHandler:
	path = Path("output_files") #need to check

	def createDir():
		if not DirHandler.path.exists():
			DirHandler.path.mkdir()
			print("output_files Directory created!")
		else:
			print("output_files Directory already exists. Skipping directory creation")
