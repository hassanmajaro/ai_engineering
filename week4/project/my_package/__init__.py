#   This is a special file that tells python that my_package is a package.
# It can be empty or used to initialize the package

# __init__.py
print("my_package is being imported")

# Optional: import functions directly for easier access
from .math_utils import add, subtract
from .string_utils import capitalize_text

