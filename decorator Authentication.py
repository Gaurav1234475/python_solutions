from enum import Enum

class AuthorixationError(Exception):
    """raised when a user attempts an admin-restricted task"""

class UserType(Enum):
    Regular = 0
    Admin = 1

def admin_required(func):
    def wrapper(self, *args, **kwargs):
        if self.user_type is UserType.Admin:
            return func(self,*args, **kwargs)
        else:
            raise AuthorixationError(f"User must be an admin to use {func.__name__}.")

    return wrapper

class User:

    def __init__(self, username, user_type):
        self.username = username
        self.user_type = user_type

    def do_something_regular(self):
        print(f"{self.username} is doing something any regular user can do.")

    @admin_required
    def do_something_admin(self):
        print(f"{self.username} is doing something only an admin can do.")

me = User("MyUsername", UserType.Admin)
me.do_something_regular()
me.do_something_admin()