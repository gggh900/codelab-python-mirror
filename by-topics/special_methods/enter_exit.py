class ManagedFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("__enter__:")
        # Acquire the resource (open the file)
        self.file = open(self.filename, self.mode)
        print(f"File '{self.filename}' opened.")
        return self.file  # Return the file object for use in the 'with' block

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__:")
        # Release the resource (close the file)
        if self.file:
            self.file.close()
            print(f"File '{self.filename}' closed.")

# Usage with the 'with' statement
with ManagedFile('example.txt', 'w') as f:
    f.write("Hello, world!")
    print("Content written to file.")
