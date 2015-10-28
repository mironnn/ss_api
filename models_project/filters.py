__author__ = 'sever'


def model_to_dict(obj):
    res = {}
    keys = obj._meta.fields
    for key in keys:
        res['key'] = obj.key
    return res
        

