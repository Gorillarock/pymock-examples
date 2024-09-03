from urllib.parse import urljoin

import requests

from app.constants import BASE_URL

TODO_URL = urljoin(BASE_URL, 'todos')

def get_todos():
  try:
    response = requests.get(TODO_URL)
    if response.ok:
        return response
    return None
  except:
    return None