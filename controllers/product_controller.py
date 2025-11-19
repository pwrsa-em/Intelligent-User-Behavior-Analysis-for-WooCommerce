from models.product_model import ProductModel
from views.api_response import success

class ProductController:
    def __init__(self):
        self.product_model = ProductModel()

    def get_product(self, product_id):
        product = self.product_model.get_product(product_id)
        return success(product)

    def get_all_products(self):
        products = self.product_model.get_all_products()
        return success(products)