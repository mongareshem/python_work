from user import User

class Privileges:
    """A separate class for all the special privileges the admin has"""

    def __init__(self, privileges):
        """Initialize the attribute privileges"""
        self.privileges = privileges

    def show_privileges(self):
        """Print out the privileges of the admin"""

        print(f"\nThe following are the Admin privileges: ")
        for privilege in self.privileges:
            print(f"\t\t{privilege.capitalize()}.")

class Admin(User):
    def __init__(self, first_name, last_name, login_attempts):
        super().__init__(first_name, last_name, login_attempts)

        special_permissions = ['can add post', 'can delete post', 'can ban user']
        self.privileges = Privileges(special_permissions)