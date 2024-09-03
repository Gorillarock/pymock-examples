# Third-party imports...
from unittest.mock import Mock, patch

import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../app'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

from app.services import get_todos
import unittest

class TestAPIMethods(unittest.TestCase):
    def test_request_response(self):
        test_request_mock()

@patch('services.requests.get') # Finds the services module and replaces requests.get with a Mock object
def test_request_mock(mock_get):
    mock_get.return_value.ok = True

    # Send a request to the API server and store the response.
    response = get_todos()

    # Confirm that the request-response cycle completed successfully.
    mock_get.assert_called_once()
    print('Arg list: ', mock_get.get_args_list())
    assert(response.ok != None)

if __name__ == '__main__':
    unittest.main()