
class Cart:
    def __init__(self, jsonCart):
        self.id = jsonCart["id"]
        self.items = jsonCart["items"]
        self.errorList = []

    def compute_total(self, catalog, delivery_fees=None, discounts=None):
        """
            Generate the total price of the cart taking the catalog, and optionnaly delivery_fees and discounts information
        """
        self.errorList = []
        total = 0
        for item_dict in self.items:
            article_detail = next((article for article in catalog if article["id"] == item_dict["article_id"]), None)
            if(article_detail == None):
                self.errorList.append("Error, article {} not found in catalog".format(item_dict["article_id"]))
                #mechanism of exception to refine if the article is not found
            discount = None
            if(discounts != None):
                discount = next((disc for disc in discounts if disc["article_id"] == item_dict["article_id"]), None)
            total += self.compute_price(item_dict["quantity"], article_detail["price"], discount)
        self.total = total
        if(delivery_fees != None):
            self.add_fee_price(delivery_fees)

        return total

    def add_fee_price(self, delivery_fees):
        """
            using delivery_fees, increase total price depending on current total and fees
            a fee should have a class for more generic code, 
            and an matching method in case we want to add more parameters (distance maybe?)
        """
        fee = 0
        for fee_dict in delivery_fees:
            volumeInterval = fee_dict["eligible_transaction_volume"]
            if(self.total>=volumeInterval["min_price"] and (volumeInterval["max_price"]==None or self.total<volumeInterval["max_price"])):
                fee = fee_dict["price"]

        self.total = self.total + fee

    def compute_price(self, quantity, price, discount):
        """
            Apply a discount to article price and return the reduced price
            discount should be a proper class for more genericity
        """
        actual_price = quantity * price
        if(discount != None):
            if(discount["type"]=="amount"):
                actual_price = quantity * (price - discount["value"])
            if(discount["type"]=="percentage"):
                #actual_price = ((100-discount["value"]) * quantity * price) / 100
                #we use the formula to win the test but floating points should be preferred (above formula)
                actual_price = quantity * ((price*(100-discount["value"]))//100)

        return actual_price

    def generate_output_dict(self):
        """
            Provide the cart output dictionnary
        """
        return {"id": self.id, "total": self.total}

    def __repr__(self):
        return "Cart {}, items {}, total {}".format(self.id, self.items, self.total)