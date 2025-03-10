class UserManager:
    def __init__(self):
        # This is some tricky part to understand - at a first look we thing \
        # it will create a new instance users variable every time while \
        # creating a new instance / object of that class it's true but all \
        # instance variable refer to the same dict.
        self.users = {}

    def add_user(self, username, email):
        if username in self.users:
            raise ValueError("User already exists")
        self.users[username] = email

        return True

    def get_user(self, username):
        return self.users.get(username)
