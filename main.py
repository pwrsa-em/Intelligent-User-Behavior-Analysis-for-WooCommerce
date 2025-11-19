from controllers.user_controller import UserController
from controllers.product_controller import ProductController
from controllers.event_controller import EventController
from controllers.ml_controller import MLController
from views.dashboard_view import DashboardView

if __name__ == "__main__":
   
    user_ctrl = UserController()
    product_ctrl = ProductController()
    event_ctrl = EventController()
    ml_ctrl = MLController()


    all_users = user_ctrl.get_all_users()
    print("Users:", all_users)


    all_products = product_ctrl.get_all_products()
    print("Products:", all_products)


    all_events = event_ctrl.get_all_events()
    print("Events:", all_events)


    training_data = ml_ctrl.generate_training_data()
    print("Training Features:", training_data['features'].head())


    dashboard = DashboardView(
        user_features=training_data['users'],
        product_data=training_data['products'],
        events=training_data['events']
    )
    dashboard.render_summary()
    dashboard.render_top_products(top_n=5)