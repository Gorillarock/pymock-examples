from unittest.mock import Mock, patch

import json

json = Mock()
json.dumps({'a':1})
print(dir(json))

print(json.dumps.assert_called())
json.dumps.assert_called_once_with({'a':1})
json.reset_mock()
json.dumps({'b':2})
json.loads('{"a":1}')
print(json.dumps.assert_called_with({'b':2}))
print('Count: ' + str(json.dumps.call_count))
print('dumps Args: ' + str(json.dumps.call_args))
print('loads Args: ' + str(json.loads.call_args))
print('Calls: ' + str(json.method_calls))
print(json.dumps.assert_called_once()) # will fail