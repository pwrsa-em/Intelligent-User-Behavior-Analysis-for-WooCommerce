from .repository import Repository

class UserModel(Repository):
    def create_user(self, wp_user_id=None, device_id=None):
        query = "INSERT INTO users (wp_user_id, device_id) VALUES (%s, %s)"
        self.execute(query, (wp_user_id, device_id))

    def get_user(self, user_id):
        query = "SELECT * FROM users WHERE id = %s"
        return self.fetchone(query, (user_id,))

    def get_all_users(self):
        query = "SELECT * FROM users"
        return self.fetchall(query)