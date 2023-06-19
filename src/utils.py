import os

class cd:
    def __init__(self, dest: str):
        self.dest = dest
    
    def __enter__(self):
        self.original_path = os.getcwd()
        os.chdir(self.dest)
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        os.chdir(self.original_path)
