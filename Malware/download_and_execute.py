#!/usr/bin/env python
import requests

def download(url):
    get_respone = requests.get(url)
    # When Dealing with Files We need to use "with"
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_respone.content)

download("https://www.agtauto.com/wp-content/uploads/2019/07/dodge-challenger-srt-hellcat-red.jpg")
