__author__ = 'sever'


def validate(filters, attr_list):
    """
    Checks attributes for values from request GET and checks if their exists in model attributes
    :param filters: dict with attributes in request GET
    :param attr_list: model attributes
    :return: dict with attributes and values
    """
    return {k: v for (k, v) in filters.items() if v and k in attr_list}