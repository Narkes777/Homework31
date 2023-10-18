class User:
    def __init__(self, username, email, password):
        self.__username = username
        self.__email = email
        self.__password = password

    def get_username(self):
        return self.__username

    def set_username(self, new_username):
        self.__username = new_username

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        self.__email = new_email

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        self.__password = new_password

    def display_info(self):
        return f"Логин: {self.__username}, Email: {self.__email}"

    def validate_password(self, input_password):
        return self.__password == input_password

user1 = User("user123", "user123@mail.ru", "qwerty1234567")
print(user1.display_info())

entered_password = "qwerty1234567"
if user1.validate_password(entered_password):
    print("Пароль верный.")
else:
    print("Неверный пароль.")
