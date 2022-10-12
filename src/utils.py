"""
This function gets a simple file row count for data load confirmation
"""
def ctrl_count(fname):
    f = open(fname)
    count = sum(1 for line in f)
    f.close()
    return count
