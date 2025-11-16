class DynamicAttributes:
    def __init__(self, data):
        self._data = data

    def __getattr__(self, name):
        # This method is called only if 'name' is not found in the object's
        # or its class's regular attributes.
        if name in self._data:
            return self._data[name]
        else:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

# Create an instance of DynamicAttributes
my_object = DynamicAttributes({"name": "Alice", "age": 30})

# Access existing attributes
print(f"Name: {my_object.name}")
print(f"Age: {my_object.age}")

# Attempt to access a non-existent attribute, triggering __getattr__
try:
    print(my_object.city)
except AttributeError as e:
    print(f"Error: {e}")

# Demonstrate that __getattr__ is not called for existing attributes
my_object.occupation = "Engineer"
print(f"Occupation: {my_object.occupation}")
