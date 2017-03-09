import unittest
from CartManager import retrieve_document_from_file, create_carts, provide_count_in_file, generate_output_count

class TestTechnique(unittest.TestCase):

    def test_level1(self):
        document = retrieve_document_from_file("level1/data.json")
        cart_list = create_carts(document)
        for cart in cart_list:
            cart.compute_total(document["articles"])
        cart_output_dict = generate_output_count(cart_list)
        #the actual part of the test, we compare our dict with the theoretical result
        theo_result = retrieve_document_from_file("level1/output.json")
        self.assertDictEqual(cart_output_dict, theo_result)
        #printing the result in a file for beauty (we suppose we are really interested in the content, not formatting)
        provide_count_in_file(cart_output_dict, "level1/test_result.json")
        
    def test_level2(self):
        document = retrieve_document_from_file("level2/data.json")
        cart_list = create_carts(document)
        for cart in cart_list:
            cart.compute_total(document["articles"], document["delivery_fees"])
        cart_output_dict = generate_output_count(cart_list)
        #the actual part of the test, we compare our dict with the theoretical result
        theo_result = retrieve_document_from_file("level2/output.json")
        self.assertDictEqual(cart_output_dict, theo_result)
        #printing the result in a file for beauty (we suppose we are really interested in the content, not formatting)
        provide_count_in_file(cart_output_dict, "level2/test_result.json")

    def test_level3(self):
        document = retrieve_document_from_file("level3/data.json")
        cart_list = create_carts(document)
        for cart in cart_list:
            cart.compute_total(document["articles"], document["delivery_fees"], document["discounts"])
        cart_output_dict = generate_output_count(cart_list)
        #the actual part of the test, we compare our dict with the theoretical result
        theo_result = retrieve_document_from_file("level3/output.json")
        self.assertDictEqual(cart_output_dict, theo_result)
        #printing the result in a file for beauty (we suppose we are really interested in the content, not formatting)
        provide_count_in_file(cart_output_dict, "level3/test_result.json")
        

if __name__ == '__main__':
    unittest.main()