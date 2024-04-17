def validate_user(request, user):
    if user.is_superuser():
        print('pass')
        return user.is_superuser

def create_user(self, *args):
    self.is_superuser = True
