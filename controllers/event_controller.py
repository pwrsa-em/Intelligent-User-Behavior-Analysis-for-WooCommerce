from models.event_model import EventModel
from views.api_response import success

class EventController:
    def __init__(self):
        self.event_model = EventModel()

    def add_event(self, user_id, product_id, event_type, value=None):
        self.event_model.add_event(user_id, product_id, event_type, value)
        return success({'message': 'Event added successfully'})

    def get_events_by_product(self, product_id):
        events = self.event_model.get_events_by_product(product_id)
        return success(events)

    def get_all_events(self):
        events = self.event_model.get_all_events()
        return success(events)


