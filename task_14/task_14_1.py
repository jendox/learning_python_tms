class MyOpen:

    def __init__(self, filename, method):
        self.file_obj = open(filename, method)

    def __enter__(self):
        return self.file_obj;

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()

