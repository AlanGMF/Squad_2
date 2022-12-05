import os

def root_file()-> dict:
    """Gets the path of the CSV files and their respective name

    :return: root_file(Dictionary filename - path)
    :rtype: dict
    """
    # Current work path
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'file')
    # Route files
    files = os.listdir(root)
    # Dictionary filename - path
    root_file = {}
    for f in files:
        root_file[f] = root + '/' + f
    
    return root_file
