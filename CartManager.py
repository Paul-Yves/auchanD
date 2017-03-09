import json

def retrieve_document(filePath):
    """
    Basic method to retrieve json data from file
    """
    with open(filePath) as data_file:    
        data = json.load(data_file)
    return data