import re


def validate_service_name(value):
    return re.match(r'^[\w.@+-]{1,150}\Z', value)
