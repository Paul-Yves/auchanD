"""
    This module aims at managing the retrieval and building of carts, and outputting them
    Retrieved data are json document, read from file, but more functions could be defined
    to multiply data sources (document oriented db, rest apis...)
"""
import json
from Cart import Cart

def retrieve_document_from_file(filePath):
    """
        Basic method to retrieve json data from file
    """
    with open(filePath) as data_file:    
        data = json.load(data_file)
    return data

def provide_count_in_file(count_dict, filePath):
    with open(filePath, 'w') as outfile:
        json.dump(count_dict, outfile, indent=2)

def create_carts(document_dict):
    """
        Creates a list of carts out of the document
    """
    cart_list = []
    for cartDict in document_dict["carts"]:
        cart_list.append(Cart(cartDict))
    return cart_list

def generate_output_count(cart_list):
    """
        Create the data structure of output document with totals for the carts
    """
    return {"carts": [cart.generate_output_dict() for cart in cart_list]}