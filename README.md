# What does this decorator do?
This decorator makes it simple to map JSON values (whether from an API call or a database query) to class attributes. It's a simple way to create Python objects from JSON. 

``` python
import json_dec

class JsonTest(object):

    @json_decorate(json_data_source_goes_here)
    def __init__(self):
        pass
```

# To do
Currently, more complicated JSON (nested lists of json entries, for example) requires some pruning if you want to map it to the class accurately. In these cases its helpful to write functions that return the JSON data you want and then passing these to the decorators. However, I would like to add the ability to handle some of this automagically. 