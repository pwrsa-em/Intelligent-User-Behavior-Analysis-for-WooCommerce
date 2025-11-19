from .repository import Repository

class ProductModel(Repository):
    def add_product(self, wc_product_id, name, category, price):
        query = "INSERT INTO products (wc_product_id, name, category, price) VALUES (%s, %s, %s, %s)"
        self.execute(query, (wc_product_id, name, category, price))

    def get_product(self, product_id):
        query = "SELECT * FROM products WHERE id = %s"
        return self.fetchone(query, (product_id,))

    def get_all_products(self):
        query = "SELECT * FROM products"
        return self.fetchall(query)