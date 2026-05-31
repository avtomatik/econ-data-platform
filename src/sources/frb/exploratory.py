import io

import requests

from sources.frb.constants import API_URL
from sources.frb.readers import read_api_response


def run() -> None:
    response = requests.get(API_URL)
    content = io.BytesIO(response.content)
    read_api_response(content)
