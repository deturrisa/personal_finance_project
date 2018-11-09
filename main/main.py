from main.file_handler import FileHandler
from main.PATHS import INPUT_FILE, OUTPUT_DIR

def main():
    FileHandler.writeOutputFile(INPUT_FILE, OUTPUT_DIR)


if __name__ == "__main__":
    main()
