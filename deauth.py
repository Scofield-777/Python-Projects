#!/usr/bin/env python

import requests

url = "mailagoogle.com"
try:
    get_response = requests.get("http://" + url)
    print(get_response)
except requests.exceptions.ConnectionError:
    print("Invalid Domain")
