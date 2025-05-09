import os

def find(path, dir_name):
    matches = []
    for root, dirs, files in os.walk(path):
        for d in dirs:
            if d == dir_name:
                matches.append(os.path.abspath(os.path.join(root, d)))
    for match in matches:
        print(match)

# Example usage:
find("./tree", "python")