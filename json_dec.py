import json


json_data = open("test.json")


def json_decorate(json_source):
    def decorator(init):
        def wrapper(self, *args):
            json_obj = json.load(json_source)
            if isinstance(json_obj, dict):
                for key, value in json_obj.iteritems():
                    setattr(self, key, value)
            init(self, *args)
        return wrapper
    return decorator


def test():
    q = JsonTest()
    print q.first_name
    print q.last_name
    print q.pin
    return q


class JsonTest(object):

    @json_decorate(json_data)
    def __init__(self):
        pass
