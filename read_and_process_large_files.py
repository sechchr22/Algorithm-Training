"""
This way im reading and proccesing by one line
instead of saving the whole file to procces it later
im reading the line and yield is giving the line to process one by one is a generator
"""

def read_large_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        line = file.readline()
        while line:
            yield line
            line = file.readline()


def main(filepath):
    for line in read_large_file(filepath):
        process(line)

"""
same as
with open("large_file.log", "r") as f:
    for line in f:
        process(line)
"""