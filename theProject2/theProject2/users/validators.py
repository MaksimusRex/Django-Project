import re

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class UsernameWordCharValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Make sure that the username contains only letters, numbers and underscores."
        else:
            self.__message = value

    def __call__(self, value, *args, **kwargs):
        regex = r'^\w*$'
        if not re.match(regex, value):
            raise ValidationError(self.message)



