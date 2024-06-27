
#this class will act as Basemodel to all product classes
#I am cosidering making it accept dictionary arguments
class product:
    def __init__(
            self, 
            Product_id,
            Product_Name,
            Product_type,
            Sizes,
            Product_Price
):
        self.Product_id = Product_id
        self.Product_Name = Product_Name
        self.Product_type = Product_type
        self.Sizes = Sizes
        self.Product_Price = Product_Price

