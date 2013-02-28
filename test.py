import json
import json_dec

json_data = open("test.json")


def test():
    test_class = JsonTest()
    assert test_class.first_name == "Steve"
    assert test_class.last_name == "Smith"
    assert test_class.pin == [1,2,3]
    assert test_class.test_dict == {"lol": 0, "teehee": 1}


class JsonTest(object):

    @json_decorate(json_data)
    def __init__(self):
        pass
