from .repository import Repository

class EventModel(Repository):
    def add_event(self, user_id, product_id, event_type, value=None):
        query = "INSERT INTO user_events (user_id, product_id, event_type, value) VALUES (%s, %s, %s, %s)"
        self.execute(query, (user_id, product_id, event_type, value))

    def get_events_by_product(self, product_id):
        query = "SELECT * FROM user_events WHERE product_id = %s"
        return self.fetchall(query, (product_id,))

    def get_all_events(self):
        query = "SELECT * FROM user_events"
        return self.fetchall(query)
