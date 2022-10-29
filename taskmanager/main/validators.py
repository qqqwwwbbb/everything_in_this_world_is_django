import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

'''
The main purpose of these validators is to accept the password like 6 digit pin only
'''


class LengthValidator:
    def __init__(self, length=6, ):
        self.length = length

    def validate(self, password, user=None):
        if len(password) != self.length:
            raise ValidationError(
                _("This password must contain only %(length)d characters."),
                code='password_should_6_digits_pin',
                params={'length': self.length},
            )

    def get_help_text(self):
        return _(
            "Your password must contain only %(length)d characters."
            % {'length': self.length}
        )


class NumberValidator(object):
    def __init__(self, min_digits=6, max_digits=6):
        self.min_digits = min_digits
        self.max_digits = max_digits

    def validate(self, password, user=None):
        if not re.findall('\d{0,10}', password):
            raise ValidationError(
                _("The password must contain only digit between, 0-9. like : 012690"),
                code='only numbers are required',
            )

    def get_help_text(self):
        return _(
            "Your password must contain only digit between, 0-9. like : 012690."
        )


class NoUppercaseValidator(object):
    def validate(self, password, user=None):
        if re.findall('[A-Z]', password):
            raise ValidationError(
                _("The password must not contain uppercase letter, A-Z."),
                code='password_upper',
            )

    def get_help_text(self):
        return _(
            "The password must not contain uppercase letter, A-Z.",
        )


class NoLowercaseValidator(object):
    def validate(self, password, user=None):
        if re.findall('[a-z]', password):
            raise ValidationError(
                _("The password must not contain lowercase letter, a-z."),
                code='password_no_lower',
            )

    def get_help_text(self):
        return _(
            "Your password must not contain lowercase letters, a-z."
        )


class NoSymbolValidator(object):
    def validate(self, password, user=None):
        if re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            raise ValidationError(
                _("The password must not contain any symbol: " +
                  "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"),
                code='password_with_symbol',
            )

    def get_help_text(self):
        return _(
            "Your password must not contain any symbol: " +
            "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
        )
