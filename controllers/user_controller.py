from models.user_model import UserModel
from views.api_response import success

class UserController:
    def __init__(self):
        self.user_model = UserModel()

    def get_user(self, user_id):
        user = self.user_model.get_user(user_id)
        return success(user)

    def get_all_users(self):
        users = self.user_model.get_all_users()
        return success(users)
