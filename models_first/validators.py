__author__ = 'sever'


def validate(filters, attr_list):
    return {k: v for (k, v) in filters.items() if v and k in attr_list}