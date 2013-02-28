import json


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
