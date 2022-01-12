import os


def file1(fname):
    stat = os.stat(fname)
    return stat.st_size


print("The file size of a plain File is: ", file1('spamcodes.txt'), "bytes")
