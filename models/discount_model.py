from .repository import Repository

class DiscountModel(Repository):
    def save_discount(self, product_id, score, recommended_discount):
        query = "INSERT INTO discount_recommendations (product_id, score, recommended_discount) VALUES (%s, %s, %s)"
        self.execute(query, (product_id, score, recommended_discount))

    def get_latest_discount(self, product_id):
        query = "SELECT * FROM discount_recommendations WHERE product_id = %s ORDER BY id DESC LIMIT 1"
        return self.fetchone(query)