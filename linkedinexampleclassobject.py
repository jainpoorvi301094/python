class User:
    def __init__(self, email, user_name, role, password):
        self.email=email
        self.name=user_name
        self.role=role
        self.password=password

    def change_role(self, new_role):
        self.role=new_role

    def change_pass(self, new_password):
        self.password=new_password

    def get_user_info(self):
        print(f"user {self.name} working as {self.role}: you can contact them at {self.email} ")




