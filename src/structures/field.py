from datetime import datetime, date, time


def uuid(value: str):
    return {
        'type': 'UUID',
        'value': value,
    }


def string_field(value: str):
    return {
        'type': 'String',
        'value': value,
    }


def file_field(value):
    return {
        'type': 'File',
        'value': value,
    }


def boolean_field(value: bool):
    return {
        'type': 'Boolean',
        'value': value,
    }


def integer_field(value: int):
    return {
        'type': 'Integer',
        'value': value,
    }


def float_field(value: float):
    return {
        'type': 'Float',
        'value': value,
    }


def date_time_field(value: datetime):
    return {
        'type': 'DateTime',
        'value': value,
    }


def date_field(value: date):
    return {
        'type': 'Date',
        'value': value,
    }


def time_field(value: time):
    return {
        'type': 'Time',
        'value': value,
    }


def dict_field(value: dict):
    return {
        'type': 'Dict',
        'value': value,
    }


def list_field(value: list):
    return {
        'type': 'List',
        'value': value,
    }
