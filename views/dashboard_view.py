
class DashboardView:
    def __init__(self, user_features, product_data, events):
        self.user_features = user_features
        self.product_data = product_data
        self.events = events


    def render_summary(self):
        print("===== DASHBOARD SUMMARY =====")
        print(f"Total Users: {len(self.user_features)}")
        print(f"Total Products: {len(self.product_data)}")
        print(f"Total Events: {len(self.events)}")


    def render_top_products(self, top_n=5):
        top_products = self.events.groupby('product_id').size().sort_values(ascending=False).head(top_n)
        print("===== TOP PRODUCTS =====")
        print(top_products)


    def render_user_activity(self, user_id):
        user = self.user_features[self.user_features['user_id'] == user_id]
        if not user.empty:
            print(f"User {user_id} Activity Score: {user['user_activity_score'].values[0]}")
        else:
            print(f"User {user_id} not found.")