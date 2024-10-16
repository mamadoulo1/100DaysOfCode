import requests
import warnings
from urllib3.exceptions import InsecureRequestWarning
import html


warnings.simplefilter('ignore', InsecureRequestWarning)

parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php", params=parameters,verify=False)
response.raise_for_status()
question_data = response.json()['results']