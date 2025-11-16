import ctypes
import sys

# Create a Python integer object
a = 0x7fff

# Get the memory address of the object
object_address = id(a)

# Get the size of the object in bytes
object_size = sys.getsizeof(a)

# Use ctypes.string_at to get the raw bytes from the memory address
# string_at returns a bytes object
raw_bytes = ctypes.string_at(object_address, object_size)

# Print the raw bytes in hexadecimal format
print(raw_bytes.hex())

