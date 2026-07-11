class User:
    """A model of a general user"""

    def __init__(self, first_name, last_name, login_attempts):
        """Initializing attributes"""
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.login_attempts = login_attempts

    def describe_user(self):
        """A brief description of the user using the first and last names"""
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")

    def greet_user(self):
        """A greeting to the user"""
        print(f"Hello {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        """A method to increase the login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """A method that resets the login attempts to 0"""
        self.login_attempts = 0