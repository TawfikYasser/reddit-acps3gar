import os, sys
# Get the current directory of this script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Append the parent directory to the Python path
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)
print(parent_dir)
print(sys.path)