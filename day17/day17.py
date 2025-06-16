#Context Managers
# Build a context manager for safe file handling
class FileManager():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"Opening {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tab):
        if self.file:
            self.file.close()
            print(f"Closing {self.filename}")

with FileManager("day17InputFile.txt", "r") as f:
    content = f.read()
    print("File content:\n", content)