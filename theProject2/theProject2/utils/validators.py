from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class AgeLimitValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Age should be between 18 and 120 years."
        else:
            self.__message = value

    def __call__(self, value, *args, **kwargs):
        if value < 18 or value > 120:
            raise ValidationError(self.message)