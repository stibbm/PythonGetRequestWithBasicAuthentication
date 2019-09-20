# Pre-Requisite to run:
# run "pip install requests" from the project directory to install the requests library


# Example Code for how to send get request to FAST api resource and parse result
import json
import requests
from datetime import datetime, date

url = "https://url-path-to-resource.com"

    
response = requests.get(url, auth=('<username>', '<password>'))
print(response.text)

json_response = json.loads(response.text)

## json_response is a dictionary which contains the key-value pairs stored in the json result returned by the API
for key in json_response:
    # key = field name
    # json_response[key] = value stored in that field name
    output = str(key) + ' : ' + str(json_response[key])
    print(output)










