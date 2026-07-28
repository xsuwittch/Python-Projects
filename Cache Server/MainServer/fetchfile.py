
def fetchfile(filename):
    try:
        file = open(filename,'r')
        return file
    except FileNotFoundError as e:
        return 0