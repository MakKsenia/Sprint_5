from random import randint

class Helper:
    @staticmethod
    def generate_email():
        return f"kseniamak+{randint(0, 9999)}@yandex.ru"