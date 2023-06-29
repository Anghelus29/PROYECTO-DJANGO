from django.core.exceptions import ValidationError


def validation_paginas(value):
    if value>500:
        raise ValidationError(
            "%(value)s La cantidad de paginas no es permitida",
            params={"value": value},
        )
    
def validation_edad(value):
    if value>100:
        raise ValidationError(
            "%(value)s La edad no es permitida",
            params={"value": value},
        )
