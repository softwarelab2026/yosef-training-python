import sys, os

file_path = sys.argv[1]
if not os.path.isdir(file_path):
    print("Directory not found")
else:
    files = os.listdir(file_path)
    print(files)
    