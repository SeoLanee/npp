from django.db import models
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class WhitelistEmailValidator(EmailValidator):
    def __init__(self, allowlist=None, *args, **kwargs):
        if allowlist is None:
            allowlist = []
        self.allowlist = allowlist
        super().__init__(*args, **kwargs)

    def validate_domain_part(self, domain_part):
        if domain_part != 'sogang.ac.kr':
            return False
        return True

    def __eq__(self, other):
        return isinstance(other, WhitelistEmailValidator) and super().__eq__(other)


class Email(models.Model):
    email = models.EmailField(
        primary_key=True,
        max_length=64,
        validators=[WhitelistEmailValidator(allowlist=['sogang.ac.kr'])]
    )
    validated = models.BooleanField(default=False)
    key = models.CharField(max_length=6, blank=False, null=False)
