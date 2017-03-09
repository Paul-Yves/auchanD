
class Cart:
    def __init__(self, jsonCart):
        self.id = jsonCart["id"]
        self.items = jsonCart["items"]
        self.errorList = []

    def compute_total(self, catalog, delivery_fees):
        self.errorList = []
        total = 0
        for item_dict in self.items:
            article_detail = next((article for article in catalog if article["id"] == item_dict["article_id"]), None)
            if(article_detail == None):
                self.errorList.append("Error, article {} not found in catalog".format(item_dict["article_id"]))
                #mechanism of exception to refine if the article is not found
            total += item_dict["quantity"] * article_detail["price"]
        self.total = total
        if(delivery_fees != None):
            self.reduce_price(delivery_fees)

        return total

    def reduce_price(self, delivery_fees):
        fee = 0
        for fee_dict in delivery_fees:
            volumeInterval = fee_dict["eligible_transaction_volume"]
            if(self.total<volumeInterval["max_price"] and self.total>=volumeInterval["min_price"]):
                fee = fee_dict["price"]

        self.total = self.total - fee

    def generate_output_dict(self):
        """
            Provide the cart output dictionnary
        """
        return {"id": self.id, "total": self.total}

    def __repr__(self):
        return "Cart {}, items {}, total {}".format(self.id, self.items, self.total)