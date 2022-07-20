from typing import Tuple
from requests.models import Response
import requests

def make_request(uri: str) -> Tuple[Response, bool]:
    """
        Method that make a API request
    """
    try:
        response = requests.get(uri)

        if response.status_code == 200:
            print('Success API request!')
            return response, True
        else:
            print('Not Found.')
            return response, False
    except Exception as e:
        msg = f"Error when try to make request: \n" \
              f"Uri: {uri} \n" \
              f"Traceback: {e}"
        print(msg)
        return None, False